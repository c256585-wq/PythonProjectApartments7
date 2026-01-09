try:
    from database import DATABASE # Импорт базы данных
except Exception:
    DATABASE = None

from validators import validate_database # Импорт проверки базы
from reports import (
    report_all_sorted,
    report_with_benefits,
    report_by_area
)                     # Импорт функций каждого отчёта

def main():
    database = DATABASE[:] if isinstance(DATABASE, list) else None

    if not validate_database(database):
        return

    while True:  # Проверка базы перед началом работы
        print("\nМеню:")   # Бесконечный цикл меню
        print()
        print("1 - Полный список квартиросъёмщиков")
        print("2 - Квартиросъёмщики с льготами")
        print("3 - Квартиры по диапазону площади от N1 до N2")
        print("0 - Выход")
        print()

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            print("Вот отчёт о всех квартиросъёмщиках, которые отсортированы по КЛЮЧУ:")
            print(" количество прописанных человек (по убыванию) + адрес (по возрастанию)")
            print()
            report_all_sorted(database)
        elif choice == "2":
            print("Вот отчёт о квартиросъёмщиках имеющих льготы, которые отсортированы по КЛЮЧУ:")
            print(" этаж (по возрастанию) + количество прописанных (по убыванию) + общая площадь (по возрастанию)")
            print()
            report_with_benefits(database)
        elif choice == "3":
            report_by_area(database)
        elif choice == "0":
            print("Программа завершена.")
            break
        else:
            print("Неверный ввод. Повторите попытку.")


if __name__ == "__main__":  # Проверка, что файл запущен напрямую
    main()  # Запуск