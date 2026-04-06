# 与 `colleague-skill` 的方法对比

参考仓库：[`titanwings/colleague-skill`](https://github.com/titanwings/colleague-skill)

这份文档不复述它做了什么，而是只说明方法差异。

## `colleague-skill` 已经做得好的部分

从它的 prompts 和 tools 结构来看，`colleague-skill` 已经具备这些关键层：

- intake
- `persona` / `work` 双 analyzer
- `persona` / `work` 双 builder
- correction handler
- incremental merge
- version manager
- 面向聊天、邮件等材料的 collector / parser

这已经是一条完整的“人物 Skill 生产线”。

## 以录音和长对话为主的场景，还缺什么

如果你的核心材料是会议转写、长对话、指导性录音，那么还需要显式补四层。

### 1. Raw Material 和 Stable Assets 中间的 `history memory`

`colleague-skill` 更快地把原材料推向稳定文件。

但在 transcript-first 场景里，最好先有一层中间记忆：

- 每份会议或材料一份记忆文件
- 在完全压缩前保留证据
- 用案例级结构承载内容，而不是直接只剩最终结论

### 2. 置信度管理

录音和转写材料天然会有噪声：

- 说话人标签可能错
- ASR 可能错
- 上下文可能缺

因此更强的方法应该显式标注：

- 明确证据
- 推断证据
- 低置信度内容，暂不晋升稳定规则

### 3. 面向公开发布的强制脱敏层

`colleague-skill` 的目标更像“生成人物 Skill”。

如果目标是“公开方法而不公开人物”，还必须补一层：

- 脱敏规则
- 公私导出分离
- 只保留方法、不保留人物指纹的示例

### 4. 长周期压缩与稳定规则晋升机制

连续多场会议会产生很多重复模式。

更强的方法应该能压缩：

- 重复原则
- 重复提问方式
- 重复评审习惯

同时保留证据来源，而不是直接把所有东西扁平化。

## 应该复用什么

从 `colleague-skill` 值得直接复用的结构有：

- `persona` / `work` 双拆分
- analyzer / builder 分层
- correction 结构化处理
- merge 时的冲突提示
- version 归档与回滚

## 应该补什么

如果你要做“老板类人物”的长周期提炼，建议额外补上：

- transcript-aware 的 `history-memory` 模板
- 置信度标签
- 脱敏清单
- 公私导出分离
- 稳定规则晋升标准

## 最终推荐链路

推荐方法链路是：

`source intake -> evidence extraction -> history memory -> persona/work stable assets -> correction/versioning -> sanitized public export`

这就是这个仓库公开的方法论核心。
