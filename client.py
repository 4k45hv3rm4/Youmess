import time
import socket

import sys

print("Welcome to python chat v2.0")
print(" ")
print("Initialising....")
time.sleep(1)

s=  socket.socket()

print(" ")

host = input(str("Please enter the server addresss"))
name = input(str("Please enter your name : "))
port = 8080
print("trying to connect to ", host , " at port ", port)
time.sleep(1)
s.connect((host, port))
print("Connected")

#connection done

s.send(name.encode())
s_name = s.recv(1024)
s_name =  s_name.decode()
print(" ")
print(s_name ,"Has joined the network")

#messaging_loop

while 1:
    message = s.recv(1024)
    message = message.decode()
    print(" ")
    print(name,":",message)
    message = input(str("please enter your message:"))
    print(" ")
    s.send(message.encode())
    print("Sent")
