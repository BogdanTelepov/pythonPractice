import random

player = input('Ваш ход - Камень, Ножницы, Бумага: ').lower()
random_num = random.randint(0,2)

if random_num == 0:
	computer = 'камень'
elif random_num == 1:
	computer = 'ножницы'
elif random_num == 2:
	computer ='бумага'

if  player == computer:
    print('Ничья!')
elif player == 'камень':
    if computer == 'ножницы':
        print('Первый игрок выиграл!')
    elif computer == 'бумага':
        print('Компьютер выиграл!')
elif player == 'ножницы':
    if computer == 'камень':
        print('Компьютер выиграл!')
    elif computer == 'бумага':
        print('Первый игрок выиграл!')
elif player == 'бумага':
    if computer == 'камень':
        print('Первый игрок выиграл!')
    elif computer == 'ножницы':
        print('Компьютер выиграл!')
else:
    print('Вы ввели неправильную команду!')

