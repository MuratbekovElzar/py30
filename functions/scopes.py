'''Области видимости и пространства имен'''


'''Пространства имен'''
'''
1. builtins (встроенное) -> все, что встроенно в стандартную библиотеку питона
(print, input, len ... )
'''

'''
2. Global -> (глобальное) все переменные внутри файла, которые мы создали (без табуляции)
'''
name = 'Sam'


'''
3. Enclosed -> (не локальное, замкнутое) находится между двумя пространствами
'''

'''
4. Local -> (локальное)
'''

# def test():
#     hello = 'hello'

# print(globals())  -> возвращает все глобальные переменные


# print(dir(__builtins__)) -> возвращает все встроенные имена


# x = 100
y = 0
z = 99

# x = 77
# globals()['x'] = 45
# print(z is globals()['z'])
# print(globals())


'''
Локальные -> переменные в функциях
'''

# locals() ->  возвращает все локальные имена
 
# def func(test):
#     a = 10
#     b = 0
#     print(locals()) # {'test': 6, 'a': 10, 'b': 0}

# func(6)

# print(locals()) -> когда применяем на глобальном уровне, возвращает все глобальные имена

# a = 5
# b = 6
# def func1():
#     # a = 1
#     # b = 9
#     print(a, b)

# func1()
# print(a, b)


'''Enclosed'''
# возникает только тогда, когда внутри функции объявляется еще функция (при вложенности функций)

# string = 'я глобальная'
# def outer_func():
#     # string = 'не локальная переменная (enclosed)'
#     print(string)
#     def inner_func():
#         # string = 'локальная переменная'
#         print(string)
#         # print(locals())
#     inner_func()
#     # print(locals())

# outer_func()
# inner_func() -> будет ошибка, так как она в нелокальной области 
# print(outer)

'''Порядок поиска переменных'''
# Local -> Enclosed -> Global -> Builtins


# import this #краткий гайд по Дзен Питону 


'''
global -> позволяет изменить значение глобальной переменной, находясь в локальной области видимости
'''
# x = 10

# def func():
#     global x
#     x = 20
#     print(x)


# func()
# print(x)

# x = [1, 2, 3]

# def func():
#     global x
#     # x[0] = 0
#     x = [3, 4, 5]
#     print(x)


# func()
# print(x)



count = 0

def couter():
    global count
    count += 1
    return count

# print(couter())
# print(couter())
# print(couter())
# print(count)
# couter()
# couter()
# couter()
# couter()

# name = input()
# age = input()
# print({'id': couter(), 'name': name, 'age': age})

# name = input()
# age = input()
# print({'id': couter(), 'name': name, 'age': age})

# a = 0
# def outer():
#     global a
#     a = 8
#     def inner():
#         global a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a = ', a)

# outer()
# print('global a = ', a)

'''
nonlocal -> позволяет изменить значение enclosed (не локальная) переменной в локальной области видимости
'''

# def outer():
#     a = 8
#     def inner():
#         nonlocal a
#         a = 10
#         print('inner a = ', a)
#     inner()
#     print('outer a = ', a)

# outer()

# from time import sleep

# def counter(number):
#     count = number

#     def add():
#         nonlocal count
#         count -= 1
#         print(count)
#         sleep(1)

#     for i in range(number):
#         add()

# counter(10)




