from convertor import binary_convertor
from say_hello import say_my_name
from triangle_area import calc_area

# 1. Hello fonksiyonu
my_name = "Yusuf"
say_my_name(my_name)

# 2. Üçgen alanı
side = 5
calc_area(side)

# 3. İkili taban dönüşümü
number = 13
binary_result = binary_convertor(number)
print(f"Binary representation of {number} is {binary_result}")