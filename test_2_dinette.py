import tkinter as tk
import random

def generate_grille():
    """Fonction qui genere la grille"""
    grille = [[0 for x in range(9)] for y in range(9)] #creer une grille vide de taille 9x9
    for i in range(9):#boucle pour remplir les lignes de la grille
        for j in range(9):#boucle pour remplir les colonnes de la grille
            if random.random() < 0.5:
                valeur = random.randint(1, 9)#les valeurs doivent etre comprises entre 1 et 9
                if is_valid(grille, i, j, valeur):#on verifie si le remplissage respecte les conditions
                    grille[i][j] = valeur
    return grille

def is_valid(grille, ligne, col, valeur):
    """Fonction qui verifie les conditions"""
    # Vérification de la ligne et de la colonne
    for i in range(9):
        if grille[ligne][i] == valeur:
            return False
        if grille[i][col] == valeur:
            return False
    # Vérification de la région
    region_ligne = (ligne // 3) * 3
    region_col = (col // 3) * 3
    for i in range(region_ligne, region_ligne + 3):
        for j in range(region_col, region_col + 3):
            if grille[i][j] == valeur:
                return False
    return True
    
grille = generate_grille()

fenetre = tk.Tk()
fenetre.title("Grille Sudoku")
fenetre.geometry("400x400")
fenetre.resizable(width=0, height=0)
cadre = tk.Frame(fenetre)
cadre.pack()

for i in range(9):
    for j in range(9):
        case = tk.Entry(cadre, width=3)
        case.grid(row=i, column=j)
        case.insert(0, str(grille[i][j]))

bouton_valider = tk.Button(fenetre, text="Valider")
bouton_valider.pack()

fenetre.mainloop()