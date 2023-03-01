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
        # подключение к удаленному серверу
        self.client_socket.connect((remote_ip, remote_port))

    def initialize_gui(self):
        """ инициализация графического интерфейса пользователя. Прослушивание входящих сообщений в потоке """
        self.root.title('Python-Socket-Chat-App')
        self.root.resizable(0, 0)
        self.display_chat_box()
        self.display_name_section()
        self.display_chat_entry_box()

    def listen_for_incoming_messages_in_a_thread(self):
        """ Создание потока для одновременной отправки и получения сообщений """
        thread = threading.Thread(
            target=self.receive_message_from_server, args=(self.client_socket,))
        thread.start()

    def receive_message_from_server(self, so):
        """ функция для получения сообщений """
        while True:
            buffer = so.recv(256)
            if not buffer:
                break
            message = buffer.decode('utf-8')

            if 'joined' in message:
                user = message.split(":")[1]
                message = user + ' успешно присоединился'
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)
            else:
                self.chat_transcript_area.insert('end', message + '\n')
                self.chat_transcript_area.yview(END)
        
        so.close()
    
    def display_name_section(self):
        frame = Frame()
        Label(frame, text='Введите ваше имя:', font=('Helvetica', 16)).pack(side='left', padx=10)
        self.name_widget = Entry(frame, width=50, borderwidth=2)
        self.name_widget.pack(side='left', anchor='e')
        self.join_button = Button(frame, text='Соединение', width=10, command=self.on_join).pack(side='left')
        frame.pack(side='top', anchor='nw')
    

    def display_chat_box(self):
        frame = Frame()
        Label(frame, text='Chat Box:', font=('Serif', 12)).pack(side='top', anchor='w')
        self.chat_transcript_area = Text(width=60, height=10, font=('Serif', 12))
        scrollbar = Scrollbar(frame, command=self.chat_transcript_area.yview, orient=VERTICAL)
        self.chat_transcript_area.config(yscrollcommand=scrollbar.set)
        self.chat_transcript_area.bind('<KeyPress>', lambda e: 'break')
        self.chat_transcript_area.pack(side='left', padx=10)
        scrollbar.pack(side='right', fill='y')
        frame.pack(side='top')

        
