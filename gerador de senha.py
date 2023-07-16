import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length < 8:
        password_label.config(text="A senha deve ter no mínimo 8 caracteres.", fg="red")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    password_label.config(text=f"Senha gerada: {password}", fg="green")

root = tk.Tk()
root.title("Gerador de Senha")
root.geometry("300x200")

def center_window(w, h):
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry(f"{w}x{h}+{int(x)}+{int(y)}")

center_window(300, 200)

title_label = tk.Label(root, text="Gerador de Senha", font=("Helvetica", 16, "bold"), bg="pink", fg="black")
title_label.pack(fill=tk.X)

font_label = ("Helvetica", 12)
font_entry = ("Helvetica", 14)
font_button = ("Helvetica", 12, "bold")

label_length = tk.Label(root, text="Comprimento da senha:", font=font_label, bg='pink')
label_length.pack(pady=10)

length_entry = tk.Entry(root, font=font_entry)
length_entry.pack()

btn_generate = tk.Button(root, text="Gerar Senha", font=font_button, command=generate_password)
btn_generate.pack(pady=10)

password_label = tk.Label(root, text="", font=font_label)
password_label.pack()

root.config(bg="pink")
root.mainloop()

