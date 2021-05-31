import socket

s=socket.socket()

host=input("Please enter the host address of the sender: ")
port=1234
s.connect((host,port))
print("Connection Successful!")

files = s.recv(1024).decode()
print(files)

choice = input("\nYour choice: ")
s.send(choice.encode())

rfilename=input("\nEnter a name for the incoming file: ")
rfile=open(rfilename,'wb')
rdata=s.recv(1024)
rfile.write(rdata)
rfile.close()
print("File has been received successfully by the name:",rfilename)