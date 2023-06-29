
# Виды коментариев
'''
1. Многострочный
'''
"""Многострочный"""
# 2.

'''
Обзор типов данных
Типы данных в Питоне
'''

# 1. NoneType -> None
# 2. Boolean (bool()) -> True/False
# 3. Числовые типы данных:
    # a. integer (int()) -> 1 2 3 ... Целые числа
    # b. float() -> 1.6  5.99 Числа с плавающей точкой
    # c. complex(3, 5) -> 3 + 5j Комплексные числа
# 4. string (str()) -> "hello" 'makers' """ """  ''' ''' ... Строки
# 5. list() -> [1, 2, 3, None, True, 'Hello', [1, 2, 3], {1: 'a'}] Списки
# 6. tuple() -> (1, 2, 3, None, False) Кортеж
# 7. set() -> {1, 2, 3, 4, 5} Множество
# 8. dict() -> {1: 'one', 2: 'two'} Словарь 
# 9. frozenset() -> замороженное множество

 
'''Изменяемые (Mutable)'''
# set()
# dict()
# list()


'''================ Переменные ==============='''
# ссылка на ячейку памяти в которой хранится объект. Предназначена для для хранения данных

hello_world = 'snake case'
helloWorld = 'camel case'

num = 10
num_2 = 11
name = 'John'
age = 32
is_user = True

# print() -> функция для вывода данных в терминал

# print(hello_world)
# print(helloWorld)

# num3 = num + num_2
# print(num3)

# input() -> функция ввода данных c терминала

# name = input('Enter your name: ')
# print(name)

3
        #  два разных объекта
'3'

# type() -> выводит тип данных
# print(type(3))
# print('3' + '3')

# int() -> для перевода в тип данных целые числа

# number1 = int(input('Введите число: '))
# # print(int(number1))
# print(type(number1))

# a = 1 
# b = 1

# id() -> выводит номер ячейки в памяти

# print(id(a), id(b))

# list_ =[1, 2, 3, 4]
# print(list_)
# print(id(list_))
# list_.append(5)
# print(list_)
# print(id(list_))

'''========= Операции над числами ========='''
# +
# number1 = 100
# number2 = 10
# print(number1 + number2)

# # -
# number_1 = 77
# number_2 = 9
# print(number_1 - number_2)

# # * -> умножение
# number_3 = number_2 * number_1
# print(number_3)

# / -> деление 

# division_result = number1 / number2
# print(division_result)

# # % -> для получения остатка от деления
# a = 89
# b = 9
# print(a % b)

# // -> целочисленное деление
# a = 89
# b = 9
# print(a // b)


# ** -> возведение в степень
# print(10 ** 2)
# print(5 ** 3)


# abs -> модуль числа -> |-9| из острицательного сделает положительное
# print(abs(-9))
# print(abs(10))

# pow -> 1. возведение в степень
    #    2.  возвращает остаток от деления первого результата (возведения в степень) на третье число

# 1. 
# print(pow(5, 4))
# 2.
# print(pow(5, 3, 9))

# divmode() -> принимает два числа и возвращает два числа ->   первое число - результат целочисленного деления, второе -> остаток от деления

# print(divmod(9, 4))
# divmod(15, 5)  # (3, 0)

# round()
# print(round(559/5))
# print(round(777/8, 3)) # второй элемент, указывает сколько числе после запятой оставить

import math
# math -> pi, cos, sin, sqrt, factorial ...
# print(dir(math))

# from math import sqrt

# # math.sqrt()
# sqrt() -> для гахождения квадратного корня

# print(math.sqrt(100))
# math.sqrt(36) #6

