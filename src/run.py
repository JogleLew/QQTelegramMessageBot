#coding: utf-8
import os
import sys
import telepot
from smart_qq_plugins import gol
from random import randint
from pprint import pprint

here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)

from smart_qq_bot.logger import logger
from smart_qq_bot.main import run

gol._init() # 初始化全局变量表

tgBot = telepot.Bot('请在这里填写token') # 启动Telegram机器人
gol.set_value('tgBot', tgBot)

# 如果你知道QQ群和Telegram群的ID，可以直接在程序启动时设置
# gol.set_value('tgGroupId', -123456789)
# gol.set_value('qqGroupId', 987654321)

def handle(msg):
    pprint(msg)
    chatId = msg[u'chat'][u'id']
    chatType = msg[u'chat'][u'type']
    if chatType != u'group': # 屏蔽掉所有不来自Telegram群组的消息
        return
    sender = msg[u'from'][u'username']
    text = u''
    if msg.has_key(u'text'): # 文本消息
        text = msg[u'text']
    elif msg.has_key(u'photo'): # 图片消息，显示占位符
        text = u'[图片]'
    elif msg.has_key(u'video'): # 视频消息，显示占位符
        text = u'[视频]'
    elif msg.has_key(u'audio'): # 音频消息，显示占位符
        text = u'[音频]'
    elif msg.has_key(u'document'): # 文件消息，显示占位符
        text = u'[文件]'
    elif msg.has_key(u'sticker'): # 贴图消息，显示对应emoji
        text = msg[u'sticker'][u'emoji']
    if text == u'!setgroupid': # 检测!setgroupid指令
        gol.set_value('tgGroupId', chatId);
        tgBot.sendMessage(chatId, 'Telegram连接已建立，chatId = ' + str(chatId));
    else:
        qqBot = gol.get_value('qqBot')
        qqGroupId = gol.get_value('qqGroupId')
        msg_id = randint(1, 10000)
        forwardFrom = u''
        if msg.has_key(u'forward_from'): # 添加转发消息标注
            forwardFrom = u' (forwarded from ' + msg[u'forward_from'][u'username'] + u') '
        replyTo = u''
        if msg.has_key(u'reply_to_message'): # 添加回复消息标注
            replyTo =  u' (reply to ' + msg[u'reply_to_message'][u'from'][u'username'] + u') '
        qqBot.send_group_msg(sender + replyTo + forwardFrom + ': ' + text, qqGroupId, msg_id); # 向QQ发送消息

tgBot.message_loop(handle);
run() # 启动QQ机器人
