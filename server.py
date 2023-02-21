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
        self.server_socket.listen(4) #прослушивание входящих соединений. В данном случае - не более 4-х.
        self.receive_messages_in_a_new_thread()
    
    #получить данные (сообщение) из сокета
    def receive_messages(self, sock):
        while True:
            incoming_buffer = sock.recv(256) #инициализация буффера. Получить данные из сокета и сохранить их в буфере.
            if not incoming_buffer:
                break
            self.last_received_message = incoming_buffer.decode('utf-8')
            self.broadcast_to_all_clients(sock) #отправить всем клиентам
        sock.close()
    
    #Трансляция сообщений всем клиентам 
    def broadcast_to_all_clients(self, senders_socket):
        for client in self.clients_list:
            socket, (ip, port) = client
            if socket is not senders_socket:
                socket.sendall(self.last_received_message.encode('utf-8'))
    
    #получение сообщений в новом потоке выполнения
    def receive_messages_in_a_new_thread(self):
        while True:
            client = sock, (ip, port) = self.server_socket.accept()
            self.add_to_clients_list(client)
            print('Соединено по адресу: ', ip,  ':', str(port))
            t = threading.Thread(target=self.receive_messages, args=(sock,))
            t.start()







