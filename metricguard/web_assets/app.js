"use strict";
const el = id => document.getElementById(id);
let token, pending = null, timer, view = 0, taskState = null, pendingAnswer = null, historyView = 0;
const names = {created:"准备执行",running:"正在分析",waiting:"等待澄清",ended:"已结束",failed:"执行失败",interrupted:"已中断"};
async function api(path, data) {
  const response = await fetch(path, {method:data?"POST":"GET", headers:{"X-MetricGuard-Token":token,"Content-Type":"application/json"},body:data?JSON.stringify(data):undefined});
  const value=await response.json();
  if(!response.ok) {const error=new Error(value.error || "请求未完成，请重新打开任务。");error.status=response.status;throw error;}
  return value;
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
function unlock() {el("fields").disabled=false;el("submit").disabled=false;el("submit").textContent="开始分析";}
async function showTask(id, generation = ++view) {
  clearTimeout(timer);
  el("empty").hidden=true;el("task").hidden=false;el("new").hidden=false;
  el("task-link").textContent="任务 "+id;el("task-link").href="/?task="+encodeURIComponent(id);
  try {
    const state=await api("/api/tasks/"+encodeURIComponent(id));
    if(generation!==view) return;
    fill(state);
    el("connection").textContent="";el("status").textContent=names[state.status]||state.status;
    el("elapsed").textContent=state.elapsed_seconds===null?"运行历时未完整记录":"本次运行历时 "+state.elapsed_seconds+" 秒";
    el("task-question").textContent=state.question;
    el("scope").textContent=state.window?(state.window_confirmed?"分析范围：":"请求范围（尚未分析）：")+state.window[0]+" 至 "+state.window[1]+"（结束日不包含）":"";
    if(taskState?.id!==state.id || taskState?.status!==state.status) refreshHistory();
    taskState=state;renderClarification(state);renderRecovery(state);
    el("result").textContent=state.body;
    el("report-view").replaceChildren();
    if(!["created","running","waiting"].includes(state.status)) {
      try {
        const report=await api("/api/tasks/"+encodeURIComponent(id)+"/report");
        if(generation!==view) return;
        renderReport(report,el("report-view"));
      } catch(error) {
        if(generation!==view) return;
        el("report-view").textContent="报告读取失败。请刷新重试；已有文本报告和任务记录仍保留。";
      }
    }
    el("text-report").hidden=!state.body;
    if(["created","running"].includes(state.status)) timer=setTimeout(()=>showTask(id,generation),1000);
  } catch(error) {
    if(generation!==view) return;
    if(error.status===404) {
      taskState=null;el("clarification").hidden=true;el("recovery-actions").hidden=true;el("parent-link").hidden=true;el("recovery-message").textContent="";el("status").textContent="无法打开任务";
      for(const name of ["result","report-view","scope","elapsed","task-question"]) el(name).textContent="";
      el("connection").textContent=error.message+" 请从历史列表选择任务，或新建问题。";
    } else el("connection").textContent="暂时无法读取任务。请确认本机服务仍在运行后刷新；不会自动重新执行。";
  }
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
  el("new").click();fill(source);el("question").focus();
  el("error").textContent="已复制问题、快照和明确日期。请修改并点击开始分析；新任务不会继承旧结论或证据。";
});
el("rerun").addEventListener("click",async()=>{
  if(!taskState) return;
  const id=taskState.id, generation=++view, key="metricguard-rerun:"+id;
  clearTimeout(timer);
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
    if(error.status && error.status<500) sessionStorage.removeItem(key);
    el("rerun-error").textContent=error.message;
    el("rerun").disabled=false;el("copy").disabled=false;el("new").disabled=false;
    el("rerun").textContent=sessionStorage.getItem(key)?"重试关联重跑":"创建关联重跑";
  }
});
function renderClarification(state) {
  const question=state.clarification;
  el("clarification").hidden=!question;
  const storageKey="metricguard-answer:"+state.id;
  const saved=sessionStorage.getItem(storageKey);
  pendingAnswer=saved?JSON.parse(saved):null;
  if(!question || pendingAnswer && (pendingAnswer.question_id!==question.question_id || pendingAnswer.version!==question.version)) {
    pendingAnswer=null;sessionStorage.removeItem(storageKey);
  }
  if(!question) return;
  el("known-information").textContent=question.known_information||"";
  el("clarification-prompt").textContent=question.prompt;
  el("answer-options").replaceChildren();
  for(const option of question.options||[]) {
    const button=document.createElement("button");button.type="button";button.textContent=option;
    button.addEventListener("click",()=>{el("answer").value=option;el("answer").focus();});
    el("answer-options").append(button);
  }
  el("answer").value=pendingAnswer?pendingAnswer.answer:"";
  el("answer-fields").disabled=!!pendingAnswer;el("answer-submit").disabled=false;el("answer-refresh").disabled=false;
  el("answer-submit").textContent=pendingAnswer?"重试相同回答":"提交回答";
  el("answer-error").textContent=pendingAnswer?"上次回答尚未确认。重试沿用同一操作，不会重复执行。":"";
}
el("answer-form").addEventListener("submit",async event=>{
  event.preventDefault();
  if(!taskState?.clarification) return;
  const generation=++view;clearTimeout(timer);
  const id=taskState.id, question=taskState.clarification, storageKey="metricguard-answer:"+id;
  if(!pendingAnswer) pendingAnswer={request_id:crypto.randomUUID(),question_id:question.question_id,version:question.version,answer:el("answer").value};
  sessionStorage.setItem(storageKey,JSON.stringify(pendingAnswer));
  el("answer-fields").disabled=true;el("answer-submit").disabled=true;el("answer-refresh").disabled=true;el("new").disabled=true;el("answer-error").textContent="";
  try {
    await api("/api/tasks/"+id+"/answers",pendingAnswer);
    if(generation!==view) return;
    pendingAnswer=null;sessionStorage.removeItem(storageKey);el("new").disabled=false;
    await showTask(id,generation);
  } catch(error) {
    if(generation!==view) return;
    if(error.status && error.status<500) {pendingAnswer=null;sessionStorage.removeItem(storageKey);el("answer-fields").disabled=false;}
    el("answer-error").textContent=error.message;
    el("answer-submit").disabled=false;el("answer-refresh").disabled=false;el("new").disabled=false;
    el("answer-submit").textContent=pendingAnswer?"重试相同回答":"提交回答";
  }
});
el("answer-refresh").addEventListener("click",()=>{if(taskState) showTask(taskState.id);});
el("analysis-form").addEventListener("submit",async event=>{
  const generation=++view;clearTimeout(timer);
  event.preventDefault();el("error").textContent="";el("submit").disabled=true;el("new").disabled=true;
  try {
    if(!pending) pending={request_id:crypto.randomUUID(),question:el("question").value,snapshot_id:el("snapshot").value,window:windowValue("start","end"),comparison_window:windowValue("previous-start","previous-end")};
    sessionStorage.setItem("metricguard-pending",JSON.stringify(pending));el("fields").disabled=true;el("new").hidden=false;
    const value=await api("/api/tasks",pending);
    if(generation!==view) return;
    el("new").disabled=false;
    pending=null;sessionStorage.removeItem("metricguard-pending");
    history.pushState(null,"","/?task="+encodeURIComponent(value.id));
    await showTask(value.id,generation);
  } catch(error) {
    if(generation!==view) return;
    el("new").disabled=false;
    el("error").textContent=error.message;
    el("submit").disabled=false;el("submit").textContent=pending?"重试相同提交":"开始分析";
  }
});
el("new").addEventListener("click",()=>{
  view++;clearTimeout(timer);taskState=null;pendingAnswer=null;pending=null;sessionStorage.removeItem("metricguard-pending");history.pushState(null,"","/");
  el("task").hidden=true;el("empty").hidden=false;el("status").textContent="尚未开始";el("new").hidden=true;el("error").textContent="";unlock();
});
window.addEventListener("popstate",()=>location.reload());
(async()=>{
  try {
    const config=await (await fetch("/api/config")).json();token=config.token;
    for(const name of config.snapshots){const option=document.createElement("option");option.value=name;option.textContent=name;el("snapshot").append(option);}
    if(config.example){el("example").hidden=false;el("example").addEventListener("click",()=>fill(config.example));}
    unlock();refreshHistory();
    const id=new URLSearchParams(location.search).get("task");
    if(id){el("fields").disabled=true;el("submit").disabled=true;await showTask(id);return;}
    const saved=sessionStorage.getItem("metricguard-pending");
    if(saved){pending=JSON.parse(saved);fill(pending);el("fields").disabled=true;el("submit").textContent="重试相同提交";el("new").hidden=false;el("error").textContent="上次提交尚未确认。重试将沿用同一操作，不会重复执行。";}
  } catch(error){el("error").textContent="无法连接本机服务，请检查启动终端后刷新。";}
})();
