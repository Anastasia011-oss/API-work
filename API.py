import requests
import tkinter as tk
from tkinter import ttk, messagebox

def get_rates():
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    data = response.json()

    rates = {"UAH": 1.0}

    for currency in data:
        rates[currency["ccy"]] = float(currency["sale"])

    return rates

def convert():
    try:
        amount = float(entry_amount.get())
        from_currency = combo_from.get()
        to_currency = combo_to.get()

        rates = get_rates()

        if from_currency in rates and to_currency in rates:
            uah = amount * rates[from_currency]
            result = uah / rates[to_currency]

            label_result.config(
                text=f"{amount} {from_currency} = {result:.2f} {to_currency}"
            )
        else:
            messagebox.showerror("Ошибка", "Неверная валюта")

    except:
        messagebox.showerror("Ошибка", "Введите число")

window = tk.Tk()
window.title("Конвертер валют")

tk.Label(window, text="Сумма:").pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

tk.Label(window, text="Из валюты:").pack()
combo_from = ttk.Combobox(window, values=["UAH", "USD", "EUR"])
combo_from.current(1)
combo_from.pack()

tk.Label(window, text="В валюту:").pack()
combo_to = ttk.Combobox(window, values=["UAH", "USD", "EUR"])
combo_to.current(0)
combo_to.pack()

tk.Button(window, text="Конвертировать", command=convert).pack()

label_result = tk.Label(window, text="")
label_result.pack()

window.mainloop()