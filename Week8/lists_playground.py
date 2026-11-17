total = 0
dummy_range = range(10)
dummy_list_1 = list(dummy_range)

dummy_list_2 = []
for i in range(10):
    dummy_list_2.append(i)

print("Lists equal: ", dummy_list_1 == dummy_list_2)

for num in dummy_list_1:
    total += num
print("Total sum: ", total)

dummy_list = [x**2 for x in range(10)]
for index, value in enumerate(dummy_list):
    print(f"Index: {index}, Value: {value}")

def lenght_and_square(L):
    length = len(L)
    squares = [x**2 for x in L]
    return length, squares

print(lenght_and_square([1, 3, 5, 9568]))