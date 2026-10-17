"use strict";
const el = id => document.getElementById(id);
let token, pending = null, timer, view = 0;
const names = {created:"准备执行",running:"正在分析",waiting:"等待澄清",ended:"已结束",failed:"执行失败",interrupted:"已中断"};
async function api(path, data) {
  const response = await fetch(path, {method:data?"POST":"GET", headers:{"X-MetricGuard-Token":token,"Content-Type":"application/json"},body:data?JSON.stringify(data):undefined});
  const value=await response.json();
  if(!response.ok) throw new Error(value.error || "请求未完成，请重新打开任务。");
  return value;
}
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
    el("pending").textContent=state.pending?state.pending+" 本版暂不支持网页回答；任务已保留。":"";
    el("result").textContent=state.body;
    if(["created","running"].includes(state.status)) timer=setTimeout(()=>showTask(id,generation),1000);
  } catch(error) {
    if(generation!==view) return;
    el("connection").textContent="暂时无法读取任务。请确认本机服务仍在运行后刷新；不会自动重新执行。";
  }
}
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
  view++;clearTimeout(timer);pending=null;sessionStorage.removeItem("metricguard-pending");history.pushState(null,"","/");
  el("task").hidden=true;el("empty").hidden=false;el("status").textContent="尚未开始";el("new").hidden=true;el("error").textContent="";unlock();
});
window.addEventListener("popstate",()=>location.reload());
(async()=>{
  try {
    const config=await (await fetch("/api/config")).json();token=config.token;
    for(const name of config.snapshots){const option=document.createElement("option");option.value=name;option.textContent=name;el("snapshot").append(option);}
    if(config.example){el("example").hidden=false;el("example").addEventListener("click",()=>fill(config.example));}
    unlock();
    const id=new URLSearchParams(location.search).get("task");
    if(id){el("fields").disabled=true;el("submit").disabled=true;await showTask(id);return;}
    const saved=sessionStorage.getItem("metricguard-pending");
    if(saved){pending=JSON.parse(saved);fill(pending);el("fields").disabled=true;el("submit").textContent="重试相同提交";el("new").hidden=false;el("error").textContent="上次提交尚未确认。重试将沿用同一操作，不会重复执行。";}
  } catch(error){el("error").textContent="无法连接本机服务，请检查启动终端后刷新。";}
})();
