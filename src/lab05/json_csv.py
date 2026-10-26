from pathlib import Path
import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    '''
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    '''
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not json_file.suffix.lower() == ".json":
        raise ValueError("Входной файл не .json")
    if not csv_file.suffix.lower() == ".csv":
        raise ValueError("Выходной файл не .csv")

    if not json_file.exists():
        raise FileNotFoundError("Не найден входной JSON")

    with open(json_file, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Некорректный или пустой JSON")

    if (not isinstance(data, list) or not data or not all(isinstance(item, dict) for item in data)):
        raise ValueError("JSON должен содержать непустой список словарей")

    csv_file.parent.mkdir(parents=True, exist_ok=True)

    keys_dict = {}
    for item in data:
        for k in item.keys():
            keys_dict[k] = None
    fieldnames = list(keys_dict.keys())  

    with open(csv_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, restval="")
        writer.writeheader()
        writer.writerows(data)



def csv_to_json(csv_path: str, json_path: str) -> None:
    '''
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    '''
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file.suffix.lower() != ".json":
        raise ValueError("Выходной файл не .json")
    if csv_file.suffix.lower() != ".csv":
        raise ValueError("Входной файл не .csv")

    if not csv_file.exists():
        raise FileNotFoundError("Не найден входной CSV")

    with open(csv_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        data = list(reader)
        if not reader.fieldnames or not data:
            raise ValueError("CSV-файл пуст или не содержит заголовка")
        

    json_file.parent.mkdir(parents=True, exist_ok=True)

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


        
