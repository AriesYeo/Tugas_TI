import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("400x300")
root.configure(bg="#8FD9FB")

title_label = tk.Label(root, text="Login", font=("Arial", 20), bg="#8FD9FB")
title_label.pack(pady=20)

email_label = tk.Label(root, text="Email address", font=("Arial", 12), bg="#8FD9FB", anchor="w")
email_label.pack(fill="x", padx=50)
email_entry = tk.Entry(root, font=("Arial", 12))
email_entry.pack(fill="x", padx=50, pady=5)

password_label = tk.Label(root, text="Password", font=("Arial", 12), bg="#8FD9FB", anchor="w")
password_label.pack(fill="x", padx=50)
password_entry = tk.Entry(root, font=("Arial", 12), show="*")
password_entry.pack(fill="x", padx=50, pady=5)

login_button = tk.Button(root, text="Login", font=("Arial", 12), bg="gray", fg="black")
login_button.pack(pady=20)

root.mainloop()