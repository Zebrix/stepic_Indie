#from math import ceil
#l, w, h = map(int, input().split())
#print(ceil((2 * l * w + 2 * w * h) / 16))

#a = input()
#print(input().lower().replace('a','').replace('o','').replace('y','').replace('e','').replace('u','').replace('i','').replace('','.')[:-1])

# print(input().isupper())
a = hex(int(input()))[2:].zfill(2)
b = input()
c = input()
print('#' + hex(int(input()))[2:].zfill(2) + hex(int(input()))[2:].zfill(2) + hex(int(input()))[2:].zfill(2))

a = int(input())
b = int(input())
print(f'{a} / {b} = {a / b}\n{a} // {b} = {a // b}\n{a} % {b} = {a % b}')
