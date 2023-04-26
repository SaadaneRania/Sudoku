import tkinter as tk
import random
from tkinter import messagebox

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
            if case.get():
                valeur = int(case.get())
                if not is_valid(grille, i, j, valeur):
                    case.config(bg="red")
                else:
                    case.config(bg="white")

def undo():
    """Fonction qui annule la dernière action"""
    if actions:
        i, j = actions.pop()
        cases[i][j].delete(0, tk.END)
        cases[i][j].config(bg="white")

def clear():
    """Fonction qui efface tous les chiffres entrés par l'utilisateur"""
    for i in range(9):
        for j in range(9):
            if (i, j) not in initial_values:
                cases[i][j].delete(0, tk.END)
                cases[i][j].config(bg="white")
    actions.clear()

def save():
    """Fonction qui sauvegarde l'état actuel de la grille"""
    with open("sudoku_save.txt", "w") as f:
        for i in range(9):
            for j in range(9):
                case = cases[i][j]
                if case.get():
                    f.write(f"{i} {j} {case.get()}\n")

def load():
    """Fonction qui charge une grille sauvegardée"""
    try:
        with open("sudoku_save.txt", "r") as f:
            clear()
            initial_values.clear()
            for line in f:
                i, j, valeur = map(int, line.split())
                cases[i][j].insert(0, str(valeur))
                initial_values.add((i,j))
    except FileNotFoundError:
        messagebox.showerror("Erreur", "Aucune sauvegarde trouvée")

def show_help():
    """Fonction qui affiche l'aide"""
    number = simpledialog.askinteger("Aide", "Entrez un chiffre à afficher")
    if number is not None:
        clear_highlight()
        for i in range(9):
            for j in range(9):
                case = cases[i][j]
                if case.get() and int(case.get()) == number:
                    case.config(bg="lightblue")

def clear_highlight():
    """Fonction qui efface les mises en évidence"""
    for i in range(9):
        for j in range(9):
            cases[i][j].config(bg="white")

def validate():
    """Fonction qui valide la grille"""
    highlight_errors()
    if all(cases[i][j].get() and is_valid(grille,i,j,int(cases[i][j].get())) for i in range(9) for j in range(9)):
        messagebox.showinfo("Bravo!", "Vous avez réussi!")

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
        
