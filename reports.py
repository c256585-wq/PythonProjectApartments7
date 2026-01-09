from sort_utils import shell_sort

def print_records(records):
    if not records:
        print("Записей не найдено.")
        return

    for r in records: # r от 0 до 10 (от фамилии до наличия льгот)
        print(
            f"{r[0]} {r[1]} {r[2]}, "
            f"ул. {r[3]}, д.{r[4]}, кв.{r[5]}, "
            f"этаж {r[6]}, "
            f"общ. {r[7]} м², жил. {r[8]} м², "
            f"прописано {r[9]}, "
            f"льгота: {'Да' if r[10] else 'Нет'}"
        )


def report_all_sorted(database):
    data = database[:] # создаётся копия списка

    def compare(a, b):
    # функция сравнения, которая принимает две записи, возвращает True, если:
    # a должно идти ПОСЛЕ b
    # Алгоритм Шелла использует её, чтобы понимать, нужно ли менять элементы местами
        if a[9] != b[9]:
            return a[9] < b[9]
        return (a[3], a[4], a[5]) > (b[3], b[4], b[5])

    shell_sort(data, compare)
    # Вызывает функцию сортировки методом Шелла и изменяет список data на месте
    print_records(data)
    # Получает уже отсортированный список

def report_with_benefits(database):
    data = [r for r in database if r[10]]

    def compare(a, b):
        if a[6] != b[6]:
            return a[6] > b[6]
        if a[9] != b[9]:
            return a[9] < b[9]
        return a[7] > b[7]

    shell_sort(data, compare)
    print_records(data) # см. пояснение выше


def report_by_area(database):
    try:
        n1 = float(input("Введите N1: "))
        n2 = float(input("Введите N2: "))
    except ValueError:
        print("Ошибка ввода.")
        return

    if n1 > n2:
        print("N1 не может быть больше N2.")
        return
    else:
        print()
        print("Вот отчёт о квартирах с общей площадью в диапазоне от N1 до N2 кв.м., которые отсортированы по КЛЮЧУ:")
        print("наличие льготы (по возрастанию) + общая площадь (по убыванию)")

    data = [r for r in database if n1 <= r[7] <= n2]

    def compare(a, b):
        # см. пояснение выше
        if a[10] != b[10]:
            return a[10] > b[10]
        return a[7] < b[7]

    shell_sort(data, compare)
    print_records(data) # см. пояснение выше