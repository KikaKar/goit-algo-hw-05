from pathlib import Path

file_path = input('Введіть шлях до файлу: ')
path = Path(file_path)

if path.exists() and path.is_file():
    text = path.read_text()
    print(text)
else:
    print("Файл не знайдено або шлях некоректний.")
