import re

def get_user_input():
    date_pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')  # Формат ГГГГ-ММ-ДД
    time_pattern = re.compile(r'^\d{2}:\d{2}$')  # Формат ЧЧ:ММ

    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    while not date_pattern.match(date):
        print("Неверный формат даты. Пожалуйста, используйте формат ГГГГ-ММ-ДД.")
        date = input("Введите дату (ГГГГ-ММ-ДД): ")

    time = input("Введите время (ЧЧ:ММ): ")
    while not time_pattern.match(time):
        print("Неверный формат времени. Пожалуйста, используйте формат ЧЧ:ММ.")
        time = input("Введите время (ЧЧ:ММ): ")

    text = input("Введите текст записи: ")
    return date, time, text
def display_entries(entries):
    for entry in entries:
        print(entry)