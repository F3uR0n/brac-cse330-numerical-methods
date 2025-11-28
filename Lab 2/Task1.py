import numpy as np


# Method 1
coeff = [1, 0, 2, 0, 5] # coefficients of the polynomial
n = len(coeff) - 1 # degree. Remember: number of coeff = degree + 1

x = 6.0
p_x = 0.0

for i in range(len(coeff)):
    p_x += coeff[i] * (x ** i)

x_arr = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]
p_x_arr = []

for i in range(len(x_arr)):
    p_x = 0
    for j in range(len(coeff)):
        p_x += coeff[j] * (x_arr[i] ** j)
    p_x_arr.append(p_x)

print(p_x)
print(p_x_arr)

# Method 2

p_x_arr = np.zeros_like(coeff, dtype=float)