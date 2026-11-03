year_str = input("What year is this? ")
year = int(year_str)

digit_sum = 0
for digit in year_str:
    digit_sum += int(digit)

avg = digit_sum / len(year_str)
print(f"Sum of digits: {digit_sum}")
print(f"Average of digits: {avg}")

x = 0.1
y = 0.2
result = x + y
print(f"result == 0.3: {result == 0.3}")
print(f"Close enough: {0.3 - 1e-4 <= result <= 0.3 + 1e-4}")