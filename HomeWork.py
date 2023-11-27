# HomeWork.py
from Entry import Entry
from EntryStorage import EntryStorage
from Interface import get_user_input, display_entries

def main():
    storage = EntryStorage()
    filename = "entries.csv"

    try:
        storage.load_from_file(filename)
        print("Записи загружены из файла.")
    except FileNotFoundError:
        print("Файл с записями не найден. Будет создан новый.")

    while True:
        print("\nЗаписная книжка:")
        print("1. Добавить запись")
        print("2. Показать все записи")
        print("3. Сохранить записи в файл")
        print("4. Загрузить записи из файла")
        print("5. Найти записи")
        print("6. Отсортировать записи")
        print("7. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            date, time, text = get_user_input()
            entry = Entry(date, time, text)
            storage.add_entry(entry)
            print("Запись добавлена.")
        elif choice == '2':
            entries = storage.get_all_entries()
            display_entries(entries)
        elif choice == '3':
            storage.save_to_file(filename)
            print("Записи сохранены в файл.")
        elif choice == '4':
            try:
                storage.load_from_file(filename)
                print("Записи загружены из файла.")
            except Exception as e:
                print(f"Произошла ошибка при загрузке записей: {e}")
        elif choice == '5':
            search_term = input("Введите дату (ГГГГ-ММ-ДД) или текст для поиска: ")
            found_entries = storage.search_entries(search_term)
            if found_entries:
                display_entries(found_entries)
            else:
                print("Записи не найдены.")
        elif choice == '6':
            storage.sort_entries()
            print("Записи отсортированы.")
        elif choice == '7':
            break
        else:
            print("Неправильный выбор, попробуйте снова.")

if __name__ == '__main__':
    main()
