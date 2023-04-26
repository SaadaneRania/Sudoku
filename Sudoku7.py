import tkinter as tk
from tkinter import messagebox
import random
import json

def generate_grille(difficulty):
    """Fonction qui genere la grille"""
    grille = [[0 for x in range(9)] for y in range(9)] #creer une grille vide de taille 9x9
    for i in range(9):#boucle pour remplir les lignes de la grille
        for j in range(9):#boucle pour remplir les colonnes de la grille
            if random.random() < difficulty:
                valeur = random.randint(1, 9)#les valeurs doivent etre comprises entre 1 et 9
                if is_valid(grille, i, j, valeur):#on verifie si le remplissage respecte les conditions
                    grille[i][j] = valeur
    return grille

def is_valid(grille, ligne, col, valeur):
    """Fonction qui verifie les conditions"""
    # Vérification de la ligne et de la colonne
    if valeur in grille[ligne] or any(grille[i][col] == valeur for i in range(9)):
        return False

    # Vérification de la région
    region_ligne = (ligne // 3) * 3
    region_col = (col // 3) * 3
    for i in range(region_ligne, region_ligne + 3):
        for j in range(region_col, region_col + 3):
            if grille[i][j] == valeur:
                return False
    return True

def highlight_errors():
    """Fonction qui met en évidence les erreurs"""
    for i in range(9):
        for j in range(9):
            case = cases[i][j]
            valeur = case.get()
            if valeur:
                case.config(fg="black")
                if not is_valid(grille, i, j, int(valeur)):
                    case.config(fg="red")

def annuler():
    """Fonction pour annuler une partie"""
    global grille
    grille = generate_grille(difficulty)
    update_grille()

def effacer():
    """Fonction pour effacer des chiffres entrés"""
    for i in range(9):
        for j in range(9):
            case = cases[i][j]
            case.delete(0, tk.END)
            case.insert(0, str(grille[i][j]))

def sauvegarder():
    """Fonction pour sauvegarder l'état de jeu"""
    global saved_grille
    saved_grille = [[cases[i][j].get() for j in range(9)] for i in range(9)]
    with open("sudoku.json", "w") as f:
        json.dump(saved_grille, f)

def charger():
    """Fonction pour charger l'état de jeu sauvegardé"""
    global grille
    try:
        with open("sudoku.json", "r") as f:
            saved_grille = json.load(f)
        if saved_grille:
            grille = [[int(saved_grille[i][j]) if saved_grille[i][j] else 0 for j in range(9)] for i in range(9)]
            update_grille()
    except FileNotFoundError:
        pass

def update_grille():
    """Fonction pour mettre à jour l'affichage de la grille"""
    for i in range(9):
        for j in range(9):
            case = cases[i][j]
            case.delete(0, tk.END)
            if grille[i][j]:
                case.insert(0, str(grille[i][j]))
            highlight_errors()

def afficher_chiffre(chiffre):
    """Fonction pour afficher les cases contenant un chiffre donné"""
    for i in range(9):
        for j in range(9):
            case = cases[i][j]
            valeur = case.get()
            if valeur == str(chiffre):
                case.config(bg="lightblue")
            else:
                case.config(bg="white")

def check_victory():
    """Fonction pour vérifier si la grille est complète et correcte"""
    for i in range(9):
        for j in range(9):
            case = cases[i][j]
            valeur = case.get()
            if not valeur or not is_valid(grille, i, j, int(valeur)):
                return False
    return True

def set_difficulty(new_difficulty):
    """Fonction pour changer la difficulté"""
    global difficulty
    difficulty = new_difficulty
    annuler()

difficulty = 0.5
grille = generate_grille(difficulty)
saved_grille = None
fenetre = tk.Tk()
fenetre.title("Grille Sudoku")
fenetre.geometry("500x500")
fenetre.resizable(width=0, height=0)
cadre = tk.Frame(fenetre)
cadre.pack()
cases = [[None for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        case = tk.Entry(cadre, width=3)
        case.grid(row=i, column=j)
        case.insert(0, str(grille[i][j]))
        cases[i][j] = case
bouton_annuler = tk.Button(fenetre, text="Annuler", command=annuler)
bouton_annuler.pack()
bouton_effacer = tk.Button(fenetre, text="Effacer", command=effacer)
bouton_effacer.pack()
bouton_sauvegarder = tk.Button(fenetre, text="Sauvegarder", command=sauvegarder)
bouton_sauvegarder.pack()
bouton_charger = tk.Button(fenetre, text="Charger", command=charger)
bouton_charger.pack()
chiffres_cadre = tk.Frame(fenetre)
chiffres_cadre.pack()
for i in range(1, 10):
    bouton_chiffre = tk.Button(chiffres_cadre, text=str(i), command=lambda chiffre=i: afficher_chiffre(chiffre))
    bouton_chiffre.grid(row=0, column=i-1)
difficulte_cadre = tk.Frame(fenetre)
difficulte_cadre.pack()
bouton_facile = tk.Button(difficulte_cadre, text="Facile", command=lambda: set_difficulty(0.75))
bouton_facile.grid(row=0, column=0)
bouton_moyen = tk.Button(difficulte_cadre, text="Moyen", command=lambda: set_difficulty(0.5))
bouton_moyen.grid(row=0, column=1)
bouton_difficile = tk.Button(difficulte_cadre, text="Difficile", command=lambda: set_difficulty(0.25))
bouton_difficile.grid(row=0, column=2)
fenetre.mainloop()               