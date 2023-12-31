'''Логические ввыражения и операторы Python'''

'''Boolean'''
# неизменяемый тип данных
# True/False
# print(bool(0)) #False
# print(bool(2)) #True
# print(bool(False)) #False
# print(bool('False')) #True
# print(bool(' ')) #True
# print(bool('')) #False
# print(bool(-234))

'''Логические выражения -> выражения, которые возвращают Boolean Type'''
#  Логические операторы

# == -> сравнение
5 == 5 # True
4 == 6 # False
'5' == 5 # False

# != -> не равно
5 != 5 # False
6 != 4 # True

# > (больше)
5 > 2 # True
6 > 9 # False
5 > 5 # False

# < (меньше)
3 < 4 #True
3 < 1 #False
3 < 3 #False


# >= -> больше или равно
6 >= 5 #True
6 >= 6 #True
6 >= 9 #False

# <= -> меньше или равно
4 <= 3 #False
4 <= 5 #True
4 <= 4 #True

'''and or not'''
# and -> логическое и
# or -> логическое или
# not -> логическое отрицание

# and     Используются для объедтнения
# or          логических выражений

a = 5
b = 6

#True      True
a == 5 and b == 6 #True
a == 4 and b == 6 #False
a == 3 and b == 9 #False
# если все части выражения возвращают True, то все все выражение возвращает True
# если хотя бы одна часть выражения возвращает False -> False

# a = 'g'
# b = 'h'

# a == 'g' and b == 'h'

a == 5 or b == 6 #True
a == 4 or b == 6 #True
a == 4 or b == 9 #False
# если хотя бы одна часть выражения возвращает True, то все выражение возвращает True

# not

# print(not True) #False
# print(not False) #True
not a == 5 #False
not b == 7 #True

'''Операторы идентификации'''
# 1. in -> проверяет наличие элемента
# 2. сравнения
#   == -> по значению
#   is -> по ячейке памяти
# 3. is not -> отрицательое сравнение ячеек памяти

# if 'e' in 'hello':
#     print('eeeeeee')
# print(' ' in 'hello')


'''========= None Type ========'''
# неизменяемый тип данных с одним значением None. Используется для обозначения пустых значений

bool(None) #False
bool('None') #True

# a = None
# print(a == None)


'''========= Условные операторы ========'''
# нужны, для того, чтобы при разных входных данных код выполнялся по разному

# if условие:
#     тело
# тело будет работать, если условие True (верно)


# if условие1:
#     тело1
# else:
#     тело2
# тело1 будет работать, если условие1 верно, тело2 ->  если условие1 не верно (во всех других случаях)


# if условие1:
#     тело1
#     # тело1 будет работать только  если условие1 верно 
# elif условие2:
#     тело2
#     # тело2 будет работать только  если условие1 не верно, а условие2 верно
# elif условие3:
#     тело3
#     # тело3 будет работать только  если условие1 и условие2 не верны, а условие3 верно
# else:
#     тело4
#     # тело4  будет работать во всех остальных случаях (условие1, условие2, условие3 не верны)

# в одной конструкции один if
# неограниченное кол-во elif
# один else

# if a == 0:
#     print('hello')
# elif a == 1:


# if a == 1:
#     print('aaaaaaaaa')

# age = int(input('Введите возраст: '))
# if age >= 18:
#     print('Ok')
# else:
#     print('go away')

''' Запросите пользователя ввести число и выведите: является это число положительным, отрицательным или 0'''

# number = int(input('Введите число: '))
# if number > 0:
#     print(f'{number} positive')
# elif number < 0:
#     print(f'{number} negative')
# else:
#     print(f'{number} zero')

# elif number == 0:
#     print Запросите пользователя ввести число и выведите: является это число положительным, отрицательным или 0

'''Тернарные операторы'''
# условие в одну строку/ if else в одну строку

# Синтаксис
# тело1 if условие else тело2

# num = 9
# result = 'Hello' if num == 9 else 'World'
# print(result)

'''====== Маржовый оператор ====='''
# позволяет нам как присваивать значение, так и возвращать его в одном выражении

# print(hello :='hello')
# print(hello = 'hello') #TypeError

'''задача 1:четное/нечестное'''
# num = int(input('Введите число: '))
# # Вариант 1
# if num % 2 == 0:
#     print('четное')
# else:
#     print('нечетное')

# Вариант 2
# if num % 2:
#     print('нечетное')
# else:
#     print('четное')

# Вариант 3
# a = 'четное'  if num % 2 == 0 else 'нечетное'

# # Вариант 4
# a = 'нечетное'  if num % 2 else 'четное'

" ======FizzBuzz======"
# примите от пользователя число от 1 до 100
# если число кратно 3 - вывести Fizz
# если число кратно 5 - вывести Buzz
# если число кратно и 5 и 3 - вывести FizzBuzz
# если число не кратно ни 5 ни 3 - вывести число

# a = int(input())

# if a % 15 == 0:
#     print('FizzBuzz')
# # if a % 3 == 0 and a % 5 == 0:
#     # print('FizzBuzz)
# elif a % 3 == 0:
#     print('Fizz')
# elif a % 5 == 0:
#     print('Buzz')
# else:
#     print(a)
