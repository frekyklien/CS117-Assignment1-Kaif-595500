# Reading the sensor values to get answers for (a), (b), (c), (d)

readings = [3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2]

above = 0
highest = readings[0]
lowest = readings[0]
total = 0

for v in readings:
    if v > 3.2:
        above = above + 1
    if v > highest:
        highest = v
    if v < lowest:
        lowest = v
    total = total + v

average = total / len(readings)

print("Readings above 3.2 V:", above)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", round(average, 2), "V")