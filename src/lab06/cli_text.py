import argparse
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lib.io_helpers import read_text

def read_input(path: str) -> str:
    '''
    Читает текстовый файл в UTF-8 и возвращает его содержимое.
    Если файл не найден или не в UTF-8 - выводится сообщение об ошибке через stderr
    и завершает программу с кодом 1.
    '''
    try:
        return read_text(path)
    except FileNotFoundError:
        print(f"Входной файл не найден: {path}", file=sys.stderr)
        sys.exit(1)
    except UnicodeEncodeError:
        print(f"Не удалось прочитать входной файл {path} в UTF-8", file=sys.stderr)
        sys.exit(1)

def sub_cat(args: argparse.Namespace) -> None:
    '''
    Подкоманда cat выводит содержимое файла построчно.
    Если указан флаг -n, то перед каждой строкой указан её номер.
    '''
    text = read_input(args.input)
    lines = text.splitlines()
    for number, line in enumerate(lines, start=1):
        if args.n:
            print(f"{number}: {line}")
        else:
            print(f"{line}")

def sub_stats(args: argparse.Namespace) -> None:
    '''
    Подкоманда stats считает частоты слов в файле,
    возвращает общее число слов, число уникальных слов и топ слов.
    '''
    text = read_input(args.input)

    norm = normalize(text)
    tokens = tokenize(norm)
    freq = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{args.top}:")
    for word, count in top_n(freq, n=args.top):
        print(f"{word}: {count}")

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest= "command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла построчно")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в входном файле")
    stats_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топовых слов (5 по умолчанию)")

    args = parser.parse_args()

    if args.command == "cat":
        sub_cat(args)
    elif args.command == "stats":
        sub_stats(args)

if __name__=="__main__":
    main()