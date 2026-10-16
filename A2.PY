# Current direction

I = float(input("Enter current (A): "))

if I > 0:
    print("Current flows from A to B")
elif I < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
