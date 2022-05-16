import das
import socket
import struct

 
# 实例化
sk = socket.socket()
# 定义连接的ip和port
ip_port = ('127.0.0.1',12345)
# 服务器连接
sk.connect(ip_port)
# 文件上传
# 打开文件
with open('./file.txt','rb') as f:
    #? 文件加密
    bytes=f.read()
    print('源文件长度:{}'.format(len(bytes)))
    key=das.PadKey(das.key.encode())
    bytes=das.PadTest(bytes)
    print('补齐后长度为{}'.format(len(bytes)))
    encryptTest = das.EnCrypt(key, bytes)
    print(encryptTest)
  
    #? 按每一段分割文件上传
    for i in encryptTest:
        sk.send(struct.pack("B",i))
        # 等待接收完成标志
        data=sk.recv(1024)
        # 判断是否真正接收完成
        if data != b'success':
            break

#? 给服务端发送结束信号
sk.send('quit'.encode())