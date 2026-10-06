import sys
import os

src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, src_path)

from lib.text import normalize, tokenize, count_freq, top_n

text = sys.stdin.read()
if text.strip() == "":
    raise ValueError("Введите непустую строку")

new_text = normalize(text)
tokens = tokenize(new_text)
frequencies = count_freq(tokens)
top_tokens = top_n(frequencies)

aligned_table = False

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(frequencies)}")
print("Топ-5:")

if not aligned_table:
    for i in top_tokens:
        print(f"{i[0]}:{i[1]}")

if aligned_table:
    max_word_len = max(len(word) for word, i in top_tokens)
    freq_width = len("частота")
    print(f"{'слово':<{max_word_len}} | {'частота'}")
    print(f"{"-" * max_word_len}-{"-" * freq_width}")
    for word, count in top_tokens:
        print(f"{word:<{max_word_len}} | {count}")
