from random import randint

gen_list = [el * randint(1, 3) for el in range(1, 10) if not el % 2]
print(gen_list)
list_a = []
for el in gen_list:
    if gen_list.count(el) == 1:
        list_a.append(el)
print(list_a)
