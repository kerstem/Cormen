def bubble_sort(array: list) -> list:
    """
    Сортировка пузырьком (bubble sort)
    Временная сложность: O(n^2)
    Пространственная сложность: O(1)
    :param array: входной массив
    :return: отсортированный массив
    """
    n: int = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array