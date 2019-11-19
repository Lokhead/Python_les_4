from itertools import count, cycle

for el in count(10):
    if el > 20:
        break
    else:
        print(el)

n = 0
for el in cycle('Hello'):
    if n > 9:
        break
    print(el)
    n += 1
