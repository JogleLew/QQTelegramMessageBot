# -*- coding:utf-8 -*-
import gol
from random import randint
from qq_emoji_list import *
from special_sticker_list import *
from smart_qq_bot.messages import GroupMsg, PrivateMsg
from smart_qq_bot.signals import on_all_message, on_bot_inited
from smart_qq_bot.logger import logger


@on_bot_inited("PluginManager")
def manager_init(bot):
    gol.set_value('qqBot', bot);
    logger.info("Plugin Manager is available now:)")

@on_all_message(name="SamplePlugin")
def sample_plugin(msg, bot):
    """
    :type bot: smart_qq_bot.bot.QQBot
    :type msg: smart_qq_bot.messages.GroupMsg
    """
    tgBot = gol.get_value('tgBot')
    tgGroupId = gol.get_value('tgGroupId')
    msg_id = randint(1, 10000)
    
    # 发送一条群消息
    if isinstance(msg, GroupMsg):
        print msg
        gol.set_value('qqGroupId', msg.from_uin)

        # 获取并处理QQ消息
        textList = msg._content[1:]
        for i in range(len(textList)):
            textList[i] = str(textList[i])
        text = ''.join(textList).replace("[u'face', ", "[QQ表情")

        # 将常用的QQ表情转换到emoji
        for i in qqEmojiList:
            text = text.replace("[QQ表情" + str(i) + "]", qqEmojiList[i])

        # 判断!setgroupid指令
        if text == '!setgroupid':
            gol.set_value('qqGroupId', msg.from_uin)
            bot.send_group_msg("QQ连接已建立，chatId = " + str(msg.from_uin), msg.from_uin, msg_id)
        else:
            for j in specialStickerList: # 检测发送特定Telegram Sticker的指令
                if text == u'!' + j:
                    tgBot.sendSticker(tgGroupId, specialStickerList[j])
                    return
            tgBot.sendMessage(tgGroupId, msg.src_sender_name + ": " + text)  # 发送消息到telegram
    # 屏蔽私聊消息
    elif isinstance(msg, PrivateMsg):
        print msg
