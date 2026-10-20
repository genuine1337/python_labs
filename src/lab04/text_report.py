import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    try:
        raw_text = read_text("data/lab04/input.txt", encoding="utf-8")
    except FileNotFoundError:
        print("Файл не найден")
        return
    
    normal = normalize(raw_text)
    tokens = tokenize(normal)
    unique_tokens = count_freq(tokens)
    top_5 = top_n(unique_tokens, n=5)
    all_rows = sorted(unique_tokens.items(), key= lambda x: (-x[1], x[0]))

    write_csv(all_rows, "data/lab04/report.csv", header= ("word", "count"))
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(unique_tokens)}")
    print(f"Топ-5:")
    for n in top_5:
        print(f"{n[0]}: {n[1]}")

if __name__ == "__main__":
    main()
    
    