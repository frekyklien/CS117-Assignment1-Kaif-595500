# Checking tolerance of resistors and dividing them into 1% or 5% or invalid catagory

count_1 = 0
count_5 = 0
count_reject = 0

while True:
    value = float(input("Enter resistance (0 to stop): "))

    if value == 0:
        break

    if 99.0 <= value <= 101.0:
        count_1 += 1
    elif 95.0 <= value <= 105.0:
        count_5 += 1
    else:
        count_reject = count_reject + 1

print("1% tolerance:", count_1)
print("5% tolerance:", count_5)
print("Reject:", count_reject)