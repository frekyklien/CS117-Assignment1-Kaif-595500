#Finding smallest & largest of resistance among given resistors 

r1 = float(input("Enter R1: "))
r2 = float(input("Enter R2: "))
r3 = float(input("Enter R3: "))


if r1 <= r2 and r1 <= r3:
    small = r1
elif r2 <= r1 and r2 <= r3:
    small = r2
else:
    small = r3


if r1 >= r2 and r1 >= r3:
    large = r1
elif r2 >= r1 and r2 >= r3:
    large = r2
else:
    large = r3

print("Smallest =", small, "ohms")
print("Largest =", large, "ohms")