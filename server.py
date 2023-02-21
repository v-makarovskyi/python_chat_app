import threading
import socket

class ChatServer:
    clients_list = []
    last_received_message = ''

    def __init__(self) -> None:
        self.server_socket = None
        self.create_listening_server()
    
    def create_listening_server(self):
        """Прослушать входящее соединение"""
        
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создать сокет, используя TCP и ipv4
        local_ip = '127.0.0.1'
        local_port = 10319
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)