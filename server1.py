from codecs import ignore_errors
from http.client import ImproperConnectionState
import socket
import das
 
# 实例化
sk = socket.socket()
# 定义连接的ip和port
ip_port = ('127.0.0.1',12345)
# 绑定端口
sk.bind(ip_port)
# 最大连接数
sk.listen(5)
#? 进入循环接收数据
conn, address = sk.accept()
print("文件接收开始")
while True:
    with open('encryptfile','ab') as f:
        # 接收数据
        data = conn.recv(1024)
        if data == b'quit':
            break
        # 写入文件
        f.write(data)
        # 接受完成标志
        conn.send('success'.encode())
print("文件接收完成")
#? 关闭连接
sk.close()

#?进行解密
print('开始进行解密///////')
with open ('./encryptfile','rb') as f:
  
  bytes=f.read()
  key=das.PadKey(das.key.encode())
  bytes=das.PadTest(bytes)
  decryptTest = das.DeCrypt(key, bytes)
  print(decryptTest.decode("utf-8"),'ignore')
  with open('./decryptfile','wb') as ff:
    ff.write(decryptTest)
