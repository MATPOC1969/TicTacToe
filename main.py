
"""Игра до трех побед — реализуй систему, в которой игра продолжается до трех побед одного из игроков
Счетчик побед — добавь счетчик побед для каждого игрока (самое масштабное расширение проекта)
Выбор для игрока — добавь возможность выбрать, чем будет играть игрок (крестиком или ноликом), перед началом игрыУлучшение интерфейса — поработай над дизайном игры, сделай её более привлекательной и удобной для пользователя

Вариант ничьей — если все клетки поля заполнены, но победителя нет, показывай сообщение о ничьей
Добавить функциональность сброса игрового поля, чтобы можно было начать новую игру без перезапуска программы"""

from operator import truediv
import tkinter as tk
from tkinter import messagebox
import json
import os

# Создание главного окна
window = tk.Tk()

=======
window.title("🏆 Крестики-нолики - Статистика")
window.geometry("500x600")
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


# Статистика
stats = {
    "X_wins": 0,
    "O_wins": 0,
    "draws": 0,
    "total_games": 0,
    "current_streak": {"X": 0, "O": 0},
    "longest_streak": {"X": 0, "O": 0}
}

# Файл для сохранения статистики
STATS_FILE = "tictactoe_stats.json"

def load_stats():
    """Загружает статистику из файла"""
    global stats
    if os.path.exists(STATS_FILE):
        try:
            with open(STATS_FILE, 'r', encoding='utf-8') as f:
                stats = json.load(f)
        except:
            pass

def save_stats():
    """Сохраняет статистику в файл"""
    try:
        with open(STATS_FILE, 'w', encoding='utf-8') as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)
    except:
        pass

def update_stats_display():
    """Обновляет отображение статистики"""
    # Основная статистика
    x_wins_label.config(text=f"🏆 Победы X: {stats['X_wins']}")
    o_wins_label.config(text=f"🏆 Победы O: {stats['O_wins']}")
    draws_label.config(text=f"🤝 Ничьи: {stats['draws']}")
    total_games_label.config(text=f"📊 Всего игр: {stats['total_games']}")
    
    # Процент побед
    if stats['total_games'] > 0:
        x_percent = (stats['X_wins'] / stats['total_games']) * 100
        o_percent = (stats['O_wins'] / stats['total_games']) * 100
        draw_percent = (stats['draws'] / stats['total_games']) * 100
        
        x_percent_label.config(text=f"({x_percent:.1f}%)")
        o_percent_label.config(text=f"({o_percent:.1f}%)")
        draw_percent_label.config(text=f"({draw_percent:.1f}%)")
    
    # Серии побед
    x_streak_label.config(text=f"🔥 Серия X: {stats['current_streak']['X']}")
    o_streak_label.config(text=f"🔥 Серия O: {stats['current_streak']['O']}")
    x_longest_label.config(text=f"🏅 Макс. серия X: {stats['longest_streak']['X']}")
    o_longest_label.config(text=f"🏅 Макс. серия O: {stats['longest_streak']['O']}")

def reset_stats():
    """Сбрасывает всю статистику"""
    if messagebox.askyesno("Сброс статистики", "Вы уверены, что хотите сбросить всю статистику?"):
        global stats
        stats = {
            "X_wins": 0,
            "O_wins": 0,
            "draws": 0,
            "total_games": 0,
            "current_streak": {"X": 0, "O": 0},
            "longest_streak": {"X": 0, "O": 0}
        }
        save_stats()
        update_stats_display()

def new_game():
    """Начинает новую игру"""
    global current_player, game_in_progress
    current_player = "X"
    game_in_progress = True
    
    # Очищаем поле
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j]["state"] = "normal"
    
    # Обновляем информацию о текущем игроке
    current_player_label.config(text=f"🎯 Ход игрока: {current_player}")


def check_winner():
    """Проверяет, есть ли победитель"""
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


    """Проверяет ничью"""


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


# Загружаем статистику
load_stats()


# Создание интерфейса
# Заголовок
title_label = tk.Label(
    window,

    text="🏆 КРЕСТИКИ-НОЛИКИ",
    font=("Arial", 20, "bold"),

    bg="#2c3e50",
    fg="#ecf0f1"
)
title_label.pack(pady=10)


# Панель статистики
stats_frame = tk.Frame(window, bg="#34495e", relief="raised", bd=2)
stats_frame.pack(fill="x", padx=10, pady=5)

# Основная статистика
main_stats_frame = tk.Frame(stats_frame, bg="#34495e")
main_stats_frame.pack(pady=5)

x_wins_label = tk.Label(
    main_stats_frame,
    text=f"🏆 Победы X: {stats['X_wins']}",
    font=("Arial", 12, "bold"),
    bg="#34495e",
    fg="#e74c3c"
)
x_wins_label.pack(side="left", padx=10)

x_percent_label = tk.Label(
    main_stats_frame,
    text="(0.0%)",
    font=("Arial", 10),
    bg="#34495e",
    fg="#bdc3c7"
)
x_percent_label.pack(side="left")

o_wins_label = tk.Label(
    main_stats_frame,
    text=f"🏆 Победы O: {stats['O_wins']}",
    font=("Arial", 12, "bold"),
    bg="#34495e",
    fg="#f39c12"
)
o_wins_label.pack(side="left", padx=10)


o_percent_label = tk.Label(
    main_stats_frame,
    text="(0.0%)",
    font=("Arial", 10),
    bg="#34495e",
    fg="#bdc3c7"
)
o_percent_label.pack(side="left")

# Дополнительная статистика
extra_stats_frame = tk.Frame(stats_frame, bg="#34495e")
extra_stats_frame.pack(pady=5)

draws_label = tk.Label(
    extra_stats_frame,
    text=f"🤝 Ничьи: {stats['draws']}",
    font=("Arial", 11),
    bg="#34495e",
    fg="#3498db"
)
draws_label.pack(side="left", padx=10)

draw_percent_label = tk.Label(
    extra_stats_frame,
    text="(0.0%)",
    font=("Arial", 10),
    bg="#34495e",
    fg="#bdc3c7"
)
draw_percent_label.pack(side="left")

total_games_label = tk.Label(
    extra_stats_frame,
    text=f"📊 Всего игр: {stats['total_games']}",
    font=("Arial", 11),
    bg="#34495e",
    fg="#2ecc71"
)
total_games_label.pack(side="left", padx=10)

# Серии побед
streaks_frame = tk.Frame(stats_frame, bg="#34495e")
streaks_frame.pack(pady=5)

x_streak_label = tk.Label(
    streaks_frame,
    text=f"🔥 Серия X: {stats['current_streak']['X']}",
    font=("Arial", 10),
    bg="#34495e",
    fg="#e74c3c"
)
x_streak_label.pack(side="left", padx=5)

x_longest_label = tk.Label(
    streaks_frame,
    text=f"🏅 Макс. серия X: {stats['longest_streak']['X']}",
    font=("Arial", 10),
    bg="#34495e",
    fg="#e74c3c"
)
x_longest_label.pack(side="left", padx=5)

o_streak_label = tk.Label(
    streaks_frame,
    text=f"🔥 Серия O: {stats['current_streak']['O']}",
    font=("Arial", 10),
    bg="#34495e",
    fg="#f39c12"
)
o_streak_label.pack(side="left", padx=5)

o_longest_label = tk.Label(
    streaks_frame,
    text=f"🏅 Макс. серия O: {stats['longest_streak']['O']}",
    font=("Arial", 10),
    bg="#34495e",
    fg="#f39c12"
)
o_longest_label.pack(side="left", padx=5)

# Кнопки управления
controls_frame = tk.Frame(window, bg="#2c3e50")
controls_frame.pack(pady=10)

new_game_button = tk.Button(
    controls_frame,
    text="🆕 Новая игра",
    font=("Arial", 12, "bold"),
    bg="#27ae60",
    fg="white",
    command=new_game
)
new_game_button.pack(side="left", padx=5)

reset_stats_button = tk.Button(
    controls_frame,
    text="🗑️ Сбросить статистику",
    font=("Arial", 12),
    bg="#e74c3c",
    fg="white",
    command=reset_stats
)
reset_stats_button.pack(side="left", padx=5)

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
