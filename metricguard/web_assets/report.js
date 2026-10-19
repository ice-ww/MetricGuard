"use strict";
// Only text nodes and locally generated anchors: report data is never HTML.
function renderReport(report, root) {
  root.replaceChildren();
  function node(tag,text,parent=root) {
    const element=document.createElement(tag);if(text!==undefined) element.textContent=text;
    parent.append(element);return element;
  }
  function fold(title,id,parent=root) {
    const detail=node("details",undefined,parent);if(id) detail.id=id;
    node("summary",title,detail);return detail;
  }
  function jumpLink(label,target,parent) {
    const link=node("a",label,parent);link.href="#"+encodeURIComponent(target.id);
    link.addEventListener("click",event=>{
      event.preventDefault();
      for(let ancestor=target.parentElement;ancestor;ancestor=ancestor.parentElement) {
        if(ancestor.tagName==="DETAILS") ancestor.open=true;
      }
      target.focus();target.scrollIntoView({block:"center"});
    });
  }
  if(!report.available) {node("p",report.message);return;}
  const kinds={facts_available:"查询事实",supported_descriptive_candidate:"描述性候选，未证明因果",no_supported_anomaly:"未形成支持充分的异常候选",insufficient_evidence:"证据不足，暂无法判断",budget_exhausted:"预算限制，分析未完成",refused:"请求已拒绝",unsupported:"当前不支持此问题"};
  node("p",kinds[report.analysis_result]||report.analysis_result).id="report-kind";
  const scopes=node("div");scopes.className="report-scope";
  for(const [key,label] of [["original_window","原始请求"],["requested_window","确认请求"],["actual_window","实际分析"],["comparison_window","比较基期"]]) {
    const value=report.scope[key];
    if(value) node("p",label+"："+value.join(" 至 ")+"（结束日不包含）",scopes);
  }
  const overview=node("div");overview.id="report-overview";
  const facts=fold("完整事实表","facts-details");
  node("p","展示值可取整；原始数值及口径见对应证据单元格。",facts);
  const evidence=fold("原始证据与查询参数","evidence-details");
  const cells=new Map();
  for(const [index,item] of report.evidence.entries()) {
    const detail=fold(item.evidence_id,null,evidence);
    node("pre",item.metadata_text,detail);
    const wrap=node("div",undefined,detail);wrap.className="table-scroll";
    const table=node("table",undefined,wrap),head=node("tr",undefined,node("thead",undefined,table));
    const columns=Object.keys(item.columns);
    node("th","行号（从0起）",head);for(const column of columns) node("th",column,head);
    const tbody=node("tbody",undefined,table);
    item.rows.forEach((row,rowIndex)=>{
      const tr=node("tr",undefined,tbody);node("th",String(rowIndex),tr);
      columns.forEach((column,columnIndex)=>{
        const cell=node("td",item.row_text[rowIndex][column],tr);
        cell.id=`evidence-${index}-${rowIndex}-${columnIndex}`;cell.tabIndex=-1;cell.className="evidence-cell";
        cell.dataset.row=String(rowIndex);cell.dataset.column=column;
        cells.set(JSON.stringify([item.evidence_id,rowIndex,column]),cell);
      });
    });
  }
  const targets=new Map();
  for(const fact of report.facts) {
    const row=node("div",undefined,facts);row.id="fact-"+fact.assertion_id;row.tabIndex=-1;row.className="fact-row";
    node("p","A"+fact.assertion_id+" · "+fact.text,row);
    const ref=fact.reference,cell=cells.get(JSON.stringify([ref.evidence_id,ref.row,ref.column]));
    const label=ref.evidence_id+" / rows / "+ref.row+" / "+ref.column;
    if(cell) jumpLink(label,cell,row);else node("p","证据位置不可用："+label,row);
    targets.set(fact.assertion_id,row);
  }
  function textWithRefs(text,parent) {
    const pattern=/\[A([^\]]+)\]\(#fact-([^\)]+)\)/g;let offset=0;
    for(const match of text.matchAll(pattern)) {
      parent.append(document.createTextNode(text.slice(offset,match.index)));
      const target=match[1]===match[2]?targets.get(match[1]):null;
      if(target) jumpLink("A"+match[1],target,parent);else parent.append(document.createTextNode(match[0]));
      offset=match.index+match[0].length;
    }
    parent.append(document.createTextNode(text.slice(offset)));
  }
  let parent=overview;
  for(const line of report.body.split("\n")) {
    if(!line.trim()) continue;
    if(["支持依据：","反对证据与对照："].includes(line)) {parent=fold(line.slice(0,-1),null,overview);continue;}
    if(line==="未排除因素：") {parent=overview;node("h4",line,parent);continue;}
    const heading=line.match(/^(#{1,2}) (.*)$/);
    if(heading) {parent=overview;node(heading[1].length===1?"h3":"h4",heading[2],parent);continue;}
    textWithRefs(line.replace(/^- /,""),node("p",undefined,parent));
  }
  const inferenceDetails=fold("完整推断与支持/反对引用","inferences-details");
  for(const inference of report.inferences) {
    node("p",inference.text,inferenceDetails);
    for(const [key,label] of [["supporting_assertion_ids","支持依据"],["opposing_assertion_ids","反对证据与对照"]]) {
      const p=node("p",label+"：",inferenceDetails);
      for(const id of inference[key]) {if(targets.has(id)) jumpLink("A"+id,targets.get(id),p);p.append(document.createTextNode(" "));}
    }
    for(const factor of inference.unexcluded_factors) node("p","未排除因素："+factor,inferenceDetails);
  }
  const trace=fold("执行记录","trace-details");
  node("pre",report.trace_text,trace);
}
