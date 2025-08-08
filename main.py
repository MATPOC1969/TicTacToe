"""Улучшение интерфейса — поработай над дизайном игры, сделай её более привлекательной и удобной для пользователя"""

from operator import truediv
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Создание главного окна
window = tk.Tk()
window.title("🎮 Крестики-нолики")
window.geometry("400x500")
window.configure(bg="#2c3e50")
window.resizable(False, False)

# Центрирование окна на экране
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# Переменные игры
current_player = "X"
buttons = []
move_count = 0

# Стили и цвета
COLORS = {
    "bg": "#2c3e50",
    "button_bg": "#34495e",
    "button_fg": "#ecf0f1",
    "button_active": "#3498db",
    "x_color": "#e74c3c",
    "o_color": "#f39c12",
    "title_bg": "#1abc9c",
    "title_fg": "#ffffff"
}

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
        
        # Стилизация кнопки в зависимости от игрока
        if current_player == "X":
            buttons[row][col].configure(
                fg=COLORS["x_color"],
                font=("Arial", 36, "bold"),
                bg=COLORS["button_bg"]
            )
        else:
            buttons[row][col].configure(
                fg=COLORS["o_color"],
                font=("Arial", 36, "bold"),
                bg=COLORS["button_bg"]
            )
        
        move_count += 1
        move_label.config(text=f"Ход: {move_count}")
        
        if check_winner():
            messagebox.showinfo("🎉 Победа!", f"Игрок {current_player} победил!")
            window.quit()
        elif check_draw():
            messagebox.showinfo("🤝 Ничья!", "Игра закончилась вничью!")
            window.quit()
        else:
            current_player = "O" if current_player == "X" else "X"
            player_label.config(text=f"Ход игрока: {current_player}")
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
