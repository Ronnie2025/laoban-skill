# 老板 Skill

这是一个公开的“老板类人物 Skill 提炼方法论”仓库。

它公开的是方法，不公开任何真实老板、同事、公司、客户、产品、路径或内部语料。

这套方法论用于把原始人物材料整理成可复用的 AI Skill，同时把“私有画像”和“公开方法”彻底分开。

## 这套方法解决什么问题

很多“模仿某个人”的 Prompt 或 Skill，会在两个方向上出问题：

1. 写得像，但没有证据基础，容易漂移。
2. 有证据基础，但把真实人物信息一起公开了。

这套方法的目标就是同时避免这两个问题。

## 核心原则

1. 证据优先
   稳定结论必须能回溯到原始材料，或者明确标注为推断。
2. Persona 和 Work 分开
   人的表达习惯、关系行为，不能和工作方法、决策流程混写。
3. 中间必须有历史记忆层
   不要每次从原始材料直接改最终 Prompt，要先沉淀到中间记忆层。
4. 先保留案例，再提炼稳定模式
   案例和原句用于保真，稳定规则用于复用，二者不能混成一团。
5. Correction 是正式输入，不是附言
   用户纠正不是评论，而是模型塑形数据。
6. 默认脱敏
   公开导出时，必须删除名字、组织、产品、路径、内部缩写和敏感数字。
7. 私有资产和公开仓库是两种产品
   私有层可以有人物画像；公开层只能有方法、模板和脱敏规则。

## 总体流程

推荐流程分六层：

1. Intake
   接收原始材料并分类。
2. Evidence Extraction
   抽取可证明的人物行为、表达习惯和工作模式。
3. History Memory
   先写一层中间记忆，保留证据，再做压缩。
4. Stable Assets
   把重复出现的稳定模式合并进 `persona.md`、`work.md`，必要时再生成 `master-prompt.md`。
5. Correction & Versioning
   处理纠正、冲突、版本归档和回滚。
6. Public Export
   最后只公开方法、模板和脱敏后的示例。

详细说明见：

- [流程设计](docs/pipeline.md)
- [脱敏规则](docs/sanitization.md)
- [与 `colleague-skill` 的方法对比](docs/comparison-with-colleague-skill.md)

## 这套方法保留了什么

参考公开仓库 [`titanwings/colleague-skill`](https://github.com/titanwings/colleague-skill)，这套方法保留了其中最重要的几个结构优点：

- `persona` / `work` 双拆分
- analyzer / builder 分层
- correction 结构化处理
- merge 冲突提示
- version 管理与回滚

## 这套方法补了什么

如果你的原始材料以录音转写、会议纪要、长对话为主，那么还需要补四层：

- transcript-first 的 `history memory`
- 置信度管理
- 强制脱敏与公开导出边界
- 长周期压缩与稳定规则晋升机制

## 仓库结构

```text
.
├── README.md
├── docs/
│   ├── comparison-with-colleague-skill.md
│   ├── pipeline.md
│   └── sanitization.md
└── templates/
    ├── correction.md
    ├── history-memory.md
    ├── master-prompt.md
    ├── persona.md
    └── work.md
```

## 适用场景

适合用于：

- 从录音、聊天、邮件、文档中提炼老板/同事/创始人/专家型人物 Skill
- 长期维护一个私有人物语料库，但只公开方法论
- 持续吸收新增会议或对话材料
- 把“像某个人”做成可维护的资产，而不是一次性 Prompt

## 不适用场景

不适合用于：

- 只想临时写一个角色扮演 Prompt
- 没有原始材料，只有模糊印象
- 打算直接公开真实人物画像

## 使用起点

如果你想从零开始：

1. 先用 [templates/history-memory.md](templates/history-memory.md) 承接每一份原始材料。
2. 再把重复出现的稳定模式提升到 [templates/persona.md](templates/persona.md) 和 [templates/work.md](templates/work.md)。
3. 用户纠正统一走 [templates/correction.md](templates/correction.md)。
4. 对外发布前，必须过一遍 [脱敏规则](docs/sanitization.md)。
