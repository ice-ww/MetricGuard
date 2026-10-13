# 正式冻结材料

当前配置版本：`p0-independent-v3`。内容摘要 `d9dcf23bb2f4f069a30ccd0aa6c1b00673370503e630770eb6662956f7ae01a1`，代码基点 `5dce9c8`；运行前仍须验证全部文件摘要。v1、v2 永久保留，不能通过更换版本或注册库清除访问历史。

三个版本属于同一 `metricguard-p0-independent` family，使用同一批 24 个案例和原始快照字节。v2 根据父规格与开发样例补齐必需事实；v3 固定畸形用量防护后的代码配置。没有根据正式冻结诊断结果进行修复，也没有执行正式模型诊断或计分。

各目录中的 bundle 是评测侧私有答案，provenance 是生成参数及独立参考摘要，public-tasks 是给可信适配器的公共输入，freeze-record 保存版本、用途及截至冻结时的审计记录。正式运行不能将 bundle/provenance 交给模型或挂载到 SQL 容器。

本机原始快照位于 `artifacts/t18-frozen-v1`，持久注册库位于 `artifacts/evaluation-registry`，二者须一起保留、备份。Git 保存清单及审计归档，不包含这些运行数据库。后续 T20 应沿用现有注册库，通过公开 runner 记录访问；只读审查材料不代表已经完成正式验收。若用于定向修复，先登记 repair，并永久披露 regression 用途。

运行器契约及复现命令见 `experiments/t18/README.md`；本次交付与审查记录见 `docs/validation/t18-delivery.md`。
