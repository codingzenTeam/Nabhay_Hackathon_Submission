
def set_game_to_grid(grid):
    for j in range(len(grid)):
        for k in range(len(grid[j])):
            entries[j][k].delete(0, tk.END)
            if grid[j][k] != 0:
                entries[j][k].insert(0, grid[j][k])

def autosolve():
    if mode == 9:
        game.start_solve()
    if mode == 16:
        game.start_solve16x16()
    if mode == 4:
        game.start_solve4x4()

    set_game_to_grid(game.grid)

def rand_grid():
    if mode == 9:
        game.set_rand_grid()
    if mode == 16:
        game.set_rand_grid16x16()
    if mode == 4:
        game.set_rand_grid4x4()
    set_game_to_grid(game.grid)

def load_board():
    game.grid = eval(input('Input your matrix : '))
    set_game_to_grid(game.grid)
    print("Loaded your input! Click 'Solve' to automatically solve it")

def solve_image():
    pass

def init():
    global mode
    mode = 9
    global entries
    global frames
    n = 0
    if entries != []:
        for i in range(len(entries)):
            for j in range(len(entries[i])):
                entries[i][j].grid_remove()
        for i in range(len(frames)):
            frames[i].grid_remove()
    entries = []
    for i in range(9):
        entries.append([0]*9)
    for box_col in range(3):
        for box_row in range(3):
            
            box = ttk.Frame(mainFrame, borderwidth=1, relief='sunken')
            box.grid(column=box_col+1, row=box_row+1)
            frames.append(box)
            for cell_col in range(3):
                for cell_row in range(3):
                    n+=1
                    entry = tk.Entry(box,name=str(n), font=('Courier',33,'normal'),highlightthickness=2, justify='center')
                    entry.config(highlightbackground = "black", highlightcolor= "black",width=2)
                    entry.grid(column=cell_col+1, row=cell_row+1)
                    entries[3*box_row+cell_row][3*box_col+cell_col] = entry

def init16x16():
    global mode
    mode = 16
    global entries
    global frames
    n = 0
    if entries != []:
        for i in range(len(entries)):
            for j in range(len(entries[i])):
                entries[i][j].grid_remove()
        for i in range(len(frames)):
            frames[i].grid_remove()
    entries = []
    for i in range(16):
        entries.append([0]*16)
    for box_col in range(4):
        for box_row in range(4):
            
            box = ttk.Frame(mainFrame, borderwidth=1, relief='sunken')
            box.grid(column=box_col+1, row=box_row+1)
            frames.append(box)
            for cell_col in range(4):
                for cell_row in range(4):
                    n+=1
                    entry = tk.Entry(box,name=str(n), font=('Courier',15,'normal'),highlightthickness=2, justify='center')
                    entry.config(highlightbackground = "black", highlightcolor= "black",width=2)
                    entry.grid(column=cell_col+1, row=cell_row+1)
                    entries[4*box_row+cell_row][4*box_col+cell_col] = entry

def init4x4():
    global mode
    mode = 4
    global entries
    global frames
    n = 0
    if entries != []:
        for i in range(len(entries)):
            for j in range(len(entries[i])):
                entries[i][j].grid_remove()
        for i in range(len(frames)):
            frames[i].grid_remove()
    entries = []
    for i in range(4):
        entries.append([0]*4)
    for box_col in range(2):
        for box_row in range(2):
            
            box = ttk.Frame(mainFrame, borderwidth=1, relief='sunken')
            box.grid(column=box_col+1, row=box_row+1)
            frames.append(box)
            for cell_col in range(2):
                for cell_row in range(2):
                    n+=1
                    entry = tk.Entry(box,name=str(n), font=('Courier',80,'normal'),highlightthickness=2, justify='center')
                    entry.config(highlightbackground = "black", highlightcolor= "black",width=2)
                    entry.grid(column=cell_col+1, row=cell_row+1)
                    entries[2*box_row+cell_row][2*box_col+cell_col] = entry
from tkinter import ttk
import tkinter as tk
from grid import Grid
import random
r = tk.Tk()
mainFrame = ttk.Frame(r, borderwidth=10)
mainFrame.grid(column=1, row=1)
r.title('Pseudoku')
r.geometry("700x522")

entries = []
frames = []
mode = 9
init()
game = Grid()
game.set_rand_grid()
game.print()
set_game_to_grid(game.grid)


button1 = tk.Button(text="Solve", font=('Courier',12,'normal'),justify='center',command=autosolve)
button1.place(x=590, y=150)

button2 = tk.Button(text="Randomize", font=('Courier',12,'normal'),justify='center',command=rand_grid)
button2.place(x=570, y=190)

button3 = tk.Button(text="Load Input", font=('Courier',12,'normal'),justify='center',command=load_board)
button3.place(x=565, y=230)

button4 = tk.Button(text="16x16", font=('Courier',12,'normal'),justify='center',command=init16x16)
button4.place(x=590, y=270)

button4 = tk.Button(text="9x9", font=('Courier',12,'normal'),justify='center',command=init)
button4.place(x=600, y=310)

button4 = tk.Button(text="4x4", font=('Courier',12,'normal'),justify='center',command=init4x4)
button4.place(x=600, y=350)
r.mainloop()
