

import tkinter as tk
from tkinter import messagebox 

def searcing_NPM():
    try: 
        NPM = int (entry.get())
        if  NPM == 130029:
            result = 'Welcome Dinda'
        elif  NPM == 130102:
            result = 'Welcome Rino'
        else: 
            result = 'Tidak Terdaftar'

        messagebox.showinfo("Data NPM Siswa", f'NPM: {NPM}\nNamaSiswa: {result}')
    except ValueError:
        messagebox.showerror("NPM tidak terdaftar", "silahkan masuk NPM yang valid.")

root = tk.Tk()
root.title("Data Login NPM Siswa")

label = tk.Label(root, text="masukkan NPM siswa: ")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Enter", command=searcing_NPM)
button.pack(pady=20)

root.mainloop()