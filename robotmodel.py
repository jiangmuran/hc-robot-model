import sys
import os
import websocket
import time


class hackchat:
  """
Author:jmr(@jiangmuran)

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
 recvreal:接收实际信息
 recv:只接收聊天信息
 _choosemsg:辨别信息

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
  获取当前最新一条分类信息
  返回一个列表:
  [0]:消息类型，0为正常，1为emote，2为私信，3为警告，4为提示，5为其他
  [1]:发送者，字符串，如果是警告则为!warn,提示为!info，其他为发送方(如果已知)
  [2]:消息内容，字符串，其他为具体内容（如果已知）




  



  """



  def __init__(self):
    self.wsaddress=''
    self.ws=websocket.WebSocket()
    self.channel=''
    self.nick=''
    self.passwd=''
    self.color=''
    self.onlinelist=[]
    self.ver='qwq1.3'
    self.reconn_time=30 # 出错后重试时间
    
  # 重新连接hc并加入
  def reconnect(self):
    try:
      self._connect(self.wsaddress)
      return self.join(self.channel,self.nick,self.passwd)
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  #出错后重试
  def restart_program(self):
    self.reconnect()

  #字符串转字典
  def _str2dict(self,string):
    false=False
    true=True
    null=None
    return eval(string)

  #链接到hc服务器
  def connect(self,wsaddress):
    try:
      self.wsaddress=wsaddress
      self.ws.connect(self.wsaddress)
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      python = sys.executable
      os.execl(python, python, * sys.argv)

  def _connect(self,wsaddress):
    try:
      self.wsaddress=wsaddress
      self.ws.connect(self.wsaddress)
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  # 加入频道
  def join(self,channel,nick,passwd):
    try:
      self.channel=channel
      self.nick=nick
      self.passwd=passwd
      self.onlinelist=[]
      # 发送加入信息
      self.ws.send(('{"cmd":"join","nick":"'+nick+'","pass":"'+passwd+'","channel":"'+channel+'"}'))
      print("connect!")
      # 解析内容
      rec=self._str2dict(self.ws.recv())

      

      # 如果类型为成功上线
      if rec['cmd'] == 'onlineSet':
        print('joined!')
        self.onlinelist=rec['nicks']
        return [rec['nicks'],rec['users']]


      # 如果类型为服务端发出错误
      elif rec['cmd'] == 'warn':
        print('server recv a error,reconnecting...')
        print(rec['text'])
        raise

      # 未知原因
      else:
        print('??? error!')
        print(rec)
        raise
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      python = sys.executable
      os.execl(python, python, * sys.argv)
      

  # 发送hc的断开链接请求
  def disconnect(self):
    try:
      self.onlinelist=[]
      self.ws.send('{"cmd":"disconnect","cmdKey":"what"}')
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  

  def getonlinelist(self):
    return self.onlinelist

  def send(self,text):
    try:
      self.ws.send('{"cmd":"chat","text":"'+text+'"}')
      pass
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  def sendme(self,text):
    try:
      self.sendcmd({'cmd':'emote','text':text})
      pass
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  def sendw(self,nick,text):
    try:
      self.sendcmd({'cmd':'whisper','nick':nick,'text':text})
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  def sendcmd(self,cmddict):
    try:
      self.ws.send(str(cmddict))
      pass
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  def changechannel(self,channel):
    try:
      self.channel=channel
      self.reconnect()
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  def changenick(self,nick):
    try:
      self.nick=nick
      sendcmd({"cmd":"changenick","nick":nick})
      pass
    except:
      print("error,restart in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("restarting.....")
      self.restart_program()

  def changecolor(self,color):
    try:
      self.color=color
      sendcmd({"cmd":"changecolor","color":color})
      pass
    except:
      print("error,restart in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("restarting.....")
      self.restart_program()

  def changepasswd(self,passwd):
    try:
      self.passwd=passwd
      reconnect()
    except:
      print("error,restart in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("restarting.....")
      self.restart_program()

  def _choosemsg(self,msgstr):
    try:
      msgdict=self._str2dict(msgstr)
      # 新用户
      if msgdict['cmd'] == 'onlineRemove':
        del self.onlinelist[self.onlinelist.index(msgdict['nick'])]
        return [5,'!userleft',msgdict['nick']]
      elif msgdict['cmd'] == 'onlineAdd':
        self.onlinelist.append(msgdict['nick'])
        return [5,'!useradd',msgdict['nick']]
      elif msgdict['cmd'] == 'chat':
        return [0,msgdict['nick'],msgdict['text']]
      elif msgdict['cmd'] == 'emote':
        return [1,msgdict['nick'],msgdict['text'][(2+len(msgdict['nick'])):]]
      elif msgdict['cmd'] == 'chat':
        return [0,msgdict['nick'],msgdict['text']]
      elif msgdict['cmd'] == 'info':
        if msgdict.__contains__('type'):
          if msgdict['type'] == 'whisper' :
            if msgdict['text'][0:3] != 'You':
              return [2,msgdict['text'].split(' ')[0],msgdict['text'][len(msgdict['text'].split(' ')[0])+12:]]
          else:
            return [5,'!echo',msgdict['text']]
        else:
          return [4,'!info',msgdict['text']]
      elif msgdict['cmd'] == 'warn':
        return [3,'!warn',msgdict['text']]
      else:
        return [5,'not found',msgstr]
    except:
      print("error,restart in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("restarting.....")
      self.restart_program()
    
  def recvreal(self):
    xyz=self.ws.recv()
    self._choosemsg(xyz)
    return self._str2dict(xyz)

  def recv(self):
    return self._choosemsg(self.ws.recv())

