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
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #это позволяет немедленно перезапустить TCP-сервер
        self.server_socket.bind(local_ip, local_port) #это привязывает сервер к IP и порту с целью прослушивания входящих соединений
        print('Прослушивание входящих соединений...')
        self.server_socket.listen(5)
