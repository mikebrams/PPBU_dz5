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
    url = f'https://open.er-api.com/v6/latest/{base}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if target not in data['rates']:
            mb.showerror('Ошибка', f'Целевая валюта {target} для базовой валюты {base} - не найдена')
        else:
            exchange_rate = data['rates'][target]
            return exchange_rate
    except Exception as e:
        mb.showerror('Ошибка', f'Произошла ошибка:\n{e}')

def exchange():
    target_code = comb3.get()   # eg 'AUD: Австралийский доллар'
    if not target_code:
        mb.showwarning('Внимание', 'Выберите целевую валюту')
        return
    target = target_code[:3]
    base1 = comb1.get()[:3]
    base2 = comb2.get()[:3]

    if not base1 and not base2:
        mb.showwarning('Внимание', 'Выберите хотя бы одну базовую валюту')
        return
    elif base1 and base2:
        rate1 = get_rate(base1, target)
        rate2 = get_rate(base2, target)
        mb.showinfo('Курсы обмена',f'1 {base1}\t= {rate1:>10.2f} {target_code[:3]}\n'
                                       f'1 {base2}\t= {rate2:>10.2f} {target_code[:3]}')
    else:
        base = max(base1, base2)
        rate = get_rate(base, target)
        mb.showinfo('Курс обмена',f'1 {base}\t= {rate:>10.2f} {target_code[:3]}')



currencies = {
    '': '',
    '111': '222',
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

Button(text='Получить курс обмена', font=('Helvetica', 10, 'bold'), command=exchange).pack(pady=8)

root.mainloop()
