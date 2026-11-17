import math

def estimate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

def take_square(x):
    return x**2

print("Derivative (def):", estimate_derivative(take_square, 3))
print("Derivative (lambda):", estimate_derivative(lambda x: x**2, 3))

def integrate(func, steps=1000):
    total_area = 0.0
    delta_x = 1.0 / steps
    for i in range(steps):
        x = (i + 0.5) * delta_x
        total_area += func(x) * delta_x
    return total_area

print("Integral of x^2 on [0, 1]:", integrate(take_square))

def f_x_twice(x, f_x):
    return f_x(f_x(x))

print("f_x_twice sqrt:", f_x_twice(16, math.sqrt))
print("f_x_twice square:", f_x_twice(2, lambda x: x**2))