
"""Выбор для игрока — добавь возможность выбрать, чем будет играть игрок (крестиком или ноликом), перед началом игрыУлучшение интерфейса — поработай над дизайном игры, сделай её более привлекательной и удобной для пользователя

Вариант ничьей — если все клетки поля заполнены, но победителя нет, показывай сообщение о ничьей
Добавить функциональность сброса игрового поля, чтобы можно было начать новую игру без перезапуска программы"""




from operator import truediv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


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
    global current_player, move_count
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
        messagebox.showinfo("⚠️ Ошибка!", "Эта клетка уже занята!")

# Создание заголовка
title_frame = tk.Frame(window, bg=COLORS["title_bg"], height=80)
title_frame.pack(fill="x", padx=10, pady=(10, 5))

title_label = tk.Label(
    title_frame,
    text="🎮 КРЕСТИКИ-НОЛИКИ",
    font=("Arial", 20, "bold"),
    bg=COLORS["title_bg"],
    fg=COLORS["title_fg"]
)
title_label.pack(expand=True)

# Информационная панель
info_frame = tk.Frame(window, bg=COLORS["bg"])
info_frame.pack(fill="x", padx=10, pady=5)

player_label = tk.Label(
    info_frame,
    text=f"Ход игрока: {current_player}",
    font=("Arial", 14, "bold"),
    bg=COLORS["bg"],
    fg=COLORS["button_fg"]
)
player_label.pack(side="left")


move_label = tk.Label(
    info_frame,
    text="Ход: 0",
    font=("Arial", 12),
    bg=COLORS["bg"],
    fg=COLORS["button_fg"]
)
move_label.pack(side="right")

# Игровое поле
game_frame = tk.Frame(window, bg=COLORS["bg"])
game_frame.pack(pady=20)


# Создаем игровое поле
for i in range(3):
    row = []
    for j in range(3):


        button = tk.Button(
            game_frame,
            text="",
            font=("Arial", 32),
            width=4,
            height=2,
            bg=COLORS["button_bg"],
            fg=COLORS["button_fg"],
            relief="raised",
            bd=3,
            command=lambda i=i, j=j: on_click(i, j)
        )
        button.grid(row=i, column=j, padx=3, pady=3)
        row.append(button)
    buttons.append(row)

# Панель с подсказками
hint_frame = tk.Frame(window, bg=COLORS["bg"])
hint_frame.pack(fill="x", padx=10, pady=10)

hint_label = tk.Label(
    hint_frame,
    text="💡 Кликайте по клеткам, чтобы сделать ход",
    font=("Arial", 10),
    bg=COLORS["bg"],
    fg=COLORS["button_fg"]
)
hint_label.pack()

# Запуск игры


window.mainloop()
