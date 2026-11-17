import math


def calc_area(side_length):
    area = (math.sqrt(3) / 4) * (side_length**2)
    print(f"The area of the triangle is {area}")
    return float(area)