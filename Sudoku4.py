import tkinter as tk
import random

def generate_grille():
    """Fonction qui genere la grille"""
    grille = [[0 for x in range(9)] for y in range(9)]
    for i in range(9):
        for j in range(9):
            if random.random() < 0.5:
                valeur = random.randint(1, 9)
                if is_valid(grille, i, j, valeur):
                    grille[i][j] = valeur
    return grille

def is_valid(grille, ligne, col, valeur):
    """Fonction qui verifie les conditions"""
    if valeur in grille[ligne] or any(grille[i][col] == valeur for i in range(9)):
        return False
    region_ligne = (ligne // 3) * 3
    region_col = (col // 3) * 3
    return not any(grille[i][j] == valeur for i in range(region_ligne, region_ligne + 3) for j in range(region_col, region_col + 3))

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