# Finding R_eq in parallel

def parallel_resistance(resistors):
    inv_total = 0
    for r in resistors:
        inv_total = inv_total + (1 / r)
    return 1 / inv_total

print(parallel_resistance([10, 10]))
print(parallel_resistance([100, 200, 300]))