"""Вариант ничьей — если все клетки поля заполнены, но победителя нет, показывай сообщение о ничьей"""

from operator import truediv
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

current_player = "X"
buttons = []

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_draw():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        if check_winner():
            messagebox.showinfo("Победа!", f"Игрок {current_player} победил!")
            window.quit()
        elif check_draw():
            messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
            window.quit()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showinfo("Ошибка!", "Эта клетка уже занята!")

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 40), width=3, height=1, command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

window.mainloop()
