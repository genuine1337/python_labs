m = int(input("Минуты: "))
hh = m//60
mm = m - 60*hh
print(f"{hh}:{mm:02d}")