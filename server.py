import time
import socket
import sys

print("Welcome to chat 2.0")
print(" ")
print("Initialising .....")

s = socket.socket()

host = socket.gethostname()
port = 8080
s.bind((host, port))

print(" ")
print(host)
name = input(str("Please enter your username :"))
s.listen(1)
print(" ")

print("waiting for any incoming requests. ")

print(" ")


conn, addr = s.accept()


print("Recieved Connection")

#connection done
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "Was connected to the chat")

print("")
conn.send(name.encode())


#messaging_loop

while(1):
    message = input(str("please enter your message:"))
    print(" ")
    conn.send(message.encode())
    print("Sent")
    print(" ")
    message = conn.recv(1024)
    message = message.decode()
    print(name,":",message)
