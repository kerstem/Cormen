import pytest
import random
from core.sort import (
    bubble_sort
)

# Фиксируем seed для воспроизводимости тестов
random.seed(42)


# 1. Создаем 100 тестовых случаев
def generate_test_cases():
    test_cases = []

    # Граничные случаи (10%)
    test_cases.extend([
        [],
        [1],
        [0],
        [-5],
        [1, 1, 1, 1],
        [3, 1, 4, 1, 5, 9, 2, 6],
        [-3, 1, -2, 4],
        [1.5, 0.5, 3.2],
        ['banana', 'apple', 'cherry']
    ])

    # Уже отсортированные массивы (10%)
    for _ in range(10):
        size = random.randint(0, 50)
        arr = sorted([random.randint(-100, 100) for _ in range(size)])
        test_cases.append(arr)

    # Обратно отсортированные массивы (10%)
    for _ in range(10):
        size = random.randint(0, 50)
        arr = sorted([random.randint(-100, 100) for _ in range(size)], reverse=True)
        test_cases.append(arr)

    # Случайные массивы (70%)
    for _ in range(70):
        size = random.randint(0, 100)
        arr = [random.randint(-1000, 1000) for _ in range(size)]
        test_cases.append(arr)

    return test_cases


# 2. Получаем тестовые данные
TEST_CASES = generate_test_cases()

# 3. Регистрируем все алгоритмы для тестирования
ALGORITHMS = [
    bubble_sort
]


# 4. Параметризованный тест
@pytest.mark.parametrize('algorithm', ALGORITHMS, ids=[a.__name__ for a in ALGORITHMS])
@pytest.mark.parametrize('test_input', TEST_CASES, ids=lambda x: f"size:{len(x)}")
def test_sorting_algorithm(algorithm: callable, test_input):
    """Тестирует алгоритм сортировки на одном наборе данных"""
    # Ожидаемый результат
    expected = sorted(test_input)

    # Запускаем алгоритм на копии данных
    result = algorithm(test_input.copy())

    # Проверяем результат
    assert result == expected
