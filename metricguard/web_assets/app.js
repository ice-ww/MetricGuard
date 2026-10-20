"use strict";
const el = id => document.getElementById(id);
let token, pending = null, timer, view = 0, taskState = null, pendingAnswer = null, historyView = 0;
let shownQuestion = null, staleSignature = "";
let currentTaskId=null, readController=null, writing=false, needsManualRefresh=false;
let connected=false, recoveryDeadline=null, recoveryAttempt=0, recoveryStopped=false;
let composing=!new URLSearchParams(location.search).has("task");
function gateWrites() {
  if(!connected) for(const id of ["submit","answer-submit","rerun","unknown-answer-retry"]) el(id).disabled=true;
}
function connectionFailed(message) {
  connected=false;gateWrites();
  if(composing) el("fields").disabled=false;
  if(taskState?.clarification) el("answer-fields").disabled=false;
  el("reconnect").hidden=false;
  el("connection").dataset.state="unavailable";
  el("connection").textContent=message+" 以下为最后已知信息，已显示内容可能过期；可编辑、复制，提交已暂停。";
}
function resetRecovery() {recoveryDeadline=null;recoveryAttempt=0;recoveryStopped=false;}
function recoveryExpired() {
  if(recoveryDeadline!==null && Date.now()>=recoveryDeadline) {
    recoveryStopped=true;
    connectionFailed("自动重连已停止（已达两分钟上限）。请确认本机服务后立即重连。");
  }
  return recoveryStopped;
}
function retryState(id,generation) {
  recoveryDeadline ??= Date.now()+120000;
  if(recoveryExpired()) return;
  const delay=[1000,2000,4000,8000][recoveryAttempt++] || 10000;
  if(!document.hidden) timer=setTimeout(()=>{
    if(!recoveryExpired()) showTask(id,generation);
  },Math.min(delay,recoveryDeadline-Date.now()));
}
function reconnect() {
  if(writing || readController || (!currentTaskId && !composing)) return;
  resetRecovery();showTask(currentTaskId);
}
function recoverWriteConnection(error) {
  if(knownWriteRejection(error)) return;
  connectionFailed("提交结果尚未确认，请先恢复连接；原内容和操作标识已保留。");
  if([401,403].includes(error.status) && error.code!=="session_expired") {
    recoveryStopped=true;connectionFailed(error.message+" 访问被拒绝，已停止自动重连。");
  } else retryState(currentTaskId,view);
}
function knownWriteRejection(error) {return error.status && error.status<500 && ![401,403].includes(error.status);}
function stopReading() {clearTimeout(timer);readController?.abort();readController=null;}
const composeFields=["snapshot","question","start","end","previous-start","previous-end"];
function saveCompose() {
  if(!el("fields").disabled) drafts.saveCompose(Object.fromEntries(composeFields.map(id=>[id,el(id).value])));
}
function restoreCompose() {
  const saved=drafts.compose();
  if(saved && typeof saved==="object") for(const id of composeFields) {
    if(typeof saved[id]==="string") el(id).value=saved[id];
  }
}
el("analysis-form").addEventListener("input",saveCompose);
el("analysis-form").addEventListener("change",saveCompose);
function saveAnswer() {
  if(taskState?.clarification && !el("answer-fields").disabled)
    drafts.saveAnswer(taskState.id,taskState.clarification,el("answer").value);
}
el("answer").addEventListener("input",saveAnswer);
const names = {created:"准备执行",running:"正在分析",waiting:"等待澄清",ended:"已结束",failed:"执行失败",interrupted:"已中断"};
async function api(path, data, signal) {
  const response = await fetch(path, {method:data?"POST":"GET", headers:{"X-MetricGuard-Token":token,"Content-Type":"application/json"},body:data?JSON.stringify(data):undefined,signal,redirect:"error"});
  const value=await response.json();
  if(!response.ok) {const error=new Error(value.error || "请求未完成，请重新打开任务。");error.status=response.status;error.code=value.code;throw error;}
  return value;
}
async function readTask(id,signal,generation) {
  if(!id) {
    const config=await api("/api/config",undefined,signal);
    if(signal.aborted || generation!==view) throw new DOMException("读取已取消","AbortError");
    if(typeof config.token!=="string" || !config.token) throw new Error("无法核对服务会话。");
    token=config.token;return null;
  }
  const path="/api/tasks/"+encodeURIComponent(id);
  try {return await api(path,undefined,signal);}
  catch(error) {
    if(error.status!==403 || error.code!=="session_expired") throw error;
    connectionFailed("页面会话已失效，正在重新核对原任务。");
    const config=await api("/api/config",undefined,signal);
    if(signal.aborted || generation!==view) throw new DOMException("读取已取消","AbortError");
    if(typeof config.token!=="string" || !config.token || config.token===token) throw error;
    token=config.token;
    // Only one session refresh per read, under the original ten-second deadline.
    return await api(path,undefined,signal);
  }
}
async function refreshHistory() {
  const generation=++historyView;
  try {
    const result=await api("/api/tasks");
    if(generation!==historyView) return;
    el("history-list").replaceChildren();
    for(const task of result.tasks) {
      const item=document.createElement("li"),link=document.createElement("a"),detail=document.createElement("small");
      link.href="/?task="+encodeURIComponent(task.id);link.textContent=task.question;
      detail.textContent=(names[task.status]||task.status)+" · "+task.snapshot_id+" · "+task.id.slice(0,8);
      item.append(link,detail);el("history-list").append(item);
    }
    el("history-message").textContent=result.tasks.length?"":"尚无历史任务。";
  } catch(error) {
    if(generation!==historyView) return;
    el("history-message").textContent="历史列表读取失败。请确认服务仍在运行后点击刷新列表；已显示内容可能不是最新状态。";
  }
}
el("history-refresh").addEventListener("click",refreshHistory);
function fill(value) {
  el("snapshot").value=value.snapshot_id; el("question").value=value.question;
  ["start","end"].forEach((id,i)=>el(id).value=value.window?.[i]||"");
  ["previous-start","previous-end"].forEach((id,i)=>el(id).value=value.comparison_window?.[i]||"");
}
function windowValue(a,b) {
  const start=el(a).value,end=el(b).value;
  if(!start&&!end) return null;
  if(!start||!end||start>=end) throw new Error("请填写完整日期范围，结束日期须晚于开始日期。");
  return [start,end];
}
function unlock() {el("fields").disabled=false;el("submit").disabled=false;el("submit").formNoValidate=!!pending;el("submit").textContent=pending?"重试相同提交":"开始分析";gateWrites();}
async function showTask(id, generation = ++view) {
  if(recoveryExpired()) return;
  if(!composing && taskState?.id!==id) {
    connectionFailed("正在核对原任务状态，请稍候。");
  }
  stopReading();currentTaskId=id;needsManualRefresh=false;
  const controller=new AbortController();readController=controller;
  if(!composing) {el("empty").hidden=true;el("task").hidden=false;el("new").hidden=false;}
  el("task-link").textContent="任务 "+id;el("task-link").href="/?task="+encodeURIComponent(id);
  let timedOut=false;
  const timeout=setTimeout(()=>{timedOut=true;controller.abort();},Math.min(10000,recoveryDeadline===null?10000:recoveryDeadline-Date.now()));
  try {
    const state=await readTask(id,controller.signal,generation);
    clearTimeout(timeout);
    if(generation!==view || controller.signal.aborted) return;
    connected=true;resetRecovery();el("reconnect").hidden=true;
    if(composing) {
      currentTaskId=null;unlock();el("connection").textContent=id?"连接正常 · 已核对原任务状态":"连接正常 · 已恢复服务连接，原提交仍待确认";
      el("connection").dataset.state="connected";return;
    }
    fill(state);
    el("connection").textContent="连接正常 · 已读取任务状态";el("status").textContent=names[state.status]||state.status;
    el("connection").dataset.state="connected";
    renderProgress(state);
    renderBudget(state);
    el("elapsed").textContent=state.elapsed_seconds===null?"运行历时未完整记录":"本次运行历时 "+state.elapsed_seconds+" 秒";
    el("task-question").textContent=state.question;
    el("scope").textContent=state.window?(state.window_confirmed?"分析范围：":"请求范围（尚未分析）：")+state.window[0]+" 至 "+state.window[1]+"（结束日不包含）":"";
    if(taskState?.id!==state.id || taskState?.status!==state.status) refreshHistory();
    taskState=state;renderClarification(state);renderRecovery(state);
    el("result").textContent=state.body;
    el("report-view").replaceChildren();
    if(!["created","running","waiting"].includes(state.status)) {
      try {
        const report=await api("/api/tasks/"+encodeURIComponent(id)+"/report",undefined,controller.signal);
        if(generation!==view || controller.signal.aborted) return;
        renderReport(report,el("report-view"));
      } catch(error) {
        if(generation!==view || controller.signal.aborted) return;
        needsManualRefresh=true;
        el("report-view").textContent="报告读取失败。请刷新重试；已有文本报告和任务记录仍保留。";
      }
    }
    el("text-report").hidden=!state.body;
    if(!document.hidden && ["created","running","waiting"].includes(state.status))
      timer=setTimeout(()=>showTask(id,generation),state.status==="waiting"?5000:1000);
  } catch(error) {
    if(generation!==view || (controller.signal.aborted && !timedOut)) return;
    needsManualRefresh=false;
    connectionFailed(timedOut?"任务状态读取超过 10 秒，连接异常。":"暂时无法读取任务，连接异常。");
    if(error.status===403 || error.status===401) {
      recoveryStopped=true;connectionFailed(error.message+" 访问被拒绝，已停止自动重连。");
    } else if(error.status===404) {
      recoveryStopped=true;
      if(taskState?.id!==id) {
        el("budget").hidden=true;
        el("stale-drafts").hidden=true;el("unknown-answer").hidden=true;
        taskState=null;el("clarification").hidden=true;el("recovery-actions").hidden=true;el("parent-link").hidden=true;el("recovery-message").textContent="";el("status").textContent="无法打开任务";
        for(const name of ["result","report-view","scope","elapsed","task-question","current-action","progress-time","progress-notice"]) el(name).textContent="";
      }
      connectionFailed(error.message+" 已停止自动重连，请核对启动地址和工作目录。");
    } else {
      el("progress-notice").textContent="";
      retryState(id,generation);
    }
  } finally {
    clearTimeout(timeout);
    if(readController===controller) readController=null;
  }
}
el("task-refresh").addEventListener("click",reconnect);
el("reconnect").addEventListener("click",reconnect);
document.addEventListener("visibilitychange",()=>{
  if(document.hidden) {clearTimeout(timer);if(!writing) stopReading();}
  else if((currentTaskId || (!connected && composing)) && !writing && !needsManualRefresh && !recoveryExpired()) showTask(currentTaskId);
});
function renderBudget(state) {
  const budget=state.budget;
  el("budget").hidden=!budget;
  if(!budget) return;
  el("budget-summary").textContent=`已计入预算：模型 ${budget.model_calls} / ${budget.limits.model} 次 · 工具 ${budget.tool_calls} / ${budget.limits.tool} 次`;
  el("budget-tokens").textContent=`Token 预算占用：${budget.tokens} / ${budget.limits.tokens}；已知用量：${budget.known_tokens}；保留预留量：${budget.reserved_tokens}`;
  el("budget-unknown").textContent=`尚待确认用量：${budget.pending_calls} 次；用量未知：${budget.unknown_calls} 次。`;
  el("budget-time").textContent=`累计时间预算（服务已确认）：${budget.active_seconds.toFixed(3)} / ${budget.limits.active_seconds} 秒；与本次运行历时不同，不随页面计时增长。`;
  const labels={model:"模型计入次数",tool:"工具计入次数",tokens:"Token 预算占用"};
  el("budget-notice").textContent=budget.near_limits.map(key=>labels[key]+"已达上限的 80%"+(key==="tokens"?"（可能含预留）":"")+" 或以上。").join(" ");
  el("budget-stop").textContent=budget.stopped_reason||"";
}
function renderProgress(state) {
  const progress=state.progress||{};
  const fallback={created:"准备执行",running:"正在分析（未记录具体动作）",waiting:"等待澄清",ended:"无（已结束）",failed:"无（执行失败）",interrupted:"无（已中断）"};
  el("current-action").textContent="当前动作："+(progress.action||fallback[state.status]||"未记录");
  el("progress-time").textContent="最近可靠进展："+(progress.latest_at?new Date(progress.latest_at).toLocaleString("zh-CN",{hour12:false})+"（本地时间）":"未记录");
  el("progress-notice").textContent=progress.quiet?"已至少 60 秒没有新的执行进展记录，当前动作可能仍在进行。这不表示任务失败，不会自动重试。":"";
}
function renderRecovery(state) {
  el("recovery-actions").hidden=false;
  el("recovery-message").textContent=state.recovery_message;
  el("parent-link").hidden=!state.parent;
  if(state.parent) el("parent-link").href="/?task="+encodeURIComponent(state.parent);
  el("rerun").hidden=!["ended","failed","interrupted"].includes(state.status);
  el("rerun").disabled=false;el("copy").disabled=false;
  const saved=sessionStorage.getItem("metricguard-rerun:"+state.id);
  el("rerun").textContent=saved?"重试关联重跑":"创建关联重跑";
  el("rerun-error").textContent=saved?"上次重跑尚未确认。重试将沿用同一操作，不会重复创建任务。":"";
}
el("copy").addEventListener("click",()=>{
  if(!taskState) return;
  const source=taskState;
  el("new").click();fill(source);saveCompose();el("question").focus();
  el("error").textContent="已复制问题、快照和明确日期。请修改并点击开始分析；新任务不会继承旧结论或证据。";
});
el("rerun").addEventListener("click",async()=>{
  if(!taskState || !connected || writing) return;
  const id=taskState.id, generation=++view, key="metricguard-rerun:"+id;
  stopReading();writing=true;
  const saved=sessionStorage.getItem(key), data=saved?JSON.parse(saved):{request_id:crypto.randomUUID()};
  sessionStorage.setItem(key,JSON.stringify(data));
  el("rerun").disabled=true;el("copy").disabled=true;el("new").disabled=true;el("rerun-error").textContent="";
  try {
    const result=await api("/api/tasks/"+id+"/rerun",data);
    if(generation!==view) return;
    sessionStorage.removeItem(key);el("new").disabled=false;
    history.pushState(null,"","/?task="+encodeURIComponent(result.id));
    await showTask(result.id,generation);
  } catch(error) {
    if(generation!==view) return;
    if(knownWriteRejection(error)) sessionStorage.removeItem(key);
    el("rerun-error").textContent=error.message;
    el("rerun").disabled=false;el("copy").disabled=false;el("new").disabled=false;
    el("rerun").textContent=sessionStorage.getItem(key)?"重试关联重跑":"创建关联重跑";
    recoverWriteConnection(error);
  } finally {
    writing=false;
  }
});
function renderClarification(state) {
  const question=state.clarification;
  el("clarification").hidden=!question;
  const storageKey="metricguard-answer:"+state.id;
  const saved=sessionStorage.getItem(storageKey);
  pendingAnswer=saved?JSON.parse(saved):null;
  const currentPending=pendingAnswer && drafts.matches(pendingAnswer,question);
  el("answer-submit").formNoValidate=!!currentPending;
  el("unknown-answer-retry").disabled=!connected;
  el("unknown-answer").hidden=!pendingAnswer;
  el("unknown-answer-retry").hidden=!!currentPending;
  if(pendingAnswer) el("unknown-answer-text").value=pendingAnswer.answer;
  renderStaleDrafts(state);
  if(!question) {shownQuestion=null;return;}
  const identity=JSON.stringify([state.id,question.question_id,question.version,pendingAnswer?.request_id]);
  if(shownQuestion===identity) {
    el("answer-submit").disabled=!!pendingAnswer && !currentPending;
    el("unknown-answer-retry").disabled=false;
    gateWrites();return;
  }
  shownQuestion=identity;
  el("known-information").textContent=question.known_information||"";
  el("clarification-prompt").textContent=question.prompt;
  el("answer-options").replaceChildren();
  for(const option of question.options||[]) {
    const button=document.createElement("button");button.type="button";button.textContent=option;
    button.addEventListener("click",()=>{el("answer").value=option;saveAnswer();el("answer").focus();});
    el("answer-options").append(button);
  }
  el("answer").value=drafts.answer(state.id,question)?.answer ?? (currentPending?pendingAnswer.answer:"");
  el("answer-fields").disabled=false;el("answer-submit").disabled=!!pendingAnswer && !currentPending;el("answer-refresh").disabled=false;
  el("answer-submit").textContent=currentPending?"重试相同回答":"提交回答";
  el("answer-error").textContent=pendingAnswer?"上次回答尚未确认。重试沿用同一操作，不会重复执行。":"";
  gateWrites();
}
function renderStaleDrafts(state) {
  const old=drafts.answers(state.id).filter(d=>d.answer && !drafts.matches(d,state.clarification) &&
    !(drafts.matches(d,pendingAnswer) && d.answer===pendingAnswer.answer));
  const signature=JSON.stringify([state.id,old]);
  if(signature===staleSignature) return;
  staleSignature=signature;
  const area=el("stale-drafts");area.hidden=!old.length;area.replaceChildren();
  if(!old.length) return;
  const message=document.createElement("p");
  message.textContent="问题已更新或已被回答。以下旧草稿保留供复制，不会自动填入或提交给新问题。";area.append(message);
  for(const draft of old) {
    const label=document.createElement("p"),text=document.createElement("textarea");
    label.textContent="旧问题（版本 "+draft.version+"）："+(draft.prompt||"未记录");
    text.readOnly=true;text.value=draft.answer;text.setAttribute("aria-label","旧回答草稿（版本 "+draft.version+"）");
    area.append(label,text);
  }
}
el("answer-form").addEventListener("submit",async event=>{
  event.preventDefault();
  if(!taskState?.clarification) return;
  if(pendingAnswer && !drafts.matches(pendingAnswer,taskState.clarification)) return;
  const question=taskState.clarification;
  await sendAnswer(pendingAnswer || {request_id:crypto.randomUUID(),question_id:question.question_id,version:question.version,answer:el("answer").value});
});
el("unknown-answer-retry").addEventListener("click",()=>{if(pendingAnswer) sendAnswer(pendingAnswer);});
async function sendAnswer(data) {
  if(writing || !connected) return;
  const generation=++view;stopReading();writing=true;
  const id=taskState.id, storageKey="metricguard-answer:"+id;
  pendingAnswer=data;
  sessionStorage.setItem(storageKey,JSON.stringify(pendingAnswer));
  el("unknown-answer-retry").disabled=true;
  el("answer-fields").disabled=true;el("answer-submit").disabled=true;el("answer-refresh").disabled=true;el("new").disabled=true;el("answer-error").textContent="";
  try {
    await api("/api/tasks/"+id+"/answers",pendingAnswer);
    if(generation!==view) return;
    drafts.clearAnswer(id,data);shownQuestion=null;
    pendingAnswer=null;sessionStorage.removeItem(storageKey);el("new").disabled=false;
    await showTask(id,generation);
  } catch(error) {
    if(generation!==view) return;
    if(knownWriteRejection(error)) {pendingAnswer=null;sessionStorage.removeItem(storageKey);el("answer-fields").disabled=false;}
    el("answer-error").textContent=error.message;
    el("answer-submit").formNoValidate=!!pendingAnswer && !!drafts.matches(pendingAnswer,taskState.clarification);
    el("answer-submit").disabled=false;el("answer-refresh").disabled=false;el("new").disabled=false;
    if(!drafts.matches(data,taskState.clarification)) {
      shownQuestion=null;renderClarification(taskState);
      el("unknown-answer-error").textContent=error.message+" 原回答提交结果尚未确认，可手动重试。";
    } else el("answer-submit").textContent=pendingAnswer?"重试相同回答":"提交回答";
    recoverWriteConnection(error);
  } finally {
    writing=false;
    el("unknown-answer-retry").disabled=!connected;
  }
}
el("answer-refresh").addEventListener("click",reconnect);
el("analysis-form").addEventListener("submit",async event=>{
  event.preventDefault();
  if(!connected || writing) return;
  const generation=++view;stopReading();writing=true;
  event.preventDefault();el("error").textContent="";el("submit").disabled=true;el("new").disabled=true;
  try {
    if(!pending) pending={request_id:crypto.randomUUID(),question:el("question").value,snapshot_id:el("snapshot").value,window:windowValue("start","end"),comparison_window:windowValue("previous-start","previous-end")};
    sessionStorage.setItem("metricguard-pending",JSON.stringify(pending));el("fields").disabled=true;el("new").hidden=false;
    const value=await api("/api/tasks",pending);
    if(generation!==view) return;
    el("new").disabled=false;
    drafts.clearCompose(pending);
    pending=null;sessionStorage.removeItem("metricguard-pending");
    composing=false;
    history.pushState(null,"","/?task="+encodeURIComponent(value.id));
    await showTask(value.id,generation);
  } catch(error) {
    if(generation!==view) return;
    el("new").disabled=false;
    el("error").textContent=error.message;
    el("submit").disabled=false;el("submit").textContent=pending?"重试相同提交":"开始分析";
    el("submit").formNoValidate=!!pending;
    if(pending) recoverWriteConnection(error);
  } finally {
    writing=false;
  }
});
el("new").addEventListener("click",()=>{
  view++;stopReading();if(connected) currentTaskId=null;
  composing=true;shownQuestion=null;taskState=null;pendingAnswer=null;history.pushState(null,"","/");
  el("task").hidden=true;el("empty").hidden=false;el("status").textContent="尚未开始";el("new").hidden=true;el("error").textContent="";
  el("analysis-form").reset();restoreCompose();unlock();
  if(!connected && currentTaskId && !recoveryExpired()) retryState(currentTaskId,view);
});
window.addEventListener("popstate",()=>location.reload());
(async()=>{
  try {
    const config=await (await fetch("/api/config")).json();token=config.token;connected=true;
    for(const name of config.snapshots){const option=document.createElement("option");option.value=name;option.textContent=name;el("snapshot").append(option);}
    if(config.example){el("example").hidden=false;el("example").addEventListener("click",()=>{fill(config.example);saveCompose();});}
    unlock();refreshHistory();
    const id=new URLSearchParams(location.search).get("task");
    if(id){el("fields").disabled=true;el("submit").disabled=true;await showTask(id);return;}
    const saved=sessionStorage.getItem("metricguard-pending");
    if(saved){pending=JSON.parse(saved);fill(pending);restoreCompose();unlock();el("new").hidden=false;el("error").textContent="上次提交尚未确认。重试仍提交原问题「"+pending.question+"」及原条件；草稿修改不会替换原操作。";}
    else restoreCompose();
  } catch(error){el("error").textContent="无法连接本机服务，请检查启动终端后刷新。";}
})();
