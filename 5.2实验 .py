import socket
#服务器端的socket初始化
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8001))#绑定.localhost = 127.0.0.1port=0-65535
s.listen()#监听
conn,address = s.accept()#阻塞
data = conn.recv(1024)#接收
print(data.decode())
conn.sendall(("服务器已经接收到了数据内容：你好世界"+str(data.decode())).encode())
s.close()