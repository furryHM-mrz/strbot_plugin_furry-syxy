# AstrBot Furry 菜单插件

一个用于 AstrBot 的自定义文字菜单插件，可以显示帮助信息和指令列表。

## 功能介绍

该插件提供了一个自定义菜单功能，通过读取 `zp/cmd.txt` 文件的内容，以合并转发消息的形式展示给用户。主要特点包括：

- 自动创建 `zp` 文件夹（如果不存在）
- 读取 `zp/cmd.txt` 文件内容作为菜单展示
- 以合并转发消息形式发送，美观且不易刷屏
- 完善的错误处理机制

## 使用方法

### 安装插件

将本插件文件夹放入 AstrBot 的插件目录中，重启 AstrBot 即可自动加载。

### 触发指令

在聊天中发送以下任一指令即可触发菜单显示：

- `/help`
- `/菜单`

### 配置菜单内容

1. 确保插件目录下存在 `zp` 文件夹（插件会自动创建）
2. 在 `zp` 文件夹中创建 `cmd.txt` 文件
3. 在 `cmd.txt` 中编写您想要显示的菜单内容

例如，您可以这样编写 cmd.txt 的内容：
```
🌟 雪泷Bot 指令菜单 🌟

📌 基础指令:
/help - 显示帮助菜单
/about - 关于机器人

📌 娱乐功能:
/jrrp - 今日人品
/roll - 随机数

📌 实用工具:
/weather <城市> - 查询天气
/time - 当前时间
```

## 插件结构

```
strbot_plugin_furry-syxy/
├── main.py          # 插件主程序
├── metadata.yaml    # 插件元数据
├── README.md        # 说明文档
└── zp/              # 菜单文件夹
    └── cmd.txt      # 菜单内容文件
```

## 技术细节

- 插件名称: `strbot_plugin_furry-syxy`
- 指令名称: `help`
- 别名: `菜单`
- 版本: `1.0.0`
- 作者: `furryhm`

## 注意事项

1. 插件会自动创建 `zp` 文件夹，但需要确保有相应目录的写入权限
2. 如果 `cmd.txt` 文件不存在或为空，插件会给出相应提示
3. 建议在 `cmd.txt` 中使用清晰明了的格式，以提升用户体验

## 自定义

您可以修改 [main.py] 中的以下部分来自定义插件：

1. 指令名称和别名：
   ```python
   @filter.command("help", alias=['菜单'])
   ```

2. 合并转发消息的发送者名称：
   ```python
   node = Node(
       name="雪泷Bot指令菜单",  # 发送者外显名称
       content=[Plain(content)]  # 文字内容
   )
   ```

## 开源许可

本项目基于 LICENSE 文件中的条款进行许可。

基于插件[custom_menu](https://github.com/Futureppo/astrbot_plugin_custom_menu)改编的