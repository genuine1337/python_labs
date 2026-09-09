a = input("a: ")
b = input("b: ")
a = a.replace(",", ".")
a = float(a)
b = b.replace(",", ".")
b = float(b)

s = a+b
avg = s/2
print(f"sum={s:.2f}; avg={avg:.2f}")