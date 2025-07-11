from pathlib import Path
import sys


# Відкриття файлу

file_path = input('Введіть шлях до файлу: ')
path = Path(file_path)

if path.exists() and path.is_file(): # перевірка існування файлу за вказаним посиланням
    text = path.read_text()
    print('Прийнято файл логів')
else:
    print("Файл не знайдено або шлях некоректний.")

# Необов'язковий аргумент командного рядка, виведення всі записи певного рівння логування

