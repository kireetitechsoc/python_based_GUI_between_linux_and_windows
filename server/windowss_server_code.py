import socket
import threading
import tkinter as tk

HOST = "0.0.0.0"
PORT = 5000

client_socket = None

def receive_data():
    global client_socket
    while True:
        try:
            data = client_socket.recv(1024).decode()
            if data:
                text_box.insert(tk.END, "Raspberry Pi: " + data + "\n")
        except:
            break

def send_data():
    global client_socket
    message = entry.get()
    if message and client_socket:
        client_socket.send(message.encode())
        text_box.insert(tk.END, "Windows: " + message + "\n")
        entry.delete(0, tk.END)

def start_server():
    global client_socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    text_box.insert(tk.END, "Waiting for connection...\n")
    client_socket, addr = server.accept()
    text_box.insert(tk.END, "Connected to " + str(addr) + "\n")
    threading.Thread(target=receive_data, daemon=True).start()

# GUI
root = tk.Tk()
root.title("Windows Server")

text_box = tk.Text(root, height=15, width=50)
text_box.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_data)
send_button.pack()

threading.Thread(target=start_server, daemon=True).start()

root.mainloop()
