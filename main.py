"""Игра до трех побед — реализуй систему, в которой игра продолжается до трех побед одного из игроков"""
from operator import truediv
import tkinter as tk
from tkinter import messagebox

# Создание главного окна
window = tk.Tk()
window.title("🏆 Крестики-нолики - До 3 побед")
window.geometry("400x500")
window.configure(bg="#2c3e50")
window.resizable(False, False)

# Центрирование окна
window.update_idletasks()
width = window.winfo_width()
height = window.winfo_height()
x = (window.winfo_screenwidth() // 2) - (width // 2)
y = (window.winfo_screenheight() // 2) - (height // 2)
window.geometry(f"{width}x{height}+{x}+{y}")

# Переменные игры
current_player = "X"
buttons = []
game_in_progress = False

# Счет раундов
round_scores = {
    "X": 0,
    "O": 0
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

def reset_board():
    """Сбрасывает игровое поле"""
    global current_player, game_in_progress
    current_player = "X"
    game_in_progress = True
    
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"
            buttons[i][j].configure(fg="black", font=("Arial", 40))
    
    current_player_label.config(text=f"🎯 Ход игрока: {current_player}")

def new_series():
    """Начинает новую серию игр"""
    global round_scores
    if messagebox.askyesno("Новая серия", "Начать новую серию игр? Текущий счет будет сброшен."):
        round_scores = {"X": 0, "O": 0}
        update_score_display()
        reset_board()

def update_score_display():
    """Обновляет отображение счета"""
    x_score_label.config(text=f"🏆 X: {round_scores['X']}")
    o_score_label.config(text=f"🏆 O: {round_scores['O']}")
    
    # Определяем лидера
    if round_scores['X'] > round_scores['O']:
        leader_label.config(text="👑 Лидер: X", fg="#e74c3c")
    elif round_scores['O'] > round_scores['X']:
        leader_label.config(text="👑 Лидер: O", fg="#f39c12")
    else:
        leader_label.config(text="⚖️ Ничья", fg="#3498db")

def on_click(row, col):
    global current_player, game_in_progress
    
    if not game_in_progress:
        return
        
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        
        # Стилизация кнопки
        if current_player == "X":
            buttons[row][col].configure(fg="#e74c3c", font=("Arial", 36, "bold"))
        else:
            buttons[row][col].configure(fg="#f39c12", font=("Arial", 36, "bold"))
        
        if check_winner():
            # Победа в раунде
            round_scores[current_player] += 1
            update_score_display()
            
            game_in_progress = False
            
            # Проверяем, достиг ли кто-то 3 побед
            if round_scores[current_player] >= 3:
                messagebox.showinfo("🎉 Финальная победа!", 
                                  f"Игрок {current_player} выиграл серию со счетом {round_scores['X']}:{round_scores['O']}!")
                
                # Отключаем все кнопки
                for i in range(3):
                    for j in range(3):
                        buttons[i][j]["state"] = "disabled"
                
                # Предлагаем начать новую серию
                if messagebox.askyesno("Новая серия", "Хотите начать новую серию игр?"):
                    new_series()
            else:
                messagebox.showinfo("🎯 Победа в раунде!", 
                                  f"Игрок {current_player} выиграл этот раунд!\nСчет: X - {round_scores['X']}, O - {round_scores['O']}")
                
                # Отключаем все кнопки
                for i in range(3):
                    for j in range(3):
                        buttons[i][j]["state"] = "disabled"
                
                # Предлагаем продолжить серию
                if messagebox.askyesno("Следующий раунд", "Начать следующий раунд?"):
                    reset_board()
                    
        elif check_draw():
            # Ничья в раунде
            game_in_progress = False
            messagebox.showinfo("🤝 Ничья в раунде!", "Этот раунд закончился вничью!")
            
            # Отключаем все кнопки
            for i in range(3):
                for j in range(3):
                    buttons[i][j]["state"] = "disabled"
            
            # Предлагаем продолжить серию
            if messagebox.askyesno("Следующий раунд", "Начать следующий раунд?"):
                reset_board()
        else:
            # Продолжаем раунд
            current_player = "O" if current_player == "X" else "X"
            current_player_label.config(text=f"🎯 Ход игрока: {current_player}")
    else:
        messagebox.showinfo("⚠️ Ошибка!", "Эта клетка уже занята!")

# Создание интерфейса
# Заголовок
title_label = tk.Label(
    window,
    text="🏆 ДО ТРЕХ ПОБЕД",
    font=("Arial", 18, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1"
)
title_label.pack(pady=10)

# Панель счета
score_frame = tk.Frame(window, bg="#34495e", relief="raised", bd=2)
score_frame.pack(fill="x", padx=10, pady=5)

# Счет игроков
score_display_frame = tk.Frame(score_frame, bg="#34495e")
score_display_frame.pack(pady=10)

x_score_label = tk.Label(
    score_display_frame,
    text=f"🏆 X: {round_scores['X']}",
    font=("Arial", 16, "bold"),
    bg="#34495e",
    fg="#e74c3c"
)
x_score_label.pack(side="left", padx=20)

vs_label = tk.Label(
    score_display_frame,
    text="VS",
    font=("Arial", 14, "bold"),
    bg="#34495e",
    fg="#ecf0f1"
)
vs_label.pack(side="left", padx=20)

o_score_label = tk.Label(
    score_display_frame,
    text=f"🏆 O: {round_scores['O']}",
    font=("Arial", 16, "bold"),
    bg="#34495e",
    fg="#f39c12"
)
o_score_label.pack(side="left", padx=20)

# Лидер
leader_label = tk.Label(
    score_frame,
    text="⚖️ Ничья",
    font=("Arial", 12, "bold"),
    bg="#34495e",
    fg="#3498db"
)
leader_label.pack(pady=5)

# Кнопки управления
controls_frame = tk.Frame(window, bg="#2c3e50")
controls_frame.pack(pady=10)

new_round_button = tk.Button(
    controls_frame,
    text="🔄 Новый раунд",
    font=("Arial", 12, "bold"),
    bg="#27ae60",
    fg="white",
    command=reset_board
)
new_round_button.pack(side="left", padx=5)

new_series_button = tk.Button(
    controls_frame,
    text="🏁 Новая серия",
    font=("Arial", 12),
    bg="#e74c3c",
    fg="white",
    command=new_series
)
new_series_button.pack(side="left", padx=5)

# Информация о текущем игроке
current_player_label = tk.Label(
    window,
    text="🎯 Ход игрока: X",
    font=("Arial", 14, "bold"),
    bg="#2c3e50",
    fg="#ecf0f1"
)
current_player_label.pack(pady=5)

# Игровое поле
game_frame = tk.Frame(window, bg="#2c3e50")
game_frame.pack(pady=10)

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(
            game_frame,
            text="",
            font=("Arial", 32),
            width=4,
            height=2,
            bg="#34495e",
            fg="#ecf0f1",
            relief="raised",
            bd=3,
            command=lambda i=i, j=j: on_click(i, j)
        )
        button.grid(row=i, column=j, padx=3, pady=3)
        row.append(button)
    buttons.append(row)

# Инструкция
instruction_label = tk.Label(
    window,
    text="💡 Играйте до 3 побед! Каждый раунд - это отдельная игра в крестики-нолики.",
    font=("Arial", 10),
    bg="#2c3e50",
    fg="#bdc3c7",
    wraplength=350
)
instruction_label.pack(pady=10)

# Инициализация
update_score_display()
reset_board()

window.mainloop()
