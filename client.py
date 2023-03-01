from tkinter import Tk, Frame, Scrollbar, Label, END, Entry, Text, VERTICAL, Button, messagebox
import socket
import threading

class GUI:
    client_socket = None
    last_received_message = None

    def __init__(self, master):
        self.root = master
        self.chat_transcript_area = None
        self.name_widget = None
        self.enter_text_widget = None
        self.join_button = None
        self.initialize_socket()
        self.initialize_gui()
        self.listen_incoming_messages_in_a_thread()

    def initialize_socket(self):
        """ инициализация и подключение сокета с TCP и IPv4 к удаленному серверу """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        remote_ip = '127.0.0.1'
        remote_port = 10319
        self.client_socket.connect((remote_ip, remote_port)) #подключение к удаленному серверу


    def initialize_gui(self): 
        """ инициализация графического интерфейса пользователя """
        self.root.title('Python-Socket-Chat-App')
        self.root.resizable(0,0)
        self.display_chat_box()
        self.display_name_section()
        self.display_chat_entry_box()
        
