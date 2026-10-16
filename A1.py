#Finding I & checking fuse


v = float(input("Enter Voltage (V) = "))
r = float(input("Enter Resistance (ohm) = "))

if r <= 0:
    print("Invalid resistance")
else:
    i = v / r
    print("Current: ", i, "A")
    if i > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")