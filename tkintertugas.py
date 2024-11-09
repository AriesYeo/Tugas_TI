import tkinter as tk
from tkinter import ttk

def save_action():
    pass

def update_action():
    pass

def delete_action():
    pass

window = tk.Tk()
window.title("Desain GUI")

tk.Label(window, text="Kode Kategori").grid(row=0, column=0, padx=10, pady=5, sticky="w")
kode_entry = tk.Entry(window)
kode_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Nama").grid(row=1, column=0, padx=10, pady=5, sticky="w")
nama_entry = tk.Entry(window)
nama_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Jenis Kategori").grid(row=2, column=0, padx=10, pady=5, sticky="w")
jenis_combobox = ttk.Combobox(window, values=["Jenis 1", "Jenis 2", "Jenis 3"])
jenis_combobox.grid(row=2, column=1, padx=10, pady=5)

save_button = tk.Button(window, text="Save", command=save_action)
save_button.grid(row=3, column=0, padx=10, pady=10)
update_button = tk.Button(window, text="Update", command=update_action)
update_button.grid(row=3, column=1, padx=10, pady=10)
delete_button = tk.Button(window, text="Delete", command=delete_action)
delete_button.grid(row=3, column=2, padx=10, pady=10)

info_label = tk.Label(window, text=" ", anchor="w", width=40, height=10, relief="solid")
info_label.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

window.mainloop()
