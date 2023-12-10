import matplotlib.pyplot as plt


def diff_quotient(x_k_minus_1, x_k, x_k_plus_1, list_y, k):
    f12 = (list_y[k + 1] - list_y[k]) / (x_k_plus_1 - x_k)
    f01 = (list_y[k] - list_y[k - 1]) / (x_k - x_k_minus_1)
    return (f12 - f01) / (x_k_plus_1 - x_k_minus_1)


def calculate_d(x_k_minus_1, x_k, x_k_plus_1, list_y, k):
    return 6 * diff_quotient(x_k_minus_1, x_k, x_k_plus_1, list_y, k)


def all_d(list_x, list_y):
    list_d = [1 for _ in range(len(list_x))]
    for k in range(len(list_x) - 1):
        d = calculate_d(list_x[k - 1], list_x[k], list_x[k + 1], list_y, k)
        list_d[k] = d
    return list_d


def all_h(list_x):
    h = [1 for _ in range(len(list_x))]
    for i in range(1, len(list_x)):
        h[i] = list_x[i] - list_x[i - 1]
    return h


def alllambda(list_x):
    h = all_h(list_x)
    lambdas = [1 for _ in range(len(h))]
    for k in range(1, len(h) - 1):
        lambdas[k] = h[k] / (h[k] + h[k + 1])
    return lambdas


def all_M(lambda_values, d_values):
    q = [0]
    p = [0]
    u = [0]
    n = len(lambda_values) - 1
    for i in range(1, n):
        p.append(lambda_values[i] * q[i - 1] + 2)
        q.append((lambda_values[i] - 1) / p[i])
        u.append((d_values[i] - lambda_values[i] * u[i - 1]) / p[i])

    M = [0 for i in range(n + 1)]
    M[n - 1] = u[n - 1]
    for k in range(2, n):
        i = n - k
        M[i] = u[i] + q[i] * M[i + 1]

    return M


def pick_function(x, t):
    i = 0
    for el in t:
        if (x < el):
            return i - 1
        i = i + 1


def all_ss(x, t, lista):
    lambdas = alllambda(t)
    d = all_d(t, lista)
    M = all_M(lambdas, d)
    i = pick_function(x, t)
    h = all_h(t)[1:]

    return M[i] / (6 * h[i]) * pow((t[i + 1] - x), 3) + M[i + 1] / (6 * h[i]) * pow((x - t[i]), 3) + (
                lista[i + 1] / h[i] - M[i + 1] * h[i] / 6) * (x - t[i]) + (lista[i] / h[i] - M[i] * h[i] / 6) * (
                       t[i + 1] - x)



