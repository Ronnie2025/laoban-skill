<div align="center">

# 老板.skill

> *“先把问题讲清楚，再谈方案。原因都没分析清楚，怎么就开始拍板了？”*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skill Repo](https://img.shields.io/badge/Skill-Boss-blueviolet)](./SKILL.md)
[![Persona](https://img.shields.io/badge/Output-Persona-green)](./templates/persona.md)
[![Work](https://img.shields.io/badge/Output-Work-green)](./templates/work.md)

<br>

你的老板开会很猛，但离开会议室就只剩一堆零散纪要？<br>
你的负责人方法论很强，但没人能稳定复用他的判断方式？<br>
你的导师会审需求、会挑方案、会推闭环，但这些能力没有被沉淀成资产？<br>

**把零散的录音、纪要、聊天和文档，整理成一个真正能替老板“审需求、挑方案、推项目”的 AI Skill。**

<br>

提供老板的原始材料（录音转写、会议纪要、聊天记录、文档）和你的主观补充<br>
生成一个可持续更新的 **老板 Skill**<br>
让 AI 用他的方式追问问题、组织决策、压实 owner、推进闭环

[支持的数据来源](#支持的数据来源) · [安装](#安装) · [使用](#使用) · [生成结构](#生成结构) · [项目结构](#项目结构)

</div>

---

## 支持的数据来源

| 来源 | 适用 | 说明 |
|------|------|------|
| 录音转写 / 会议纪要 | ✅ 推荐 | 最适合提炼追问方式、决策逻辑、会议机制 |
| Markdown 文档 | ✅ | 适合提炼规范、方法、输出格式 |
| 聊天记录 / 群聊导出 | ✅ | 适合提炼口头禅、表达风格、关系行为 |
| 邮件 / 长文 | ✅ | 适合提炼正式表达、汇报方式、方案结构 |
| 直接粘贴文字 | ✅ | 适合补充主观描述和纠正 |

> 推荐优先级：**录音转写 > 长文档 > 决策类聊天 > 零散短消息**

---

## 安装

### Claude Code

```bash
# 当前项目
mkdir -p .claude/skills
git clone https://github.com/Ronnie2025/laoban-skill .claude/skills/create-boss

# 全局安装
git clone https://github.com/Ronnie2025/laoban-skill ~/.claude/skills/create-boss
```

### Codex / 本地 Skill 目录

```bash
git clone https://github.com/Ronnie2025/laoban-skill ~/.codex/skills/create-boss
```

---

## 使用

在支持 Skill 的代理环境里调用：

```text
/create-boss
```

然后按顺序提供：

1. 老板的角色定位
2. 你想提炼的重点场景
3. 原始材料
4. 你对他风格的主观补充

如果后面有新增会议、转写或纪要，再把新材料继续喂进去，它应该做增量更新，而不是从头重写。

---

## 生成结构

老板 Skill 推荐拆成三层：

| 部分 | 内容 |
|------|------|
| **Part A — History Memory** | 每份材料先写一层中间记忆，保留案例、原句和证据 |
| **Part B — Work Skill** | 需求判断、方案评审、会议机制、风险闭环、推进方式 |
| **Part C — Persona** | 口头禅、追问方式、表达节奏、对上对下对平级的行为模式 |

运行逻辑：

`接到问题 -> Persona 判断说法和态度 -> Work 决定怎么拆、怎么审、怎么推进 -> 用老板的风格输出`

---

## 功能特性

### 1. 先记忆，再稳定

不会拿原始材料直接去改最终 Prompt，而是先写一层 `history memory`，把高价值案例和方法点保留下来，再做压缩。

### 2. Persona / Work 双拆分

说话风格和工作方式分开沉淀，避免出现“口气像，但不会干活”或者“会干活，但不像他”。

### 3. 增量演化

- 新会议进来 -> 先补 history memory
- 再判断哪些内容应该进入稳定 `persona.md` / `work.md`
- 冲突显式提示，不悄悄覆盖

### 4. Correction 机制

当你说：

- “他不会这么说”
- “他这里会追问边界，不会直接给结论”
- “他遇到这种情况会先拉人开会，不会先自己拍板”

这些都应该进入 Correction 层，立即影响后续行为。

---

## 项目结构

本仓库参考 `colleague-skill` 的组织方式来写，但针对“老板型人物”的提炼做了调整：

```text
laoban-skill/
├── SKILL.md
├── prompts/
│   ├── intake.md
│   ├── history_memory_builder.md
│   ├── work_builder.md
│   ├── persona_builder.md
│   ├── master_prompt_builder.md
│   ├── merger.md
│   └── correction_handler.md
├── tools/
│   ├── skill_writer.py
│   └── version_manager.py
├── bosses/
│   └── README.md
├── docs/
│   ├── comparison-with-colleague-skill.md
│   ├── pipeline.md
│   └── sanitization.md
├── templates/
│   ├── correction.md
│   ├── history-memory.md
│   ├── master-prompt.md
│   ├── persona.md
│   └── work.md
└── LICENSE
```

---

## 注意事项

- 原材料质量决定 Skill 质量
- 会议转写越完整，越容易提炼出稳定追问模式
- 不要只喂总结，尽量保留原始表达
- 适合长期迭代，不适合只做一次性角色扮演 Prompt

> 本仓库不附带真实老板样本数据，只提供通用结构、Prompt 和模板。
