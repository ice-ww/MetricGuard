"use strict";
// Drafts are tab-local and separate from immutable, unconfirmed write operations.
const drafts = (() => {
  const composeKey="metricguard-draft:new", answerPrefix="metricguard-draft:answers:";
  function read(key, fallback) {
    try {return JSON.parse(sessionStorage.getItem(key)) ?? fallback;}
    catch {return fallback;}
  }
  function write(key, value) {
    try {
      if(value===null) sessionStorage.removeItem(key);
      else sessionStorage.setItem(key,JSON.stringify(value));
    } catch {
      document.getElementById("draft-notice").textContent="无法保存标签页草稿，请在刷新前复制输入内容。";
    }
  }
  const matches=(draft,question)=>question && draft.question_id===question.question_id && draft.version===question.version;
  function answers(task) {
    const saved=read(answerPrefix+task,[]);
    return Array.isArray(saved)?saved.filter(d=>d && typeof d.question_id==="string" && Number.isInteger(d.version) && typeof d.answer==="string"):[];
  }
  return {
    compose:()=>read(composeKey,null),
    saveCompose:value=>write(composeKey,value),
    clearCompose:()=>write(composeKey,null),
    matches, answers,
    answer:(task,question)=>answers(task).find(d=>matches(d,question)),
    saveAnswer(task,question,answer) {
      const saved=answers(task).filter(d=>!matches(d,question));
      if(answer) saved.push({question_id:question.question_id,version:question.version,prompt:question.prompt,answer});
      write(answerPrefix+task,saved);
    },
    clearAnswer(task,question) {write(answerPrefix+task,answers(task).filter(d=>!matches(d,question)));}
  };
})();
