# Converting decimal positive numbers into binary string

def decimal_to_binary(n):
    if n == 0:
        return "0"
    bits = ""
    while n > 0:
        remainder = n % 2
        bits = str(remainder) + bits    # prepend
        n = n // 2
    return bits

print(decimal_to_binary(10))
print(decimal_to_binary(25))