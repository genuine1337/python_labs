type student = tuple[str, str, float]

def format_record(rec: student) -> str:
    """
    На вход подаётся кортеж из строки с ФИО(ФИ),
    строки из названия группы,
    вещественного числа с средним баллом (GPA).
    Возвращается строка вида "Фамилия И.О., группа, GPA"
    Если ФИО состоит только из фамилии или пустое, вернётся ValueError.
    Если группа пустая, вернётся ValueError.
    Если неверный тип GPA, вернётся TypeError
    """
    if not type(rec) is tuple:
        raise TypeError("rec не кортеж")
    if len(rec) != 3:
        raise ValueError("не 3 элемента в кортеже")
    fio, group, gpa = rec
    raw_fio = fio.split()

    if len(raw_fio) <= 1 or group.strip() == "":
        raise ValueError("ФИО менее чем из 2 слов или пустая группа")
    if (not type(gpa) is float) or (not 0.0 <= gpa <= 5.0):
        raise TypeError("Неверное GPA")
    surname = raw_fio[0].capitalize()
    initials = ""
    for i in range(1, len(raw_fio)):
        initials += (f"{raw_fio[i][0].capitalize()}.")
    format_fio = f"{surname} {initials}"
    result = f"{format_fio}, гр. {group}, GPA {gpa:.2f}"
    return result

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999, "г Москва")))
# print(format_record(["  сидорова  анна   сергеевна ", "ABB-01", 3.999]))