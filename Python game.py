print('Игра \'Крестики-Нолики\'')
print('')
print('Перед Вами игровое поле - Вы играете за крестики')
print('')


 #рисует первую строку - координаты оси Х
def xaxis():
    a=[]

    for i in range (3):
        if i == 0:
            a.append(' ')
            a.append(0)
        else:
            a.append(i)


    b=('%s' % ', '.join(map(str, a)))
    c=str(b).replace(',','')
    print(c) 


#рисует игровое поле

blank = '-'
x= 'x'
o= 'o'

all_moves = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

xaxis()
for j in range (3):

    if j==0:
        firstrow = (f'{j} {blank} {blank} {blank}')
    elif j == 1:
        secondrow = (f'{j} {blank} {blank} {blank}')
    else:
        thirdrow = (f'{j} {blank} {blank} {blank}')
print(firstrow)
print(secondrow)
print(thirdrow)


#первый ход игрока
print(' ')
print('Ваш ход:')
print('')
coordx=int(input('Введите координаты хода на оси Х: '))
coordy=int(input('Введите коррдинаты хода на оси У: '))
print('')




move = [coordx,coordy]

if move in all_moves:
    if move == [0,0]:
        xaxis()
        firstrow=firstrow[:(coordx+2)]+x+firstrow[(coordx+3):]
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [0,1]:
        xaxis()
        print(firstrow)
        secondrow=(f'{1} {x} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [0,2]:
        xaxis()
        firstdrow=(f'{0} {blank} {blank} {blank}')
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {x} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [1,0]:
        xaxis()
        firstrow=(f'{0} {blank} {x} {blank}')
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [1,1]:
        xaxis()
        firstrow=(f'{0} {blank} {blank} {blank}')
        print(firstrow)
        secondrow=(f'{1} {blank} {x} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [1,2]:
        xaxis()
        firstrow=(f'{0} {blank} {blank} {blank}')
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {x} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [2,0]:
        xaxis()
        firstrow=(f'{0} {blank} {blank} {x}')
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [2,1]:
        xaxis()
        firstrow=(f'{0} {blank} {blank} {blank}')
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {x}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {blank}')
        print(thirdrow)
        print('')
        all_moves.remove(move)
    else:
        xaxis()
        firstrow=(f'{0} {blank} {blank} {blank}')
        print(firstrow)
        secondrow=(f'{1} {blank} {blank} {blank}')
        print(secondrow)
        thirdrow=(f'{2} {blank} {blank} {x}')
        print(thirdrow)
        print('')
        all_moves.remove(move)

else:
    print('такой ход невозможен')


#первый ход компьютера
def computer_move():
    global all_moves
    import random
    global firstrow
    global secondrow
    global thirdrow
    global x
    global o

    move=random.choice(all_moves)
    print('Ход нолика')
    print(' ')

    if move == [0,0]:
        xaxis()
        firstrow=firstrow[:(coordx+2)]+o+firstrow[(coordx+3):]
        print(firstrow)
        print(secondrow)
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [0,1]:
        xaxis()
        print(firstrow)
        secondrow = secondrow[:(coordx+2)]+o+secondrow[(coordx+3):]
        print(secondrow)
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [0,2]:
        xaxis()
        print(firstrow)
        print(secondrow)
        thirdrow=thirdrow[:(coordx+2)]+o+thirdrow[(coordx+3):]
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [1,0]:
        xaxis()
        firstrow=firstrow[:(coordx+4)]+o+firstrow[(coordx+5):]
        print(firstrow)
        print(secondrow)
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [1,1]:
        xaxis()
        print(firstrow)
        secondrow = secondrow[:(coordx+4)]+o+secondrow[(coordx+5):]
        print(secondrow)
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [1,2]:
        xaxis()
        print(firstrow)
        print(secondrow)
        thirdrow=thirdrow[:(coordx+4)]+o+thirdrow[(coordx+5):]
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [2,0]:
        xaxis()
        firstrow=firstrow[:(coordx+6)]+o
        print(firstrow)
        print(secondrow)
        print(thirdrow)
        print('')
        all_moves.remove(move)
    elif move == [2,1]:
        xaxis()
        print(firstrow)
        secondrow = secondrow[:(coordx+6)]+o
        print(secondrow)
        print(thirdrow)
        print('')
        all_moves.remove(move)
    else:
        xaxis()
        print(firstrow)
        print(secondrow)
        thirdrow=thirdrow[:(coordx+6)]+o
        print(thirdrow)
        print('')
        all_moves.remove(move)

computer_move()



#второй ход игрока

def player_move(): #функция второго и далее хода игрока
    global firstrow
    global secondrow
    global thirdrow
    global x
    global o


    print('Ваш ход:')
    print('')
    coordx=int(input('Введите координаты хода на оси Х: '))
    coordy=int(input('Введите коррдинаты хода на оси У: '))
    print('')   
    move = [coordx,coordy]

    if move in all_moves:
        if move == [0,0]:

            xaxis()
            firstrow=firstrow[:(coordx+2)]+x+firstrow[(coordx+3):]
            print(firstrow)
            print(secondrow)
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [0,1]:

            xaxis()
            print(firstrow)
            secondrow = secondrow[:(coordx+2)]+x+secondrow[(coordx+3):]
            print(secondrow)
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [0,2]:

            xaxis()
            print(firstrow)
            print(secondrow)
            thirdrow=thirdrow[:(coordx+2)]+x+thirdrow[(coordx+3):]
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [1,0]:

            xaxis()
            firstrow=firstrow[:(coordx+3)]+x+firstrow[(coordx+4):]
            print(firstrow)
            print(secondrow)
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [1,1]:

            xaxis()
            print(firstrow)
            secondrow = secondrow[:(coordx+3)]+x+secondrow[(coordx+4):]
            print(secondrow)
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [1,2]:

            xaxis()
            print(firstrow)
            print(secondrow)
            thirdrow=thirdrow[:(coordx+3)]+x+thirdrow[(coordx+4):]
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [2,0]:

            xaxis()
            firstrow=firstrow[:(coordx+4)]+x
            print(firstrow)
            print(secondrow)
            print(thirdrow)
            print('')
            all_moves.remove(move)
        elif move == [2,1]:

            xaxis()
            print(firstrow)
            secondrow = secondrow[:(coordx+4)]+x
            print(secondrow)
            print(thirdrow)
            print('')
            all_moves.remove(move)
        else:

            xaxis()
            print(firstrow)
            print(secondrow)
            thirdrow=thirdrow[:(coordx+4)]+x
            print(thirdrow)
            print('')
            all_moves.remove(move)
    else:
        print('такой ход невозможен')
        print('')
        player_move()

player_move()


if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
    print('Вы победили!')

elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
    print('Вы проиграли')


else:
    computer_move()
    if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
        print('Вы победили!')

    elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
        print('Вы проиграли')
    else:
        player_move()
        if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
            print('Вы победили!')

        elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
            print('Вы проиграли')
        else:
            computer_move()
            if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
                print('Вы победили!')

            elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
                print('Вы проиграли')
            else:
                player_move()
                if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
                    print('Вы победили!')

                elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
                    print('Вы проиграли')
                else:
                    computer_move()
                    if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
                        print('Вы победили!')

                    elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
                        print('Вы проиграли')
                    else:  
                        player_move()
                        if (x==firstrow[6] and x==secondrow[6] and x==thirdrow[6]) or (x==firstrow[4] and x==secondrow[4] and x==thirdrow[4]) or (x==firstrow[2] and x==firstrow[4] and x==firstrow[6]) or (x==secondrow[2] and x==secondrow[4] and x==secondrow[6]) or (x==thirdrow[2] and x==thirdrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[4] and x==thirdrow[6]) or (x==firstrow[2] and x==secondrow[2] and x==thirdrow[2]) or (x==firstrow[6] and x==firstrow[4] and x==firstrow[2]):
                            print('Вы победили!')

                        elif (o==firstrow[6] and o==secondrow[6] and o==thirdrow[6]) or (o==firstrow[4] and o==secondrow[4] and o==thirdrow[4]) or (o==firstrow[2] and o==firstrow[4] and o==firstrow[6]) or (o==secondrow[2] and o==secondrow[4] and o==secondrow[6]) or (o==thirdrow[2] and o==thirdrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[4] and o==thirdrow[6]) or (o==firstrow[2] and o==secondrow[2] and o==thirdrow[2]) or (o==firstrow[6] and o==firstrow[4] and o==firstrow[2]):
                            print('Вы проиграли')
                        else:  
                            print('Ничья')



    
