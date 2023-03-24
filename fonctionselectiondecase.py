def select_cell(self, event):
    #Sélection d'une cellule de la grille
    x, y = event.x, event.y
    i, j = y//50, x//50
    if self.selected_cell:
        self.selected_cell = self.cells[i][j]
        self.canvas.itemconfig(self.selected_cell["rect"], outline = "blue")

def set_cell_value(i, j, value):
    #Définition de la valeur d'une cellule
    cell = self.cells[i][j]
    if value == 0:
        self.canvas.itemconfig(cell["text"], text = "")
    else:
        self.canvas.itemconfig(cell["text"],text = "")

def get_cell_value(i, j):
    # Récupération de la valeur d'une cellule
    cell = self.cells[i][j]
    value = cell["text"]
    if value != 0:
        return int(value)
    else:
        return 0
