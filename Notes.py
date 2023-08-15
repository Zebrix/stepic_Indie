# Числовое значение каждого символа вы можете получить с помощью команды ord()
# a, b = map(int, input().split())
# a = int(input())
# print(*list(range(1, 6)), sep=input())
# b = int(input())

a, b, c = map(int, input().split())  # считываем 4 целых числа через пробел
print(a * b * c * 2)

from math import ceil
print(ceil(float(input())/10))
print(input()[-1])

s = 'hello world'
print(s.title()) # Hello World
print(s.capitalize()) # Hello world
print(s.swapcase()) # HELLO WORLD
print(input().upper())
print(input().count('e')) # Счётчик включений
# --------------- СТРОКОВЫЕ методы -------------
# S.find(sub[, start[, end]]) - поиск. возвращает -1 если не найдено
# S.rfind(sub[, start[, end]]) - поиск справа налево
# S.index(sub[, start[, end]]) - тоже поиск, но завершается с ошибкой если не найдено
# S.replace(old, new[, count]) - замена в строке
# S.join(iterable)             - склеивает строку. S - разделитель, iterable - список.
# S.startswith(prefix[, start[, end]])  - Проверка на наличие prefix в начале строки (среза)
# S.endswith(prefix[, start[, end]])    - Проверка на наличие prefix в конце строки (среза)
# S.isalpha()                  -  True , если строка S не пустая и состоит только из букв
# S.isalnum()                  -  True , если строка S не пустая и состоит только из букв и цифр
# S.istitle()                  -  True , если строка S не пустая и слова в ней с заглавной буквой
# S.ljust(width[, fillchar])   - дополнить строку справа символами fillchar (или пробелами)
# S.rjust(width[, fillchar])   - дополнить строку слева символами fillchar (или пробелами)
# S.center(width[, fillchar]   - дополнить строку слева и справа символами fillchar (или пробелами), левый сначала
# S.zfill(width)   - дополнить строку слева нулями
# S.strip([chars])             - удаляет символы chars (не строку!) слева и справа
# S.rstrip([chars])             - удаляет символы chars (не строку!) справа
# S.lstrip([chars])             - удаляет символы chars (не строку!) слева
# S.rpartition(sep)             - разбивает строку по последнему встреченному разделителю sep и возвращает кортеж,
#                                 который состоит из трех элементов: строки до разделителя, самого разделителя и строки
#                                 после разделителя. Если разделитель в строке отсутствует, то кортеж будет состоять
#                                 из: двух пустых строк и исходной строки




