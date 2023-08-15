with open('numbers.txt', 'r') as nnn:
    aaa = 0 # кол
    aa = 0 # сум
    for n in nnn:
        x = int(n.strip())
        if 9 < x < 100:
            aa += x
        elif 100 <= x < 1000:
            aaa += 1
print(f'Количество трёхзначных - {aaa}')
print(f'Сумма двухзначных - {aa}')
