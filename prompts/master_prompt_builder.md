# Master Prompt 生成 Prompt

## 任务

在 `persona.md` 和 `work.md` 已经稳定后，把它们压缩成一个可直接调用的 `master-prompt.md`。

## 目标

这份文件不是重新发明一套规则，而是把稳定层压缩成更容易执行的统一入口。

## 必须包含

- 角色定义
- 优先级顺序
- 输出骨架
- 缺信息时的处理方式

## 输出格式

直接按 [templates/master-prompt.md](../templates/master-prompt.md) 的结构输出。

## 注意事项

- 不要把细节全部塞进去
- 优先保留稳定规则、工作流程和输出骨架
- 不要跳过 `persona.md` / `work.md` 直接从原始材料生成
