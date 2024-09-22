import tkinter as tk
from tkinter import messagebox 

def evaluate_score():
    try:
        nilai = int(entry.get())
        if nilai >= 90:
            result = 'sangat baik'
        elif (nilai >= 80) and (nilai < 90):
            result = 'baik'
        elif (nilai >= 60) and (nilai < 80):
            result = 'kurang baik'
        elif (nilai >= 40) and (nilai < 60):
            result = 'cukup'
        elif nilai < 40:
            result = 'jelek...' 
        else:
            result = 'maaf,format nilai tidak sesuai'

        messagebox.showinfo("Hasil Evaluasi", f'Nilai: {nilai}\nPredikat: {result}')
    except ValueError:
        messagebox.showerror("input error", "silahkan masuk nilai yang valid.")

root = tk.Tk()
root.title("evaluasi nilai siswa")

label = tk.Label(root, text="masukkan nilai siswa: ")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="evaluasi", command=evaluate_score)
button.pack(pady=20)

root.mainloop()