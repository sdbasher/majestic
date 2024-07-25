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
purchase_list =[] #list


def on_button_click():
    messagebox.showinfo('Сообщение', 'Приветики!')  # Corrected the message text

def on_help_click():
    messagebox.showinfo("О программе", "Версия 0.1\nСоздано Basher\nЗаинтересовался данной темой у многих media Majestic RP\nВ каждой серии некоторые из них вносят суммы заработка за серию и тд.\nРешил Сделать тоже данную программу что бы упростить многим жизнь")  # Corrected the message text

def add_income():
    global total_income
    income = simpledialog.askfloat('Добавить доход', 'Введите сумму дохода: ')
    if income is not None:
        total_income += income
        income_label.config(text=f"Общая сумма дохода: {total_income:.2f}")

def purchase():
    global total_income
    purchase_amount = simpledialog.askfloat('Покупка', 'Введите сумму покупки: ')
    if purchase_amount is not None:
        purchase_name = simpledialog.askstring('Покупка', 'Введите наименование покупки: ')
        if purchase_name:
            total_income -= purchase_amount
            income_label.config(text=f"Общая сумма дохода: {total_income:.2f}")
            purchase_list.append(f"{purchase_name}: {purchase_amount:.2f}")

def show_checklist():
    checklist = '\n'.join(purchase_list)
    if not checklist:
        checklist = 'Список покупок и продаж пуст.'
    messagebox.showinfo('Список Покупок и Продаж', checklist)


label = tk.Label(canvas, text='Добро пожаловать в программу', font=('comic sans ms', 24, 'bold'), bg='gold')
canvas.create_window(800, 50, window=label)

income_label = tk.Label(canvas, text='Баланс: $', font=('comic sans ms', 14), bg='white')
canvas.create_window(200, 100, window=income_label)

purchase_button = tk.Button(canvas, text='Покупка', command=purchase, font=('Arial', 14))
canvas.create_window(100, 300, window=purchase_button)

checklist_button = tk.Button(canvas, text='ЧекЛист', command=show_checklist, font=('Arial', 14))
canvas.create_window(100, 400, window=checklist_button)

help_button = tk.Button(canvas, text='Help', command=on_help_click, font=('monospace', 10))
canvas.create_window(800, 850, window=help_button)

add_income_button = tk.Button(canvas, text='Введите сумму старта', command=add_income, font=('Arial', 14))
canvas.create_window(100, 20, window=add_income_button)

root.mainloop()
