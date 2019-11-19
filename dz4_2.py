from random import randint

gen_list = [el * randint(1, 5) for el in range(1, 10)]
print(gen_list)
el = 1
while el < len(gen_list):
    if gen_list[el] <= gen_list[el - 1]:
        gen_list.pop(el)
    el += 1
print(gen_list)
