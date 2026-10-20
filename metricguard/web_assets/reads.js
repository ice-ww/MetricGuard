"use strict";
// One bounded read/recovery owner per region. No writes or analysis belong here.
function readRegion({read, render, message, clear, label}) {
  let context=null, generation=0, controller=null, timer=null;
  let deadline=null, attempt=0, stopped=false, complete=false, pending=false;
  function cancel() {
    generation++;clearTimeout(timer);timer=null;
    controller?.abort();controller=null;
  }
  function expired() {
    if(stopped) return true;
    if(deadline!==null && Date.now()>=deadline) {
      stopped=true;
      message(label+"读取失败。已显示内容可能过期，未读到的内容暂不可用。自动重试已停止（已达两分钟上限），可手动刷新。");
    }
    return stopped;
  }
  async function refresh({manual=false, invalidate=false}={}) {
    if(context===null || (controller && !invalidate)) return;
    if(invalidate) cancel();
    if(manual) {deadline=null;attempt=0;stopped=false;}
    if(expired()) return;
    pending=true;
    if(document.hidden) return;
    clearTimeout(timer);timer=null;
    const version=++generation, active=new AbortController();
    controller=active;
    let timedOut=false;
    const timeout=setTimeout(()=>{
      timedOut=true;active.abort();
    },Math.min(10000,deadline===null?10000:Math.max(0,deadline-Date.now())));
    try {
      const value=await read(context,active.signal);
      if(version!==generation || active.signal.aborted) return;
      render(value);message(null);
      complete=true;pending=false;deadline=null;attempt=0;stopped=false;
    } catch(error) {
      if(version!==generation || (active.signal.aborted && !timedOut)) return;
      complete=false;deadline ??= Date.now()+120000;
      const definitive=[401,403,404].includes(error.status);
      stopped=definitive;
      message(label+"读取失败。已显示内容可能过期，未读到的内容暂不可用。"+
        (timedOut?"读取超过 10 秒。":definitive?error.message+" 已停止自动重试，可手动刷新。":"正在有限重试。"));
      if(!expired() && !document.hidden) {
        const delay=[1000,2000,4000,8000][attempt++] || 10000;
        timer=setTimeout(()=>{timer=null;if(!expired()) refresh();},
          Math.min(delay,deadline-Date.now()));
      }
    } finally {
      clearTimeout(timeout);
      if(controller===active) controller=null;
    }
  }
  return {
    select(next) {
      if(context===next) return;
      cancel();context=next;deadline=null;attempt=0;stopped=false;complete=false;pending=next!==null;
      clear();message(null);
    },
    ensure(next) {
      this.select(next);
      if(!complete && !controller && !timer && !stopped) refresh();
    },
    refresh,
    pause() {
      if(controller || timer) pending=true;
      cancel();
    },
    resume() {if(pending && !expired()) refresh();},
  };
}

function waitForRead(promise, signal) {
  if(signal.aborted) return Promise.reject(new DOMException("读取已取消","AbortError"));
  return new Promise((resolve,reject)=>{
    const abort=()=>reject(new DOMException("读取已取消","AbortError"));
    signal.addEventListener("abort",abort,{once:true});
    promise.then(resolve,reject).finally(()=>signal.removeEventListener("abort",abort));
  });
}
