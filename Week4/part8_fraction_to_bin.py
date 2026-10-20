f = float(input("Enter a fraction between 0 and 1 (e.g., 0.375): "))

binary_str = "0."
precision = 20

while f > 0 and (len(binary_str) - 2) < precision:
    f *= 2
    bit = int(f)
    binary_str += str(bit)
    f -= bit
print(f"Binary representation: {binary_str}")