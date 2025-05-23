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



