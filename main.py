
"""Вариант ничьей — если все клетки поля заполнены, но победителя нет, показывай сообщение о ничьей
Добавить функциональность сброса игрового поля, чтобы можно было начать новую игру без перезапуска программы"""


from operator import truediv
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x400")

current_player = "X"
buttons = []

def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"

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

            # Отключаем все кнопки после победы
            for i in range(3):
                for j in range(3):
                    buttons[i][j]["state"] = "disabled"
        elif check_draw():
            messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
            # Отключаем все кнопки после ничьей
            for i in range(3):
                for j in range(3):
                    buttons[i][j]["state"] = "disabled"

        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showinfo("Ошибка!", "Эта клетка уже занята!")

# Создаем игровое поле
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 40), width=3, height=1, command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i, column=j, padx=2, pady=2)
        row.append(button)
    buttons.append(row)

# Кнопка "Новая игра"
reset_button = tk.Button(window, text="Новая игра", font=("Arial", 16), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")

window.mainloop()
