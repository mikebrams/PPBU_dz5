from tkinter import *
from tkinter import ttk


def update_base_currency1_label(event):
    code = comb1.get()
    if code:
        name1.config(text='')
    else:
        name1.config(text='Выберите валюту', font=('Helvetica', 9), fg='#525264')

def update_base_currency2_label(event):
    code = comb2.get()
    if code:
        name2.config(text='')
    else:
        name2.config(text='Выберите валюту', font=('Helvetica', 9), fg='#525264')

def update_target_currency_label(event):
    code = comb3.get()
    if code:
        name3.config(text='')
    else:
        name3.config(text='Выберите валюту', font=('Helvetica', 9), fg='#525264')


currencies = {
    '': '',
    'AUD: Австралийский доллар': ('AUD', 'Австралийский доллар'),
    'CAD: Канадский доллар': ('CAD', 'Канадский доллар'),
    'CHF: Швейцарский франк': ('CHF', 'Швейцарский франк'),
    'CNY: Китайский юань': ('CNY', 'Китайский юань'),
    'EUR: Евро': ('EUR', 'Евро'),
    'GBP: Фунт стерлингов': ('GBP', 'Фунт стерлингов'),
    'JPY: Японская йена': ('JPY', 'Японская йена'),
    'KZT: Казахстанский тенге': ('KZT', 'Казахстанский тенге'),
    'RUB: Российский рубль': ('RUB', 'Российский рубль'),
    'USD: Доллар США': ('USD', 'Доллар США'),
    'UZS: Узбекский сум': ('UZS', 'Узбекский сум')}

root = Tk()
root.title('Курсы обмена валют')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w2 = w // 4
h2 = h // 3
root.geometry(f'300x350+{w2}+{h2}')

frame1 = Frame(borderwidth=1, relief='raised', bg='Gainsboro')
frame1.pack(padx=10, pady=4, fill='both')

label1 = Label(frame1, text='Базовая валюта 1', font=('Helvetica', 10, 'bold'), bg='Gainsboro')
label1.pack(pady=8)
comb1 = ttk.Combobox(frame1, values=list(currencies), width=30, state='readonly')
comb1.pack(pady=2)
comb1.bind('<<ComboboxSelected>>', update_base_currency1_label)
name1 = Label(frame1, text='Выберите валюту', font=('Helvetica', 9), fg='#525264', bg='Gainsboro')
name1.pack(pady=2)

frame2 = Frame(borderwidth=1, relief='raised', bg='Gainsboro')
frame2.pack(padx=10, pady=4, fill='both')

label2 = Label(frame2, text='Базовая валюта 2', font=('Helvetica', 10, 'bold'), bg='Gainsboro')
label2.pack(pady=8)
comb2 = ttk.Combobox(frame2, values=list(currencies), width=30, state='readonly')
comb2.pack(pady=2)
comb2.bind('<<ComboboxSelected>>', update_base_currency2_label)
name2 = Label(frame2, text='Выберите валюту', font=('Helvetica', 9), fg='#525264', bg='Gainsboro')
name2.pack(pady=2)

frame3 = Frame(borderwidth=1, relief='raised')
frame3.pack(padx=10, pady=4, fill='both')

label3 = Label(frame3, text='Целевая валюта', font=('Helvetica', 10, 'bold'))
label3.pack(pady=8)
comb3 = ttk.Combobox(frame3, values=list(currencies), width=30, state='readonly')
comb3.pack(pady=2)
comb3.bind('<<ComboboxSelected>>', update_target_currency_label)
name3 = Label(frame3, text='Выберите валюту', font=('Helvetica', 9), fg='#525264')
name3.pack(pady=2)

Button(text='Получить курс обмена', font=('Helvetica', 10, 'bold')).pack(pady=8)

root.mainloop()
