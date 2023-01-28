# hc机器人模板
Ver:qwq0.99
Author:jmr(@jiangmuran)
本程序遵守MIT开源协议

MIT License

Copyright (c) 2023 jiangmuran

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


 restart_program:重新连接
 connect:连接到ws服务器
 join:加入到特定频道
 disconnect:断开连接
 reconnect:重新连接并加入

 send:发送信息
 sendme:发送me信息
 sendw:发送私信
 sendcmd:发送命令

 changechannel:切换频道
 changenick:切换昵称
 changepasswd:切换密码
 changecolor:切换颜色

 getonlinelist:获取在线昵称列表
x recvreal:接收实际信息
x recv:只接收聊天信息
x _choosemsg:辨别信息

restart_program():
  程序内部重连，相当于reconnect()

connect(wsaddress):
  连接到指定hc服务器
  如果连接不成功将尝试重复连接，可修改全局变量reconn_time

join(channel,nick,passwd):
  发送加入请求
  正常返回为列表，[0]为在线昵称列表，[1]为用户详细信息列表
  如果加入不成功将尝试重复连接，可修改全局变量reconn_time

dissconnect():
  断开与hc连接

reconnect():
  重新连接hc并加入特定频道（请务必在之前处于连接状态！）


send(text):
  发送普通消息（要求加入）

sendme(text):
  发送emote消息（要求加入）

sendw(nick,text):
  发送指定私聊消息

sendcmd(cmd):
  发送原始cmd消息（为字典）

changechannel(channel):
  切换频道（注意频率限制）

changenick(nick):
  切换昵称（限制少）

changepasswd(passwd):
  切换昵称（限制少）

changecolor():
  切换颜色（限制少）


getonlinelist():
  返回当前的在线用户列表
  请注意，本功能需要recv()函数作为支撑

recvreal():
  获取当前的原始数据（字典）
  如果遇到onlineuser修改会自动补充

recv():
  获取当前最新一条的文字信息
  返回一个列表:
  [0]:消息类型，0为正常，1为emote，2为私信
  [1]:发送者，字符串
  [2]:消息内容，字符串
