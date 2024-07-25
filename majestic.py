import tkinter as tk
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.title("Majestic - Доход/Расход")
root.geometry("1600x900")

# Load background image
bg_image = tk.PhotoImage(file="bg.png")  # Replace with your image file

# Create Canvas with background image
canvas = tk.Canvas(root, width=1600, height=900)
canvas.pack()

canvas.create_image(0, 0, anchor=tk.NW, image=bg_image)

total_income = 0

def on_button_click():
    messagebox.showinfo('Сообщение', 'Приветики!')  # Corrected the message text

def on_help_click():
    messagebox.showinfo("О программе", "Версия 0.1\n Создано Basher")  # Corrected the message text

def add_income():
    global total_income
    income = simpledialog.askfloat('Добавить доход', 'Введите сумму дохода: ')
    if income is not None:
        total_income += income
        income_label.config(text=f"Общая сумма дохода: {total_income:.2f}")


label = tk.Label(canvas, text='Добро пожаловать в программу', font=('Arial', 24, 'bold'), bg='white')
canvas.create_window(800, 50, window=label)

income_label = tk.Label(canvas, text='Общая сумма дохода: 0.00', font=('Arial', 18), bg='white')
canvas.create_window(200, 100, window=income_label)

button = tk.Button(canvas, text='Главная Кнопка', command=on_button_click, font=('Arial', 14))
canvas.create_window(400, 300, window=button)

help_button = tk.Button(canvas, text='Помощь', command=on_help_click, font=('Arial', 14))
canvas.create_window(700, 550, window=help_button)

add_income_button = tk.Button(canvas, text='Добавить Доход', command=add_income, font=('Arial', 14))
canvas.create_window(100, 550, window=add_income_button)

root.mainloop()
