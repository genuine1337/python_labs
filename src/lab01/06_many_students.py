n = int(input("in_1: "))
irl = 0
virtual = 0
#print(f"in_{a}: ")
for a in range(2, n+2):
    b = input(f"in_{a}: ").split()
    c = b[-1]
    if c == "True":
        irl += 1
    else:
        virtual += 1
print(f"out: {irl} {virtual}")


    
    

