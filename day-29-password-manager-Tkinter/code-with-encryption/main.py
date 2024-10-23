from tkinter import *
from tkinter import messagebox, ttk
from random import choice, randint, shuffle
from cryptography.fernet import Fernet
import pyperclip
import os
import pandas as pd


# ---------------------------- CRYPTOGRAPHY ------------------------------- #

def generate_key():
    key = Fernet.generate_key()
    with open("chave.key", "wb") as key_file:
        key_file.write(key)
    return key


def load_key():
    with open("chave.key", "rb") as key_file:
        return key_file.read()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"These are the details entered: "
                                                                   f"\nE-mail/Username: {username}"
                                                                   f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            df = pd.DataFrame([[website, username, encrypted_password.decode()]],
                              columns=["Website", "Username", "Password"])

            if os.path.exists("passwords.csv"):
                existing_df = pd.read_csv("passwords.csv")
                df = pd.concat([existing_df, df], ignore_index=True)

            df.to_csv("passwords.csv", index=False)

            website_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(END, string="Your E-mail")
            password_entry.delete(0, END)


# ---------------------------- SHOW PASSWORD ------------------------------- #

def load_passwords():
    key = load_key()
    fernet = Fernet(key)
    if os.path.exists("passwords.csv"):
        df = pd.read_csv("passwords.csv")
        decoded_passwords = []
        for _, row in df.iterrows():
            website = row["Website"]
            username = row["Username"]
            encrypted_password = row["Password"]
            try:
                decoded_password = fernet.decrypt(encrypted_password.encode()).decode()
                decoded_passwords.append((website, username, decoded_password))
            except Exception as e:
                print(f"Error decrypting data: {encrypted_password}\n{e}")
        return decoded_passwords
    else:
        return []


def show_passwords():
    passwords = load_passwords()
    global popup, tree
    popup = Toplevel(window)
    popup.title("Decrypted Passwords")

    columns = ("#1", "Website", "Username", "Password")
    tree = ttk.Treeview(popup, columns=columns, show="headings")
    tree.heading("#1", text="Index")
    tree.heading("Website", text="Website")
    tree.heading("Username", text="Username")
    tree.heading("Password", text="Password")

    for i, (website, username, password) in enumerate(passwords, start=1):
        tree.insert("", "end", values=(i, website, username, password))

    tree.pack(padx=20, pady=20)
    tree.bind("<Double-1>", copy_to_clipboard)

    popup.transient(window)
    popup.grab_set()
    popup.attributes("-topmost", True)

def copy_to_clipboard(event):
    item = tree.selection()[0]
    values = tree.item(item, "values")
    popup.clipboard_clear()
    popup.clipboard_append(values[3])
    messagebox.showinfo("Copied!", "Password details copied to the clipboard")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()
username_entry = Entry()
username_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_entry.insert(END, string="Your E-mail")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", command=save)
add_button.grid(column=1, row=4, sticky="EW")
show_password_button = Button(text="Show Passwords", command=show_passwords)
show_password_button.grid(column=2, row=4, sticky="EW")

if not os.path.exists("chave.key"):
    generate_key()

window.mainloop()
