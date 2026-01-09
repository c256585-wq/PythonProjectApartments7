def validate_database(database):
    try:
        if database is None:
            print("Ошибка: база данных отсутствует ИЛИ неверный синтаксис данных (программа не считывает буквы без кавычек)")
            return False

        if not isinstance(database, list):
            print("Ошибка: база данных имеет неверный тип.")
            return False

        if not database:
            print("Ошибка: база данных пуста.")
            return False

        if len(database) < 25:
            print("Ошибка: в базе данных менее 25 записей "f"({len(database)}).")
            return False

        for record in database: # Здесь проверяем КАЖДЫЙ из 11 индексов в строке
            if not isinstance(record, list):
            # Функция isinstance используется для проверки принадлежности объекта к определённому типу данных.
            # В программе она применяется для валидации структуры и типов полей базы данных
                print("Ошибка: обнаружена некорректная запись.")
                return False

            if len(record) != 11:
                print("Ошибка: запись имеет неверное количество полей.")
                return False

            if not all(isinstance(record[i], str) for i in range(4)):
                print("Ошибка: строковые поля (ФИО или улица) заданы неверно.")
                return False

            if not all(isinstance(record[i], int) for i in (4, 5, 6, 9)):
                print(
                    "Ошибка: числовые поля "
                    "(дом, квартира, этаж или прописанные) заданы неверно."
                )
                return False

            if not all(isinstance(record[i], (int, float)) for i in (7, 8)):
                print("Ошибка: поля площади должны быть числами.")
                return False

            if not isinstance(record[10], bool):
                print("Ошибка: поле наличия льготы задано неверно.")
                return False

            if record[4] <= 0 or record[5] <= 0 or record[6] <= 0:
                print("Ошибка: значения дома, квартиры и этажа должны быть положительными.")
                return False

            if record[9] < 0:
                print("Ошибка: количество прописанных не может быть отрицательным.")
                return False

            if record[7] <= 0 or record[8] <= 0:
                print("Ошибка: площади должны быть больше нуля.")
                return False

            if record[8] > record[7]:
                print("Ошибка: жилая площадь не может превышать общую.")
                return False

    except Exception:
        print("Ошибка: некорректная структура базы данных.")
        return False

    return True