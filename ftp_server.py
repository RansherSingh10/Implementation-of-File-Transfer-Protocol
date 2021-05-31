import socket

s=socket.socket()

host= '127.0.0.1'
port = 1234

s.bind((host,port))
s.listen(2)

print('Waiting for the connection...')

conn,addr=s.accept()
print(addr,"Has connected to the server")

message = ('The following are the files present on the server, mention the one you want to recieve: \n1. Text.txt\n2. help.txt\n3. transfer.txt')
conn.send(message.encode())

choice = conn.recv(1024).decode()


filename = choice
file=open(filename,'rb')
data=file.read(1024)
conn.send(data)
print("Data has been transmitted successfully!")