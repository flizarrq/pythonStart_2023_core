# ДЗ

# strings
#
# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
st = 'as 23 fdfdg544'

print([','.join([i for i in st if i.isdigit()])])
# #################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
st = 'as 23 fdfdg544 34'

print(','.join(''.join(ch if ch.isdigit() else ' ' for ch in st).split()))
# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']
greeting = 'Hello, world'

print([i.upper() for i in greeting])

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print([i ** 2 for i in range(0, 50) if i % 2 != 0])


# function
#
# - створити функцію яка виводить ліст

def showLish(list):
    for i in list:
        print(i)


showLish([1, 2, 3, 4])


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def maxNum(a, b, c):
    biggest = a
    if (b >= a and b >= c):
        biggest = b
    elif (c >= a and c >= b):
        biggest = c
    print(biggest)
    return biggest


maxNum(12, 1211, 1111)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def maxMin(*args):
    print(max(args))
    return min(args)


maxMin(10, 0, 10000)


# - створити функцію яка повертає найбільше число з ліста

def maxList(list):
    return max(list)


# - створити функцію яка повертає найменьше число з ліста

def minList(list):
    return min(list)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sumList(list):
    return sum(list)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avg(list):
    print('avg: ' + str(sum(list) // len(list)))


avg([1, 2, 3, 4, 5, 6, 7])

#
#
# ################################################################################################
# 1)Дан list:
list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]


#   - знайти мін число
def find_min(list):
    print(f'min: {min(list)}')


#   - видалити усі дублікати
def deleteDubl(list):
    list = set(list)
    print(f'new list: {list}')


#   - замінити кожне 4-те значення на 'X'

def changeToX(list):
    list = ['x' if i % 4 == 0 else ch for i, ch in enumerate(list)]
    print(list)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(width):
    print('* ' * width)
    for i in range(0, width - 1):
        print('* ' + '  ' * (width - 2) + '*')
    print('* ' * width)


# 3) вывести табличку множення за допомогою цикла while

def multi():
    size = 9
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            res = i * j
            print(f'{res:4}', end='')
            j += 1
        print()
        i += 1


# 4) переробити це завдання під меню

def menu():
    while True:
        print('1) знайти мін число')
        print('2) видалити усі дублікати')
        print('3) замінити кожне 4-те значення на \'X\'')
        print('4) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
        print('5) вивести табличку множення за допомогою цикла while')
        print('0) вийти')

        choose = input('make ur choose: ')

        if (choose == '1'):
            find_min(list)
        elif (choose == '2'):
            deleteDubl(list)
        elif (choose == '3'):
            changeToX(list)
        elif (choose == '4'):
            square(6)
        elif (choose == '5'):
            multi()
        elif (choose == '0'):
            break


menu()
