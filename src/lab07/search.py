def linear_search(nums, x) -> int:
    """
    Линейный поиск числа x в списке nums. Возвращаем индекс первого элемента, равного x.
    Если такой элемент отсутствует, возвращаем -1.
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1

def binary_search(sorted_nums, x) -> int:
    """
    Возвращаем индекса любого элемента в списке sorted_nums, равного x.
    Если такой элемент отсутствует, возвращаем -1.
    Список должен быть изначально отсортирован.
    На неотсортированном списке результат не определён.
    """
    lo = 0
    hi = len(sorted_nums) - 1
    while lo <= hi:
        mid = (hi+lo) // 2
        if sorted_nums[mid] == x: return mid
        elif sorted_nums[mid] < x: lo = mid + 1
        else: hi = mid - 1
    return -1

def two_sum_brute(nums, target) -> tuple[int, int] | None:
    """
    Ищем два индекса (i, j) таких, что nums[i] + nums[j] == target и i < j.
    Возвращаем tuple(i, j) при наличии такой пары, иначе None.
    Поиск двойным проходом по списку.
    """
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target) -> tuple[int, int] | None:
    """
    Ищем два индекса (i, j) таких, что nums[i] + nums[j] == target и i < j.
    Возвращаем tuple(i, j) при наличии такой пары, иначе None.
    Поиск через словарь.
    """
    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            return (seen[nums[i]], i)
        else:
            seen[target - nums[i]] = i
    return None


