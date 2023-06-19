# Method-Newton
Approximation of functions using the Newton interpolation polynomial

Given: Some grid 

$$\{x_i\}_{i=0}^n$$ 

and a grid function 

$$\{f_i\}_{i=0}^n$$ 

from a tabulated function for which it is required to construct a Newton polynomial.

In order to find the Newton polynomial, it is necessary to first determine the separated differences through the values of the function $f(x_0), f(x_1), \dots, f(x_n) $. Let 's calculate the separated differences by the formulas:

$$ f(x_0,x_1) = \frac{f(x_1) - f(x_0)}{x_1 - x_0}$$

$$ f(x_1,x_2) = \frac{f(x_2) - f(x_1)}{x_2 - x_1} $$

$$ \dots \ \dots \ \dots \ \dots \ \dots \ \dots $$

$$ f(x_{n-1}, x_n) = \frac{f(x_n) - f(x_{n-1})}{x_n - x_{n-1}}$$

Then the second - order differences will be found by:

$$ f(x_0,x_1,x_2) = \frac{f(x_1,x_2) - f(x_0,x_1)}{x_2 - x_0}$$

$$ \dots \ \dots \ \dots \ \dots \ \dots \ \dots \ \dots \ \dots $$

$$ f(x_{n-2},x_{n-1},x_n) = \frac{f(x_{n-1},x_n) - f(x_{n-2},x_{n-1})}{x_n - x_{n-2}} $$

$$ f(x_{i-1}, x_i, \dots, x_{i+k}) = \frac{f(x_i, x_{i+1}, \dots, x_{i+k}) - f(x_{i-1}, x_i, \dots, x_{i+k-1})}{x_{i+k} - x_{i-1}}$$

Then the Newton polynomial is calculated by:

$$ P_n(x) = f(x_0) + f(x_0, x_1)(x - x_0) + f(x_0,x_1,x_2)(x-x_0)(x-x_1) + \dots + f(x_0,x_1,x_2, \dots , x_n)(x-x_0)(x-x_1) \dots (x-x_{n-1}) $$

It remains only to substitute the grid values into the Newton polynomial and get the desired result.

![image](https://github.com/NikishinAndrey/Method-Newton/assets/113716137/6bb03979-573e-481a-9a9e-b9a003cdecf1)

![image](https://github.com/NikishinAndrey/Method-Newton/assets/113716137/0a310566-7660-4781-b332-da5a267a0271)

![image](https://github.com/NikishinAndrey/Method-Newton/assets/113716137/e72a248c-d79d-49f4-bf41-03d4dd45efc6)

![image](https://github.com/NikishinAndrey/Method-Newton/assets/113716137/8e0879d1-5d87-4b18-b2bb-9e794c0371ee)

![image](https://github.com/NikishinAndrey/Method-Newton/assets/113716137/60ed4680-f635-4722-9570-122bfaaa8321)

![image](https://github.com/NikishinAndrey/Method-Newton/assets/113716137/56615803-6aba-4058-9654-d10e7b5629b1)
