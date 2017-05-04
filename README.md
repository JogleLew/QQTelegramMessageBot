QQTelegramMessageBot
=========

本bot是基于[Yinzo/SmartQQBot](https://github.com/Yinzo/SmartQQBot)和[nickoala/telepot](https://github.com/nickoala/telepot)的二次开发。

## 功能和特性
+ 支持QQ群和Telegram群的文字消息互转
+ Telegram群的Sticker会转换成对应的emoji发送给QQ群
+ QQ群可以通过指令向Telegram群发送Sticker
+ [Yinzo/SmartQQBot](https://github.com/Yinzo/SmartQQBot)中可用的插件在本bot中依然可用

## 使用方法
1. 按照[nickoala/telepot](https://github.com/nickoala/telepot)的介绍，安装和测试Telepot
1. 按照[Yinzo/SmartQQBot](https://github.com/Yinzo/SmartQQBot)的介绍，安装相关依赖
1. 在Telegram中向@BotFather申请一个bot，记住你的token，并加入一个群组
1. 注册一个QQ小号，作为QQ机器人，加入一个QQ群
1. src/run.py中填入Telegram Bot Token，并使用python run.py运行，如果没有图形界面，需要加入参数--no-gui。扫描当前目录下的二维码v.jpg，登录QQ小号。
1. 在Telegram群组里发送一条消息!setgroupid，即可看到当前Telegram群组的group ID。
1. 在QQ群里发送一条消息!setgroupid，即可看到当前QQ群的group ID，这个ID是会变的。
1. 在两个群都发送!setgroupid之后，bot即可进行群消息的转发
1. 可以在run.py中指定QQ群和Telegram群组的group ID，程序会在开始运行时自动设置。

## 已知问题
+ 由于WebQQ协议的限制, 不能直接发送图片，一段时间后机器人会被强制下线，此时需要重新扫码登录一次。
+ 机器人只能处理一个QQ群和一个Telegram群组的消息转发，请不要将机器人加入多个QQ群或多个Telegram群组，否则消息转发会混乱。
+ 由于QQ群的group ID会随机变化，QQ群内需要偶尔有人发送消息，机器人会根据消息更新QQ群的group ID。
