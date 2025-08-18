from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from astrbot.api.message_components import *
from astrbot.api.event import filter, AstrMessageEvent
import os
import re
import aiohttp
import json
from typing import List

@register("strbot_plugin_furry-syxy", "furryhm", "自定义文字消息！！！", "1.0.0")
class custommenu(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    @filter.command("help", alias=['菜单'])  # 可以自行添加指令
    async def custommenu(self, event: AstrMessageEvent):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # 菜单文件夹路径
        menu_dir = os.path.join(base_dir, "zp")
        cmd_file_path = os.path.join(menu_dir, "cmd.txt")

        # 检查并创建菜单文件夹
        if not os.path.exists(menu_dir) or not os.path.isdir(menu_dir):
            logger.info(f"zp文件夹不存在或不是一个有效的目录，尝试创建: {menu_dir}")
            try:
                os.makedirs(menu_dir, exist_ok=True)  # 自动创建目录
                logger.info(f"zp文件夹已成功创建: {menu_dir}")
            except Exception as e:
                logger.error(f"无法创建zp文件夹: {menu_dir}, 错误信息: {e}")
                yield event.plain_result("系统错误：无法创建zp文件夹")
                return

        # 检查cmd.txt文件是否存在
        if not os.path.exists(cmd_file_path):
            logger.warning(f"cmd.txt文件不存在: {cmd_file_path}")
            yield event.plain_result("未找到指令列表文件")
            return

        try:
            # 读取cmd.txt文件内容
            with open(cmd_file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                logger.warning(f"cmd.txt文件为空: {cmd_file_path}")
                yield event.plain_result("指令列表文件为空")
                return
            
            # 创建合并转发消息节点
            node = Node(
                name="雪泷Bot指令菜单",  # 发送者外显名称
                content=[Plain(content)]  # 文字内容
            )

            # 创建Nodes对象
            nodes = Nodes(nodes=[node])

            # 发送合并转发消息
            yield event.chain_result([nodes])
            
        except Exception as e:
            logger.error(f"读取cmd.txt文件时发生错误: {e}")
            yield event.plain_result("读取指令列表文件时发生错误")