grille_0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
]

grille_1 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0],
]

grille_2 = [
    [6, 2, 5, 8, 4, 3, 7, 9, 1],
    [7, 9, 1, 2, 6, 5, 4, 8, 3],
    [4, 8, 3, 9, 7, 1, 6, 2, 5],
    [8, 1, 4, 5, 9, 7, 2, 3, 6],
    [2, 3, 6, 1, 8, 4, 9, 5, 7],
    [9, 5, 7, 3, 2, 6, 8, 1, 4],
    [5, 6, 9, 4, 3, 2, 1, 7, 8],
    [3, 4, 2, 7, 1, 8, 5, 6, 9],
    [1, 7, 8, 6, 5, 9, 3, 4, 2],
]



def afficher(x):
    ligne0 = "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗"
    ligne1 = "║ . │ . │ . ║ . │ . │ . ║ . │ . │ . ║"
    ligne2 = "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢"
    ligne3 = "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣"
    ligne4 = "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝"

    valeurs = [[""]+[" 1234567890"[case] for case in ligne] for ligne in x]

    print(ligne0)
    for ligne in range(1,9+1):
        print("".join(n+s for (n, s) in zip(valeurs[ligne-1], ligne1.split("."))))
        print([ligne2, ligne3, ligne4][(ligne % 9 == 0) + (ligne % 3 == 0)])


def ligne(x, i):
    return x[i-1]   # Renvoie la ligne i de la grille de sudoku x


def unique(x):
    taille_x = 0
    taille_set_x = len(set(x))
    if 0 in x:
        taille_set_x -= 1
    for element in x:
        if element !=0:
            taille_x += 1
    if taille_x == taille_set_x:
        return True
    else:
        return False


def colonne(x, i):
    liste_colonne = []
    for num_colonne in range(1, 10):
        for ligne in range(1, 10):
            if  (num_colonne == i):
                liste_colonne.append(x[ligne-1][num_colonne-1])
    return liste_colonne


def region(x, i):
    liste = []
    for num_ligne in range (1, 10):
        for num_colonne in range (1, 10):
            k = 3 * ((num_ligne-1)//3) + ((num_colonne-1)//3) + 1
            if int(k) == i:
                liste.append(x[num_ligne-1][num_colonne-1])
    return liste


def ajouter(x, i, j, v):
    if unique(ligne(x, i)) and unique(colonne(x, j)) and unique(region(x, i)):
        x[i][j] = v


def verifier(x):
    somme = 0
    valide = True
    for i in range(0, 9):   # vérification de la validité de la ligne, colonne, et région
        if not unique(ligne(x, i)) or not unique(colonne(x, i)) or not unique(region(x, i)):
            valide = False
        for j in range(0, 9):   # vérification des 0
            if x[i][j] != 0:
                somme += 1
    if somme == 81 and valide:
        return True
    else:
        return False


def jouer(x):
    while not verifier(x):
        afficher(x)
        i = int(input("Entrer la ligne (0 à 8):"))
        j = int(input("Entrer la colonne (0 à 8):"))
        v = int(input("Entrer la valeur à ajouter à la grille :"))
        ajouter(x, i, j, v)


def solutions(x):
    dict = {}   # définition du dictionnaire
    for i in range(0, 10):
        dict[i] = []

    for i in range(0, 9):
        for j in range(0, 9):
            if x[i][j] == 0: # si la case est vide alors on détermine les solutions possibles
                valeurs_potentielles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                for element in ligne(x, i+1):   # vérification de la ligne
                    if element in valeurs_potentielles:
                        valeurs_potentielles.remove(element)
                for element in colonne(x, j+1):     # vérification de la colonne
                    if element in valeurs_potentielles:
                        valeurs_potentielles.remove(element)
                k = 3 * (i // 3) + (j // 3) + 1
                for element in region(x, k):    # vérification de la région
                    if element in valeurs_potentielles:
                        valeurs_potentielles.remove(element)

                # ajout des valeurs potentielles au dictionnaire
                dict[len(valeurs_potentielles)] += [(i, j, valeurs_potentielles)]

    return dict


def resoudre(x):
    dictionnaire = solutions(x)
    l = []

    for element in dictionnaire.values():
        if element:
            for tuple in element:
                l.append((tuple[0], tuple[1], tuple[2]))
    
import random  

def generer_grille():
    x = [[0 for j in range(9)] for i in range(9)]  # Crée une grille vide

    for k in range(1, 10):  # Remplit chaque région avec des valeurs aléatoires
        valeurs_restantes = list(range(1, 10))
        for i in range(3 * ((k-1)//3), 3 * ((k-1)//3) + 3):
            for j in range(3 * ((k-1)%3), 3 * ((k-1)%3) + 3):
                if valeurs_restantes:
                    v = random.choice(valeurs_restantes)
                    valeurs_restantes.remove(v)
                    x[i][j] = v

    return x

def nouvelle():
    pass

#print("ligne :", ligne(grille_1, 1))
#print(colonne(grille_1, 1))
#print(region(grille_1, 1))
#print(unique(grille_2[0]))
#print(verifier(grille_2))
grile = generer_grille()
print(grile)
"""jouer(grile)
solutions(grile)
print(resoudre(grile))"""


import tkinter as tk

class SudokuApp:
    def __init__(self, master):
        self.master = master
        master.title("Sudoku")

        # Créer la grille 9x9 des widgets d'entrée
        self.entries = []
        for i in range(9):
            row = []
            for j in range(9):
                e = tk.Entry(master, width=2, font=("Arial", 20, "bold"), justify="center")
                e.grid(row=i, column=j, padx=1, pady=1)
                e.bind("<KeyRelease>", self.on_key_release)
                row.append(e)
            self.entries.append(row)

        # créer le boutton solution
        self.solve_button = tk.Button(master, text="Solve", command=self.solve)
        self.solve_button.grid(row=10, column=4, pady=10)

        # Créer le boutton reset
        self.reset_button = tk.Button(master, text="Reset", command=self.reset)
        self.reset_button.grid(row=10, column=5, pady=10)

        # Créer l'étiquette de statut
        self.status = tk.Label(master, text="")
        self.status.grid(row=11, column=0, columnspan=9, pady=10)

        #Initialiser la grille Sudoku à tous les zéros
        self.grid = [[0 for j in range(9)] for i in range(9)]

    def on_key_release(self, event):
        # Mettre à jour la grille Sudoku avec la nouvelle entrée
        for i in range(9):
            for j in range(9):
                if event.widget == self.entries[i][j]:
                    value = event.widget.get()
                    if value.isdigit():
                        self.grid[i][j] = int(value)
                    else:
                        self.grid[i][j] = 0
        self.status.config(text="")

    def solve(self):
        #resoud le sudoku
        solutions_dict = solutions(self.grid)
        num_solutions = len(solutions_dict[1])
        if num_solutions == 0:
            self.status.config(text="This Sudoku puzzle has no solutions.")
        elif num_solutions == 1:
            solution = solutions_dict[1][0]
            for i in range(9):
                for j in range(9):
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(solution[i][j]))
        else:
            self.status.config(text="This Sudoku puzzle has multiple solutions.")

    def reset(self):
        # Réinitialiser la grille Sudoku à tous les zéros
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, "0")
                self.grid[i][j] = 0
        self.status.config(text="")

root = tk.Tk()
app = SudokuApp(root)
root.mainloop()