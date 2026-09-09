fio = input("ФИО: ")
fio_raw = fio.split()
len2 = 2
initials = ""
for i in fio_raw:
    len2 += len(i)
    initials += i[0]
print(f"Инициалы: {initials}.")
print(f"Длина (символов): {len2}")