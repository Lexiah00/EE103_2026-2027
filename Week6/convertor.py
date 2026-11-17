def binary_convertor(num):
    if num == 0:
        return "0"

    remainders = ""
    temp = num
    while temp > 0:
        rem = temp % 2
        remainders += str(rem)
        temp = temp // 2

    return remainders[::-1]