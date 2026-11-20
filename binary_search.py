"""Бинарный поиск элемента в отсортированном массиве."""


def binary_search(array: list[int], target: int) -> int:
    """Возвращает индекс target в отсортированном массиве или -1, если его нет.

    Массив должен быть отсортирован по возрастанию.
    При наличии повторяющихся значений функция возвращает одно из вхождений.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == target:
            return middle
        elif array[middle] < target:
            # Искомое значение находится правее середины.
            left = middle + 1
        else:
            # Искомое значение находится левее середины.
            right = middle - 1

    return -1


def is_sorted_ascending(array: list[int]) -> bool:
    """Проверяет, упорядочен ли массив по возрастанию (неубыванию)."""
    return all(array[index] <= array[index + 1] for index in range(len(array) - 1))


def main() -> None:
    print("Бинарный поиск в отсортированном массиве")
    print("Введите целые числа через пробел в порядке возрастания.")

    try:
        array = [int(value) for value in input("Массив: ").split()]
        if not array:
            print("Ошибка: массив не должен быть пустым.")
            return

        if not is_sorted_ascending(array):
            print("Ошибка: массив должен быть отсортирован по возрастанию.")
            return

        target = int(input("Искомое число: "))
    except ValueError:
        print("Ошибка: необходимо вводить целые числа.")
        return

    result = binary_search(array, target)

    if result == -1:
        print(f"Число {target} не найдено. Результат поиска: -1")
    else:
        print(f"Число {target} найдено.")
        print(f"Индекс элемента (нумерация с 0): {result}")
        print(f"Позиция элемента (нумерация с 1): {result + 1}")


if __name__ == "__main__":
    main()
