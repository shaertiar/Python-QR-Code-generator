import tkinter as tk
import qrcode
import os
from PIL import ImageTk, Image

# Функция генерации QR-кода
def generate_QR():
    global img, qr_code_img

    # Проверка на наличие папки
    try:
        os.mkdir('QrCodes')
    except:
        None

    if entry.get() != '':
        # Генерация QR-кода
        try:
            qrcode.make(entry.get()).save(f'QrCodes/{entry.get()}.png')

            qr_code_img = ImageTk.PhotoImage(Image.open(f'QrCodes/{entry.get()}.png'))

            img['image'] = qr_code_img

        except:
            img['text'] = "Ошибка создания QR-кода. \nВозможно вы использовали символы '\\' или '/'."

    else:
        img['text'] = "Пожалуйста введите хоть какой нибудь текст."

# Создание окна
root = tk.Tk()
root.geometry('350x400')
root.title('Генератор QR-кода')

# Создание бортика
frame = tk.LabelFrame(root, padx=20, pady=20)

# Создание текста
text = tk.Label(root, text='')
img = tk.Label(frame, text='')

# Созданияе поля для ввода
entry = tk.Entry(frame, width=35, border=5)

# Создание кнопки
button = tk.Button(frame, text='Сгенерировать', command=generate_QR)

# Размещение элементов
frame.pack()
entry.pack()
button.pack()
img.pack()
text.pack()

# Запуск приложения
root.mainloop()