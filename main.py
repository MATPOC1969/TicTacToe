"""Выбор для игрока — добавь возможность выбрать, чем будет играть игрок (крестиком или ноликом), перед началом игры"""    

from operator import truediv
import tkinter as tk
from tkinter import messagebox

# Переменные игры
current_player = "X"
buttons = []
player_symbol = "X"  # Символ игрока
computer_symbol = "O"  # Символ компьютера

def show_symbol_selection():
    """Показывает диалог выбора символа для игрока"""
    global player_symbol, computer_symbol
    
    # Создаем диалоговое окно
    dialog = tk.Toplevel()
    dialog.title("Выбор символа")
    dialog.geometry("300x200")
    dialog.resizable(False, False)
    dialog.transient(window)  # Делаем диалог модальным
    dialog.grab_set()  # Захватываем фокус
    
    # Центрируем диалог
    dialog.update_idletasks()
    x = (dialog.winfo_screenwidth() // 2) - (300 // 2)
    y = (dialog.winfo_screenheight() // 2) - (200 // 2)
    dialog.geometry(f"300x200+{x}+{y}")
    
    # Заголовок
    title_label = tk.Label(dialog, text="Выберите ваш символ:", font=("Arial", 14, "bold"))
    title_label.pack(pady=20)
    
    # Функция выбора X
    def choose_x():
        global player_symbol, computer_symbol
        player_symbol = "X"
        computer_symbol = "O"
        dialog.destroy()
        start_game()
    
    # Функция выбора O
    def choose_o():
        global player_symbol, computer_symbol
        player_symbol = "O"
        computer_symbol = "X"
        dialog.destroy()
        start_game()
    
    # Кнопки выбора
    button_frame = tk.Frame(dialog)
    button_frame.pack(pady=20)
    
    x_button = tk.Button(
        button_frame,
        text="X (Крестик)",
        font=("Arial", 16, "bold"),
        width=8,
        height=2,
        command=choose_x
    )
    x_button.pack(side="left", padx=10)
    
    o_button = tk.Button(
        button_frame,
        text="O (Нолик)",
        font=("Arial", 16, "bold"),
        width=8,
        height=2,
        command=choose_o
    )
    o_button.pack(side="left", padx=10)
    
    # Ждем закрытия диалога
    dialog.wait_window()

def start_game():
    """Запускает игру после выбора символа"""
    global current_player
    
    # Устанавливаем первого игрока (всегда X начинает)
    current_player = "X"
    
    # Обновляем заголовок окна с информацией о выборе
    window.title(f"Крестики-нолики - Вы играете за {player_symbol}")
    
    # Показываем информацию о выборе
    info_label = tk.Label(
        window,
        text=f"Вы играете за: {player_symbol} | Компьютер играет за: {computer_symbol}",
        font=("Arial", 10),
        fg="blue"
    )
    info_label.grid(row=0, column=0, columnspan=3, pady=5)

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
            winner = "Вы" if current_player == player_symbol else "Компьютер"
            messagebox.showinfo("Победа!", f"{winner} победил!")
            window.quit()
        elif check_draw():
            messagebox.showinfo("Ничья!", "Игра закончилась вничью!")
            window.quit()
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        messagebox.showinfo("Ошибка!", "Эта клетка уже занята!")

# Создание главного окна
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("300x350")

# Создаем игровое поле
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 40), width=3, height=1, command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i+1, column=j)  # Сдвигаем на одну строку вниз для места под информацию
        row.append(button)
    buttons.append(row)

# Показываем диалог выбора символа
show_symbol_selection()

window.mainloop()
