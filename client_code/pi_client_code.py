import socket
import threading
import tkinter as tk

HOST = "192.168.1.5"  # Replace with Windows IP
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_data():
    while True:
        try:
            data = client.recv(1024).decode()
            if data:
                text_box.insert(tk.END, "Windows: " + data + "\n")
        except:
            break

def send_data():
    message = entry.get()
    if message:
        client.send(message.encode())
        text_box.insert(tk.END, "Raspberry Pi: " + message + "\n")
        entry.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("Raspberry Pi Client")

text_box = tk.Text(root, height=15, width=50)
text_box.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_data)
send_button.pack()

threading.Thread(target=receive_data, daemon=True).start()

root.mainloop()
