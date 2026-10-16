# Sum of resistors in series

n = int(input("How many resistors? "))

total = 0

for i in range(1, n + 1):
    r = float(input("Enter R" + str(i) + ": "))
    total += r

print("Total resistance =", total, "ohm")