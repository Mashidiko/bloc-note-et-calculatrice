
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

# Fonction pour activer/désactiver le style italique sur le texte sélectionné
def toggle_italic():
    if text_widget.tag_ranges("sel"):
        current_tags = text_widget.tag_names("sel.first")
        if "italic" in current_tags:
            text_widget.tag_remove("italic", "sel.first", "sel.last")
        else:
            text_widget.tag_add("italic", "sel.first", "sel.last")
            text_widget.tag_configure("italic", font=(current_font[0], current_font_size, "italic"))

# Fonction pour activer/désactiver le style souligné sur le texte sélectionné
def toggle_underline():
    if text_widget.tag_ranges("sel"):
        current_tags = text_widget.tag_names("sel.first")
        if "underline" in current_tags:
            text_widget.tag_remove("underline", "sel.first", "sel.last")
        else:
            text_widget.tag_add("underline", "sel.first", "sel.last")
            text_widget.tag_configure("underline", underline=True)

# Fonction pour choisir une police de caractères
def choose_font(font_family):
    global current_font
    current_font = font_family
    text_widget.config(font=font_family)

# Fonction pour choisir la couleur du texte
def choose_color():
    color = askcolor()[1]  # Demander à l'utilisateur de choisir une couleur
    if color:
        text_widget.config(fg=color)

# Fonction pour ouvrir la calculatrice
def open_calculator():
    calculator_window = tk.Toplevel(root)
    calculator_window.title("Calculatrice")

    entry = tk.Entry(calculator_window, font=("Helvetica", 20))
    entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
        ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
        ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ("=", 5, 0, 1, 4)
    ]

    for (text, row, col, *span) in buttons:
        button = ttk.Button(calculator_window, text=text)
        button.grid(row=row, column=col, columnspan=span[-1] if span else 1, sticky="nsew")
        button.bind("<Button-1>", lambda event, entry=entry: calculator_button_click(event, entry))

# Fonction pour le clic sur les boutons de la calculatrice
def calculator_button_click(event, entry):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)


