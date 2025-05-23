import tkinter as tk
from tkinter import messagebox
import random

flashcards = []

def add():
    q = entry_q.get()
    a = entry_a.get()
    if q and a:
        flashcards.append((q, a))
        entry_q.delete(0, tk.END)
        entry_a.delete(0, tk.END)
    else:
        messagebox.showwarning("Erro", "Por favor, preencha prgunta e resposta!")

def review():
    global current
    if flashcards:
        current=random.choice(flashcards)
        lbl_q.config(text=f"?{current[0]}")
        lbl_a.config(text="resposta:???")
        btn_show.config(state=tk.NORMAL)
    else:
        messagebox.showinfo("Erro","Nenhum flashcards adicionado.")

def show_answer():
    lbl_a.config(text=f"✅ {current[1]}")
    btn_show.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Flashcards")
root.geometry("400x400")

tk.Label(root, text="Pergunta:").pack()
entry_q = tk.Entry(root, width=40)
entry_q.pack()

tk.Label(root, text="Resposta:").pack()
entry_a = tk.Entry(root, width=40)
entry_a.pack()

tk.Button(root, text="Adicionar", command=add).pack(pady=5)
tk.Button(root, text="Revisar", command=review).pack(pady=5) 
btn_show=tk.Button(root, text="Mostrar Resposta",command=show_answer,state=tk.DISABLED)
btn_show.pack(pady=5)

lbl_q=tk.Label(root, text="? Questao",font=("Arial",14))
lbl_q.pack(pady=5)
lbl_a=tk.Label(root,text="Resposta:???",font=("Arial",14))
lbl_a.pack(pady=5)

current=None
root.mainloop()
