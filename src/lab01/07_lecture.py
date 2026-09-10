s = input("in: ")
first_letter_index = 0
delta = 0

for num, char in enumerate(s):
    if char.isupper():
        first_letter_index = num
        break

digits = '0123456789'

s2 = s[first_letter_index::]
for num, char in enumerate(s2):
    if char in digits:
        delta = num + 1
        break

s3 = [i for i in s[first_letter_index::delta]]

s_out = ""
for j in s3:
    if j != ".":
        s_out += j
    else:
        break

print(f"out: {s_out}.")