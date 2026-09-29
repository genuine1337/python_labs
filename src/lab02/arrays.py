def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    На вход подаётся список nums из вещественных или целых чисел,
    функция возвращает кортеж из наименьшего и наибольшего чисел из
    входного списка nums.
    Если список пустой, то вернётся ValueError.
    """
    if len(nums) == 0:
        raise ValueError("Пустой список")
    lowest = nums[0]
    biggest = nums[0]
    for num in nums:
        if num > biggest:
            biggest = num
        if num < lowest:
            lowest = num
    return (lowest, biggest)


def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    На вход подаётся список nums из вещественных или целых чисел,
    функция возвращает отсортированный список уникальных чисел в порядке возрастания.
    """
    unique_nums = list(set(nums))
    n = len(unique_nums)
    for i in range(n):
        for j in range(n-i-1):
            if unique_nums[j] > unique_nums[j+1]:
                unique_nums[j], unique_nums[j+1] = unique_nums[j+1], unique_nums[j]
    return unique_nums

def flatten(mat: list[list | tuple]) -> list:
    """
    На вход подаётся список из списков или кортежей mat,
    функция возвращает список, содержащий элементы всех входных списков или кортежей.
    В возвращённом списке элементы расположены в той же последовательности, в которой были переданы в функцию.
    Если какой-либо элемент не является списком или кортежем, то возвращается TypeError.
    """
    check = all([type(i) is tuple or type(i) is list for i in mat])
    if not check:
        raise TypeError("Элемент не является списком или кортежем")
    new_list = []
    for i in mat:
        new_list.extend(i)
    return new_list

# print(min_max([3, -1, 5, 5, 0]))
# print(min_max([42]))
# print(min_max([-5, -2, -9]))
# print(min_max([1.5, 2, 2.0, -3.1]))
# print(min_max([]))

# print(unique_sorted([3, 1, 2, 1, 3]))
# print(unique_sorted([]))
# print(unique_sorted([-1, -1, 0, 2, 2]))
# print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

# print(flatten([[1, 2], [3, 4]]))
# print(flatten([[1, 2], (3, 4, 5)]))
# print(flatten([[1], [], [2, 3]]))
# print(flatten([[1, 2], "ab"]))    