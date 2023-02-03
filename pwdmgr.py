import hashlib
import tkinter as tk
from tkinter import messagebox

def create_password_hash(password):
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    return password_hash

def store_password(service, username, password):
    password_hash = create_password_hash(password)
    with open("/home/santhosh/Documents/PythonProj/passwords.txt", "a") as password_file:
        password_file.write(f"{service},{username},{password_hash}\n")

def retrieve_password(service):
    with open("/home/santhosh/Documents/PythonProj/passwords.txt", "r") as password_file:
        for line in password_file:
            line = line.strip().split(",")
            if line[0] == service:
                return line[1], line[2]
    return None, None

def login():
    master_password = master_password_entry.get()
    master_password_hash = create_password_hash(master_password)
    with open("master.txt", "r") as master_file:
        stored_password_hash = master_file.read().strip()
        if stored_password_hash == master_password_hash:
            return True
    return False

def store_password_command():
    service = service_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    store_password(service, username, password)
    messagebox.showinfo("Password Manager", "Password stored successfully.")

def retrieve_password_command():
    service = service_entry.get()
    username, password_hash = retrieve_password(service)
    if username is None:
        messagebox.showerror("Password Manager", "Service not found.")
    else:
        username_entry.delete(0, tk.END)
        username_entry.insert(0, username)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password_hash)

root = tk.Tk()
root.title("Password Manager")

master_password_label = tk.Label(root, text="Master Password:")
master_password_label.grid(row=0, column=0)

master_password_entry = tk.Entry(root, show="*")
master_password_entry.grid(row=0, column=1)

service_label = tk.Label(root, text="Service:")
service_label.grid(row=1, column=0)

service_entry = tk.Entry(root)
service_entry.grid(row=1, column=1)

username_label = tk.Label(root, text="Username:")
username_label.grid(row=2, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=2, column=1)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)

store_password_button = tk.Button(root, text="Store Password", command=store_password_command)
store_password_button.grid(row=4, column=0)

retrieve_password_button = tk.Button(root, text="Retrieve Password", command=retrieve_password_command)
retrieve_password_button.grid(row=4, column=1)

root.mainloop()