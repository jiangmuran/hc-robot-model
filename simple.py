import robotmodel as r
x=r.hackchat()
x.connect('wss://hack.chat/chat-ws')
x.join('your-channel','jmrobot','helloworld')
while True:
	print(x.recv())
	eval(input())

