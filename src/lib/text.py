import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    '''
    заменяет все ё/Ё на е/Е, если yo2e = True
    заменяет управляющие символы \t, \r, \n на пробел
    заменяет несколько пробелов, стоящих подряд, на один пробел
    если casefold = True, то строка приводится к casefold, иначе - с помощью lower()
    '''
    text_new = " ".join(text.split()) #здесь же replace("\t", " ").replace("\r", " ").replace("\n", " ")

    if yo2e:
        text_new = text_new.replace("ё", "е").replace("Ё", "Е")
    
    if casefold:
        text_new = text_new.casefold()
    else:
        text_new = text_new.lower()

    return text_new


def tokenize(text: str) -> list[str]:
    '''
    разбивает строку на "слова" по небуквенно-цифровым разделителям,
    в т.ч. числа (2025 - слово) и слова с дефисом внутри (ярко-синий - слово)
    эмодзи не являются "словами"
    '''
    new_text = normalize(text)
    tokens = re.findall(r"\w+(?:-\w+)*", new_text)
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:
    '''
    считает частоту токенов в введённом списке,
    возвращает словарь, где ключом является сам токен, а значением - частоту токенов
    при равенстве частот сортировка по алфавитному порядку
    '''
    frequency = {}

    for token in tokens:
        frequency[token] = frequency.get(token, 0) + 1
    
    return dict(sorted(frequency.items()))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    возвращает список из топ-N токенов по убыванию частоты,
    при равенстве частот сортировка по алфавиту
    """
    sorted_pairs = sorted(freq.items(), key = lambda pair: (-pair[1], pair[0]))
    return sorted_pairs[:n]
