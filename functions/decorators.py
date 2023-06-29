'''Декораторы'''


# def outer(x):
#     def inner(y):
#         return x+y
#     return inner

# inner_func = outer(7)
# print(inner_func(7))
# print(inner_func)
# a = print
# a('hello')
# print(a)



'''
функция высшего порядка -> это функция, которая может принимать в качестве аргумента другую функцию и/или возвращать функцию как результат
'''

# def test_func(func):
#     def inner_test_func():
#         func()
#         # <тело>
#     return inner_test_func

# def hello(func):
#     # <тело>
#     pass


'''
Декоратор -> функция высшего порядка (в качестве аргумента примает функцию и возвращает функцию), которая оборачивает другую функцию для расширения ее функционала, при этом не изменяя ее код
'''

# def test_decor(func):
#     print('Makers')
#     func()
#     print('hello')

# def a():
#     print('Привет')

# test_decor(a)

# from typing import Callable

# def benchmark(func: Callable) -> None:
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(f'Время работы функции {func.__name__}, заняло {end - start}')
#     return wrapper

# # loop = None
# @benchmark
# def loop():
#     i = 0
#     while i < 1000000:
#         print(i)
#         i += 1
# loop()
# # benchmark(loop)

# def test_for_loop():
#     for i in range(1000000):
#         pass
#         # print(i)

# # benchmark(test_for_loop)
# # print(dir(loop))

'''Синтаксис'''
def decorator(func):
    def wrapper():
        print('Фунция-обертка!')
        print(f'Оборачиваем функцию {func.__name__}')
        func()
        print('Выходим из обертки')
    return wrapper

# @decorator
def say_hi():
    print('Hiiiiiiiiiiiiiiiiiiiiiii')

# say_hi()
# как работает @ по капотом
'''
@ -> синтаксический сахар, позволяет нам явно указать какой декоратор применяется для функции

под капотом вызывает функцию decorator и результат выполнения этой функции сохраняет в переменной с точно таким же названием как и обернутая функция
say_hi = decorator(say_hi)
say_hi()
'''

# def uppercase_decorator(func):
#     def wrapper():
#         func_ = func()
#         upper_str = func_.upper()
#         return upper_str
#     return wrapper

# @uppercase_decorator
# def inp_str():
#     str_ = input('Введите текст: ')
#     return str_


# print(inp_str())
    
# def smart(func):
#     def wrapper(x, y):
#         print('============')
#         if y == 0:
#             return 
#         return func(x, y)
#     return wrapper

# @smart
# def division(x, y):
#     return x / y

# print(division(7, 0))
# print(division(7, 3))

'''напишите декоратор для вызова функции определенного кол-ва раз'''

# num
# func
# *args **kwargs

# def decorator(num):
#     def inner_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 func(i, *args, **kwargs)
#         return  wrapper
#     return inner_decorator

# @decorator(7)
# def test(a, b):
#     print(f'=========={a}\n+++++++++++{b}')

# test('*')


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def div(func):
    def wrapper():
        return '<div>' + func() + ' Зима близко' + '</div>'
    return wrapper

# @test
@strong
@div
@div
def get():
    return 'Jhon Snow'

print(get())