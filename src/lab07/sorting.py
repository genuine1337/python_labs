def bubble_sort(nums) -> list[int]:
    """
    Новый список, отсортированный по возрастанию.
    Исходный список не меняется.
    Пузырьковый метод.
    """
    new = nums.copy()
    for i in range(len(new)):
        swap = False
        for j in range(len(new) - i - 1):
            if new[j] > new[j+1]:
                new[j], new[j+1] = new[j+1], new[j]
                swap = True
        if not swap:
            break
    return new


def insertion_sort(nums) -> list[int]:
    """
    Новый список, отсортированный по возрастанию.
    Исходный список не меняется.
    Вставочный метод.
    """
    new = nums.copy()
    for i in range(1, len(new)):
        j = i - 1
        a = new[i]
        while j >= 0 and new[j] > a:
            new[j+1] = new[j]
            j -= 1
        new[j+1] = a
    return new

def selection_sort(nums) -> list[int]:
    """
    Новый список, отсортированный по возрастанию.
    Исходный список не меняется.
    Выборочный метод.
    """
    new = nums.copy()
    for i in range(len(new)):
        k1 = i
        for j in range(k1 + 1, len(new)):
            if new[j] < new[k1]:
                k1 = j
        new[i], new[k1] = new[k1], new[i]
    return new
