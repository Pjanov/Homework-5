from random import randint


print('Игра с конфетами против Bota.\n\
    \nНа столе лежит некоторое кол-во конфет. Играют два игрока делая ход друг после\n\
друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более\n\
оговоринного колличества конфет. Все конфеты оппонента достаются сделавшему последний ход.\n ')

print('Перед стартом игры ответте на несколько вопросов:\n')

player_1 = input('Имя игрока: ')
player_2 = 'Bot'
candies = int(input('Введите количество конфет: '))
take_max = int(input('Сколько за один ход максимально можно взять конфет ?: '))

print('\nСТАРТ !\n')

first_move = randint(1, 2)  # жеребьевка
if first_move == 1:
    print(f'По итогам жеребьевки ходит {player_1}')
else:
    print(f'По итогам жеребьевки ходит {player_2}')

while candies >= take_max:
    if first_move == 1:
        pl_1 = int(input(f'Игрок {player_1} твой ход: '))
        candies -= pl_1
        print('Осталось:', candies)
        if candies <= take_max:
            winner = player_2
            break
        pl_2 = randint(1, take_max)
        print(f'Игрок Bot твой ход: {pl_2} ')
        candies -= pl_2
        print('Осталось:', candies)
        if candies <= take_max:
            winner = player_1
            break
    else:
        pl_2 = randint(1, take_max)
        print(f'Игрок Bot твой ход: {pl_2} ')
        candies -= pl_2
        print('Осталось:', candies)
        if candies <= take_max:
            winner = player_1
            break
        pl_1 = int(input(f'Игрок {player_1} твой ход: '))
        candies -= pl_1
        print('Осталось:', candies)
        if candies <= take_max:
            winner = player_2
            break
print(f'Победил {winner} поздравляем !')
print('Конец !')
