import sys
import os
import websocket
import time

def restart_program():
  """Restarts the current program.
  Note: this function does not return. Any cleanup action (like
  saving data) must be done before calling this function."""
  python = sys.executable
  os.execl(python, python, * sys.argv)

class hackchat:
  """restart_program:重启整个程序
     connect:连接到ws服务器
     join:加入到特定频道
     disconnect:断开连接
     reconnect:重新连接并加入
     getonlinelist:获取在线昵称列表
     send:发送信息
     sendme:发送me信息
     sendw:发送私信
     sendcmd:发送命令
     changechannel:切换频道
    x changenick:切换昵称
    x changepasswd:切换密码
    x recv:接收信息
    x _choosemsg:辨别信息





  """

  """
模板：
def model(self):
    try:
      #text in there
      pass
    except:
      print("error,restart in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("restarting.....")
      self.restart_program()


  """

  def __init__(self):
    self.wsaddress=''
    self.ws=websocket.WebSocket()
    self.channel=''
    self.nick=''
    self.passwd=''
    self.onlinelist=[]
    self.ver='qwq0.9'
    self.reconn_time=30 # 出错后重试时间
    
  # 重新连接hc并加入
  def reconnect(self):
    try:
      self.disconnect()
      self.connect(self.wsaddress)
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

      self.onlinelist=rec['nicks']

      # 如果类型为成功上线
      if rec['cmd'] == 'onlineSet':
        print('joined!')
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
      self.restart_program()

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
      self.ws.send('{"cmd":"chat","text":"/me '+text+'"}')
      pass
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()

  def sendw(self,nick,text):
    try:
      self.ws.send('{"cmd":"chat","text":"/w '+nick+' '+text+'"}')
      pass
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
      self.ws.channel=change
      self.reconnect()
    except:
      print("error,reconnect in "+str(self.reconn_time)+"s")
      time.sleep(self.reconn_time)
      print("reconnecting.....")
      self.restart_program()




  

if __name__ == "__main__":
  print('start')
  try:
    x = hackchat()
    x.connect('wss://hack.chat/chat-ws')
    x.join('your-channel','jmrobot','')
    x.sendme('helloworld!')
    input()
    x.changechannel('lounge')
    input()
    
  except:
    print("error,restart in "+str(self.reconn_time)+"s")
    time.sleep(self.reconn_time)
    print("restarting.....")
    restart_program()