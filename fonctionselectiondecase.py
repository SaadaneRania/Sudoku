def select_cell( event): #Sélection d'une cellule de la grille
    x, y = event.x, event.y
    i, j = y//50, x//50
    if selected_cell:
        selected_cell = cell[i][j]
        canvas.itemconfig(selected_cell["rect"], outline = "blue")

def donner_valeur_cell(i, j, value):
    #Définition de la valeur d'une cellule
    cell = cell[i][j]
    if value == 0:
        canvas.itemconfig(cell["text"], text = "")
    else:
        canvas.itemconfig(cell["text"],text = "")

def valeur_dans_cell(i, j):
    # Récupération de la valeur d'une cellule
    cell = cell[i][j]
    value = cell["text"]
    if value != 0:
        return int(value)
    else:
        return 0
