import socket
name = input("Your name please : ")
age = int(input("Your age please"))

ip_local = socket.gethostbyname(socket.gethostname())

print("\n---Result---")
print("Hello", name)
print("You have", age,"years old")
print("Your IP adress is", ip_local)