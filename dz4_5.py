from functools import reduce


def func_reduce(el1, el2):
    return el1 * el2


list_a = [el for el in range(100, 1001) if not el % 2]
print(reduce(func_reduce, list_a))
