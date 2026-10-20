target = float(input("Enter a fraction to convert (e.g., 0.1): "))
tolerance = 0.00001

binary_str = "0." 
current_approx = 0.0
f = target
k = 1

while abs(current_approx - target) >= tolerance and k <= 50:
          f *= 2
          bit = int(f)
          binary_str += str(bit)

          if bit == 1:
                  current_approx += 2 ** (-k)

          f -= bit
          k += 1

print(f"Binary result: {binary_str}")
print(f"Approximated float value: {current_approx}")
print(f"Absolute Error: {abs(current_approx - target):.7f}")