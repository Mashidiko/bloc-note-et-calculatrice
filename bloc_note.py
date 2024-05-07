import tkinter as tk
from tkinter import font as tkFont
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor
from tkinter import ttk  # Importez ttk pour la calculatrice

# Définition de la taille de police par défaut
current_font_size = 12
current_font = ("Arial", current_font_size)

 #Fonction pour sauvegarder le contenu du texte dans un fichier
def save_file():
    try:
        text_content = text_widget.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if not file_path:
            return
        with open(file_path, 'w') as file:
            file.write(text_content)
            messagebox.showinfo("Succès", "Le fichier a été sauvegardé avec succès")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Fonction pour ouvrir un fichier et afficher son contenu dans la zone de texte
def open_file():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")]
        )
        if not file_path:
            return
        with open(file_path, 'r') as file:
            file_content = file.read()
            text_widget.delete("1.0", tk.END)
            text_widget.insert("1.0", file_content)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Fonction pour effacer tout le contenu de la zone de texte
def new_file():
    text_widget.delete("1.0", tk.END)

# Fonction pour sauvegarder le contenu du texte dans un nouveau fichier
def save_as_file():
    save_file()

# Fonction pour activer/désactiver le style gras sur le texte sélectionné
def toggle_bold():
    if text_widget.tag_ranges("sel"):
        current_tags = text_widget.tag_names("sel.first")
        if "bold" in current_tags:
            text_widget.tag_remove("bold", "sel.first", "sel.last")
        else:
            text_widget.tag_add("bold", "sel.first", "sel.last")
            text_widget.tag_configure("bold", font=(current_font[0], current_font_size, "bold"))

