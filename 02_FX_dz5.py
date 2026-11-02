from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests


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


def get_rate(base, target):
    url = f'https://---open.er-api.com/v6/latest/{base}'
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return f"Ошибка: HTTP {response.status_code}"
        # response.raise_for_status()
        data = response.json()
        if target not in data['rates']:
            # mb.showerror('Ошибка', f'Целевая валюта {target} не найдена')
            return f'Целевая валюта {target} не найдена'
        else:
            exchange_rate = data['rates'][target]
            return exchange_rate
    except Exception as e:
        # mb.showerror('Ошибка', f'Произошла ошибка:\n{e}')
        return f'Произошла ошибка:\n{e}'

def exchange():
    target_code = comb3.get()   # eg 'AUD: Австралийский доллар'
    if not target_code:
        mb.showwarning('Внимание', 'Выберите целевую валюту')
        return
    target = target_code[:3]
    base1 = comb1.get()[:3]
    base2 = comb2.get()[:3]

    if not base1 or not base2:
        mb.showwarning('Внимание', 'Выберите две разные базовые валюты')
        return
    else:
        rate1 = get_rate(base1, target)
        rate2 = get_rate(base2, target)
        if isinstance(rate1, float) and isinstance(rate2, float):
            rate1_float = rate1
            rate2_float = rate2
            mb.showinfo('Курсы обмена',f'Курс 1:\t 1 {base1}\t= {rate1_float:.2f} {target_code[:3]}\n'
                                           f'Курс 2:\t 1 {base2}\t= {rate2_float:.2f} {target_code[:3]}')

        elif not isinstance(rate1, float) and not isinstance(rate1, float):
            rate1_str = rate1
            rate2_str = rate2
            mb.showinfo('Курсы обмена',f'Курс 1:\t {rate1_str}\nКурс 2:\t {rate2_str}')

        elif not isinstance(rate1, float):
            rate1_str = rate1
            mb.showinfo('Курсы обмена', f'Курс 1:\t {rate1_str}\n'
                                        f'Курс 2:\t {base2}\t= {rate2:.2f} {target_code[:3]}')
        else:
            rate2_str = rate2
            mb.showinfo('Курсы обмена', f'Курс 1:\t 1 {base1}\t= {rate1:.2f} {target_code[:3]}\n'
                                        f'Курс 2:\t 1 {rate2_str}')

currencies = {
    '': '',
    '111': '222',
    'AUD: Австралийский доллар': 'AUD',
    'CAD: Канадский доллар': 'CAD',
    'CHF: Швейцарский франк': 'CHF',
    'CNY: Китайский юань': 'CNY',
    'EUR: Евро': 'EUR',
    'GBP: Фунт стерлингов': 'GBP',
    'JPY: Японская йена': 'JPY',
    'KZT: Казахстанский тенге': 'KZT',
    'RUB: Российский рубль': 'RUB',
    'USD: Доллар США': 'USD',
    'UZS: Узбекский сум': 'UZS'}

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

Button(text='Получить курс обмена', font=('Helvetica', 10, 'bold'), command=exchange).pack(pady=8)

root.mainloop()
