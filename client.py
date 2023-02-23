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
         
