# Finds longest interval of voltage drop along with time taken for the voltage drop.

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0,
            11.8, 11.6, 11.5, 11.5, 11.2]

longest = 1
best_start = voltages[0]
best_end = voltages[0]

current_len = 1
start_val = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        current_len = current_len + 1
        if current_len > longest:
            longest = current_len
            best_start = start_val
            best_end = voltages[i]
    else:
        current_len = 1
        start_val = voltages[i]

print("Longest continuous drop:", longest, "minutes")
print("Started at:", best_start, "V")
print("Ended at:", best_end, "V")