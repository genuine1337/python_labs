import csv
from pathlib import Path
from typing import Iterable, Sequence


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    '''
    Открывает файл на чтение и возвращает содержимое как одну строку.
    Кодировка по умолчанию UTF-8, чтобы выбрать другую, её нужно передать в параметр функции (пример: encoding = "cp1251").
    Если файл не найден - FileNotFoundError.
    Если неподходящая кодировка - UnicodeDecodeError.
    '''
    p = Path(path)
    return p.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    '''
    Создаёт родительские директории, если таковые отсутствуют.
    '''
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)


def write_csv(rows: Iterable[Sequence], path: str | Path, 
              header: tuple[str, ...] | None = None) -> None:
    '''
    Создаёт/перезаписывает CSV с разделителем ",".
    Если передан header, то он будет записан первой строкой.
    Проверяется, что все строки в rows одинаковой длины, иначе raise ValueError.
    '''
    p = Path(path)
    rows = list(rows)

    lens = {len(r) for r in rows}
    if header is not None:
        lens.add(len(header))
    if len(lens) > 1:
        raise ValueError("Все строки должны быть одинаковой длины")

    ensure_parent_dir(path)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)


txt = read_text("data/lab04/input.txt")  # должен вернуть строку
print(txt)
write_csv([("word","count"),("test",3)], "data/check.csv")  # создаст CSV
