# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https://ru.wikipedia.org/wiki/Кодированиедлинсерий
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCDEFGH -> 1A1B1C1D1E1F1G1H -> ABCDEFGH
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR


# Функцию сжатия строки
def str_compression(data: str) -> str:
    symbol = data[0]
    count = 0
    res_str = ""
    for el in data:
        if el == symbol:
            count += 1
        elif el != symbol:
            res_str += str(count) + symbol
            count = 1
            symbol = el
    res_str += str(count) + symbol
    return res_str


# Функцию восстановления строки
def restoring_str(data:str) -> str:
    number = ''
    res_str = ''
    for i in range(len(data)):
        if not data[i].isalpha():
            number += data[i]
        else:
            res_str += data[i] * int(number)
            number = ''
    return res_str


data1 = 'WWJJJHDDDDDPPGRRR' 
data2 = '2W3J1H5D2P1G3R'   
print(f'{data1} -> {str_compression(data1)} -> {restoring_str(data2)}')
