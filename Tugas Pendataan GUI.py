import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

root = tk.Tk()
root.title("Customer Management")
root.geometry("600x650")
root.configure(bg="#FF3333")
img = PhotoImage(file="KFC1.png")
img = img.zoom(8,5)
img = img.subsample(32)
title_label = tk.Label(root, image=img)
title_label.pack(pady=10)

form_frame = tk.Frame(root,bg="#FA8072" )
form_frame.pack(pady=10, padx=20, fill="x")

tk.Label(form_frame,bg="#FA8072", text="Kode Customer:").grid(row=0, column=0, sticky="w", pady=5)
kode_customer_entry = tk.Entry(form_frame, width=30)
kode_customer_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame,bg="#FA8072", text="Nama Customer:").grid(row=1, column=0, sticky="w", pady=5)
nama_customer_entry = tk.Entry(form_frame, width=30)
nama_customer_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, bg="#FA8072", text="Jenis Kelamin:").grid(row=2, column=0, sticky="w", pady=5)
gender_frame = tk.Frame(form_frame)
gender_frame.grid(row=2, column=1, sticky="w")
gender_var = tk.StringVar(value="Pria")
tk.Radiobutton(gender_frame,bg="#FA8072", text="Pria", variable=gender_var, value="Pria").pack(side="left")
tk.Radiobutton(gender_frame,bg="#FA8072", text="Wanita", variable=gender_var, value="Wanita").pack(side="left")

tk.Label(form_frame,bg="#FA8072", text="Alamat:").grid(row=3, column=0, sticky="w", pady=5)
alamat_combobox = ttk.Combobox(form_frame, values=["Batam", "Jakarta", "Surabaya"], state="readonly", width=28)
alamat_combobox.set("Batam")
alamat_combobox.grid(row=3, column=1, pady=5)

table_frame = tk.Frame(root,bg="#FA8072")
table_frame.pack(pady=10, fill="both", expand=True)

columns = ("Kode Customer", "Nama Customer", "Jenis Kelamin", "Alamat")
tree = ttk.Treeview(table_frame, columns=columns, show="headings")
tree.pack(fill="both", expand=True)

for col in columns:
    tree.heading(col, text=col)

button_frame = tk.Frame(root,bg="#FA8072")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Simpan", width=10).pack(side="left", padx=5)
tk.Button(button_frame, text="Edit", width=10).pack(side="left", padx=5)
tk.Button(button_frame, text="Delete", width=10).pack(side="left", padx=5)
tk.Button(button_frame, text="Bersih", width=10).pack(side="left", padx=5)


root.mainloop()