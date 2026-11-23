import random
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> None:
    """
    Проверяет функцию сортировки fn против эталонного sorted() на случайных списках.
    """
    for i in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for i in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"

def check_search(fn, trials: int = 100) -> None:
    """
    Проверяет функцию fn на поиск индекса на случайных списках.
    """
    if fn == "linear_search":
        for i in range(trials):
            n = random.randint(0, 50)
            nums = [random.randint(-100, 100) for i in range(n)]
            original = list(nums)
            result = fn(nums)
            assert result == nums.index(), f"{fn.__name__} ошиблась на {nums}: {result}"
            assert nums == original, f"{fn.__name__} изменила исходный список"

    elif fn == "binary_search":
        for i in range(trials):
            n = random.randint(0, 50)
            nums = sorted([random.randint(-100, 100) for i in range(n)])
            original = list(nums)
            result = fn(nums)
            assert result == nums.index(), f"{fn.__name__} ошиблась на {nums}: {result}"
            assert nums == original, f"{fn.__name__} изменила исходный список"


def check_two_sum(trials: int = 100):
    """
    Проверяет two_sum_brute и two_sum_fast на правильность поиска индексов (i, j); i < j, при отсутствии - None.
    """
    for i in range(trials):
        n = random.randint(0, 50)
        nums = sorted([random.randint(-100, 100) for i in range(n)])
        target = random.randint(-50, 50)
        res_brute = two_sum_brute(nums, target)
        res_fast = two_sum_fast(nums, target)
        if res_brute is None or res_fast is None:
            continue
        else:
            assert nums[res_brute[0]] + nums[res_brute[1]] == target, f"Функция two_sum_brute ошиблась на {nums}: {nums[res_brute[0]] + nums[res_brute[1]]} отличается от {target}"
            assert nums[res_fast[0]] + nums[res_fast[1]] == target, f"Функция two_sum_fast ошиблась на {nums}: {nums[res_fast[0]] + nums[res_fast[1]]} отличается от {target}"

if __name__=="__main__":
    random.seed(42)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        amount_sorting = random.randint(50, 100)
        check_sorting(fn, amount_sorting)
        print(f"ОК: функция {fn.__name__} прошла все {amount_sorting} проверок.")

    for fn in (linear_search, binary_search):
        amount_search = random.randint(50, 100)
        check_search(fn, amount_search)
        print(f"ОК: функция {fn.__name__} прошла все {amount_search} проверок.")

    amount_two_sum = random.randint(50, 100)
    check_two_sum(amount_two_sum)
    print(f"ОК: Функции two_sum_brute и two_sum_fast прошли все {amount_two_sum} проверок.")