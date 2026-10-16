# Finding output of logic gates (AND, OR, XOR)

a = int(input("Enter A: "))
b = int(input("Enter B: "))

if a not in (0, 1) or b not in (0, 1):
    print("Bits must be 0 or 1")
else:
    if (a == 1 and b == 1):
        And = 1
    else:
        And = 0

    if (a == 1 or b == 1):
        Or = 1
    else:
        Or = 0

    if (a != b):
        Xor = 1
    else:
        Xor = 0

    print("AND =", And)
    print("OR  =", Or)
    print("XOR =", Xor)