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



