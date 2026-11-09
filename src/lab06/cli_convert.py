import json
import argparse
import sys
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="command")

    p1 = sub.add_parser("json2csv", help="Преобразует JSON в CSV", description="Преобразует JSON в CSV")
    p1.add_argument("--in", required=True, dest="input", help="Входной JSON")
    p1.add_argument("--out", required=True, dest="output", help="Выходной CSV")

    p2 = sub.add_parser("csv2json", help="Преобразует CSV в JSON", description="Преобразует CSV в JSON")
    p2.add_argument("--in", required=True, dest="input", help="Входной CSV")
    p2.add_argument("--out", required=True, dest="output", help="Выходной JSON")

    p3 = sub.add_parser("csv2xlsx", help="Преобразует CSV в XLSX", description="Преобразует CSV в XLSX")
    p3.add_argument("--in", required=True, dest="input", help="Входной CSV")
    p3.add_argument("--out", required=True, dest="output", help="Выходной XLSX")

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)
    except FileNotFoundError:
        print(f"Входной файл не найден: {args.input}", file = sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Некорректный JSON", file = sys.stderr)
        sys.exit(1)
    except ValueError as error:
        print(f"Ошибка: {error}", file = sys.stderr)
        sys.exit(1)

if __name__=="__main__":
    main()