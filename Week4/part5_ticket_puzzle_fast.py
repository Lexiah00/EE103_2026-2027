import time

start_time = time.time()

for A in range(1001):
    B = A - 20
    C = 2 * A
    if A + B + C == 1000:
        print(f"Alyssa sold: {A} tickets")
        break
end_time = time.time()
print(f"Execution time: {end_time - start_time: .6f} seconds")