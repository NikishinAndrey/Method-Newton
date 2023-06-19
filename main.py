import matplotlib.pyplot as plt
import numpy as np

##---------------------------input data-------------------------------##
a = -3.00  ##  left border
b = 3.00  ##  right border


def func_1(x):
    return 2 * np.cos(x)


def func_2(x):
    return x ** 3 - np.sign(x) * x ** 2 + 6 * x + 3


##----------------------------start program--------------------------##
def massive(left, right, node, func):
    #  Chebyshev's grid
    grid_x = [0.0 for _ in range(node)]
    grid_y = [0.0 for _ in range(node)]
    counter = node - 1
    for k in range(node):
        grid_x[counter] = (left + right) / 2 + (right - left) * np.cos(np.pi * (2 * k + 1) / (2 * node + 2)) / 2
        counter -= 1
    for i in range(node):
        grid_y[i] = func(grid_x[i])
    return grid_x, grid_y


def separated_differences(mas_y, mas_x):
    length = len(mas_x)
    s_d_mas = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(length):
        s_d_mas[0][i] = mas_y[i]
    for j in range(1, length):
        for k in range(length - j):
            s_d_mas[j][k] = ((s_d_mas[j - 1][k + 1] - s_d_mas[j - 1][k]) / (mas_x[k + j] - mas_x[k]))
    return s_d_mas


def massive_middle(func, mas_x):
    length = len(mas_x) - 1
    mas_mid = [0 for _ in range(length)]
    for j in range(length):
        mas_mid[j] = (mas_x[j + 1] - mas_x[j]) / 2 + mas_x[j]
    mas_f = [0 for _ in range(length)]
    for i in range(length):
        mas_f[i] = func(mas_mid[i])
    return mas_mid, mas_f


def poly(mas_f, mas_x, mas_mid):
    length = len(mas_f)
    mas_1 = [0 for _ in range(length)]
    mas_2 = [0 for _ in range(length - 1)]
    multi = 1
    for i in range(length):
        for j in range(length):
            for k in range(j):
                multi *= mas_x[i] - mas_x[k]
            mas_1[i] += mas_f[j][0] * multi
            multi = 1
    for i in range(length - 1):
        for j in range(length - 1):
            for k in range(j):
                multi *= mas_mid[i] - mas_x[k]
            mas_2[i] += mas_f[j][0] * multi
            multi = 1
    return mas_1, mas_2


##----------------------------first and second graph----------------------------##
def graph_1_2(func, node):
    result = massive(a, b, node, func)
    n_m = result[0]
    n_m_ = result[1]
    m_m = massive_middle(func, n_m)[0]
    res_ = separated_differences(n_m_, n_m)
    final = poly(res_, n_m, m_m)[0]
    return n_m, final


res_graph_1_5 = graph_1_2(func_1, 5)
res_graph_2_5 = graph_1_2(func_2, 5)
res_graph_1_20 = graph_1_2(func_1, 20)
res_graph_2_20 = graph_1_2(func_2, 20)

plt.figure(1)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("График №1")
x1 = np.linspace(a, b, 1000)
y1 = 2 * np.cos(x1)
plt.plot(x1, y1, label='2cos(x)')
plt.plot(res_graph_1_5[0], res_graph_1_5[1], 'y--', res_graph_1_5[0], res_graph_1_5[1], 'k.',
         label='апроксимация: 5 узлов')
plt.plot(res_graph_1_20[0], res_graph_1_20[1], 'r-.', res_graph_1_20[0], res_graph_1_20[1], 'kx',
         label='апроксимация: 20 узлов')
plt.legend()

plt.figure(2)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("График №2")
x2 = np.linspace(a, b, 1000)
y2 = x2 ** 3 - np.sign(x2) * x2 ** 2 + 6 * x2 + 3
plt.plot(x2, y2, 'k', label='x^3 - sign(x)x^2 + 6x + 3')
plt.plot(res_graph_2_5[0], res_graph_2_5[1], 'y--', res_graph_2_5[0], res_graph_2_5[1], 'k.',
         label='апроксимация функции: 5 узлов')
plt.plot(res_graph_2_20[0], res_graph_2_20[1], 'r-.', res_graph_2_20[0], res_graph_2_20[1], 'kx',
         label='апроксимация функции: 20 узлов')
plt.legend()


##----------------------------third and fourth graph----------------------------##
def error(func, node):
    result = massive(a, b, node, func)
    n_m = result[0]
    n_m_ = result[1]
    res = massive_middle(func, n_m)
    m_m = res[0]
    m_m_f = res[1]
    lenght = len(m_m_f)
    rr = separated_differences(n_m_, n_m)
    final = poly(rr, n_m, m_m)
    graph_3 = final[1]
    mass = [0 for _ in range(lenght)]
    for j in range(lenght):
        mass[j] = abs(graph_3[j] - m_m_f[j])
    final_res = max(mass)
    return final_res


def graph_3_4(func, node):
    massive_node = [0 for _ in range(node)]
    for j in range(node):
        massive_node[j] = j + 5
    massive_error = [0 for _ in range(node)]
    for k in range(node):
        massive_error[k] = error(func, k + 5)
    return massive_node, massive_error


res_graph_3 = graph_3_4(func_1, 45)
res_graph_4 = graph_3_4(func_2, 45)
res_graph_7 = graph_3_4(func_1, 95)
res_graph_8 = graph_3_4(func_2, 95)

plt.figure(3)
plt.grid()
plt.xlabel('количество узлов')
plt.ylabel('абсолютная погрешность')
plt.title("График №3")
plt.plot(res_graph_3[0], res_graph_3[1], 'm-.', label='2cos(x)')
plt.legend()

plt.figure(4)
plt.grid()
plt.xlabel('количество узлов')
plt.ylabel('абсолютная погрешность')
plt.title("График №4")
plt.plot(res_graph_4[0], res_graph_4[1], 'g-', label='x^3 - sign(x)x^2 + 6x + 3')
plt.legend()


##----------------------------fifth and sixth graph----------------------------##
def thick_grid(left, right, node, func):
    mas_grid = [0 for _ in range(2 * node + 1)]
    mas_grid[0] = left
    mas_grid[node] = (left + right) / 2
    mas_grid[2 * node] = right
    grid_y = [0 for i in range(2*node + 1)]
    for j in range(1, node):
        mas_grid[j] = mas_grid[j - 1] / 2
    for k in range(2 * node - 1, node, -1):
        mas_grid[k] = mas_grid[k + 1] / 2
    for i in range(2 * node + 1):
        grid_y[i] = func(mas_grid[i])
    return mas_grid, grid_y


def graph_5_6(func, node):
    result = thick_grid(a, b, node, func)
    n_m = result[0]
    n_m_ = result[1]
    m_m = massive_middle(func, n_m)[0]
    res_ = separated_differences(n_m_, n_m)
    final = poly(res_, n_m, m_m)[0]
    return n_m, final


res_graph_5 = graph_5_6(func_1, 8)
res_graph_6 = graph_5_6(func_2, 8)

plt.figure(5)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("График №5")
x1 = np.linspace(a, b, 1000)
y1 = 2 * np.cos(x1)
plt.plot(x1, y1, 'y', label='2cos(x)')
plt.plot(res_graph_5[0], res_graph_5[1], 'r--', res_graph_5[0], res_graph_5[1], 'k.', label='апроксимация функции')
plt.legend()

plt.figure(6)
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.title("График №6")
x2 = np.linspace(a, b, 1000)
y2 = x2 ** 3 - np.sign(x2) * x2 ** 2 + 6 * x2 + 3
plt.plot(x2, y2, 'r', label='x^3 - sign(x)x^2 + 6x + 3')
plt.plot(res_graph_6[0], res_graph_6[1], 'b--', res_graph_6[0], res_graph_6[1], 'k.', label='апроксимация функции')
plt.legend()

# ------------------------------extra work-----------------------------
plt.figure(7)
plt.grid()
plt.xlabel('количество узлов')
plt.ylabel('абсолютная погрешность')
plt.title("График №7")
plt.plot(res_graph_7[0], res_graph_7[1], 'm-.', label='2cos(x)')
plt.legend()

plt.figure(8)
plt.grid()
plt.xlabel('количество узлов')
plt.ylabel('абсолютная погрешность')
plt.title("График №8")
plt.plot(res_graph_8[0], res_graph_8[1], 'g-', label='x^3 - sign(x)x^2 + 6x + 3')
plt.legend()
plt.show()
