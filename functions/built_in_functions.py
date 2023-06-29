'''Встроенные функции'''

'''общеизвестные'''
print
len
sum
min
max
input
int
list
str
id
dir
sorted
divmod
type
# ...

'''lambda -> анонимная функция (та же самая функция, только без имени)'''

# def <имя>(параметры):
#     тело 

# lambda параметры: что функция возвращает

# def add_nums(x, y): return x + y
# # print(add_nums(5, 6))

# print((lambda x, y: x + y)(4, 7))

# lambda_fun = lambda x, y: x + y
# print(lambda_fun(7, 9))

# a = lambda a, b, c: (a, b, c)

# print(a(3, 4, 5))

# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# dict_keys = lambda x: x.keys()
# print(dict_keys(dict_))
# def func(dict_)

# ls = [1, 2, 3, 4, 5, 6, 7, 8]

# num = lambda z: z[-1]
# # num(ls)
# print(num(ls))

# num = lambda num1: num1**2
# print(num(7))

# o = 'o'
# о = 'о'
# print(id(o), id(о))

'''
map(func, iterable) -> она применяет func для каждого элемента итнрируемого объекта
'''
# map()
list_ = ['1', '2', '3']
# print(map(int, list_))
# for i in map(int, list_):
#     print(type(i))

# print(list(map(int, list_)))

# nums = input('Введите два числа через пробел: ')

# a, b = map(int, nums.strip().split())

# print(a)
# print(b)

# list_ = ['1', '2', '3']
# list_nums = []

# for i in list_:
#     list_nums.append(int(i))

# print(list_nums)

# def square(a):
#     return a ** 2

# list_ = [3, 56, 2, 4]
# list_s = list(map(lambda x: x ** 2, list_))
# list_s = list(map(square, list_))
# print(list_s)


'''
filter(func, iterable) -> фильтрует элементы итерируемого объекта, основываясь на результат func
func -> True
'''

# def filter_nums(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     return False

# list_ = [2, 6, 4, 9, 7, 55, 33]

# result = list(filter(filter_nums, list_))
# lambda_func = lambda x: x % 2 == 0
# result = list(filter(lambda_func, list_))
# result = list(filter(lambda x: x % 2 == 0, list_))
# print(result)


list_ = ["Тима", "Макс", "Эртай", "Алина", "Эркайым", "Алекс"]

def startswith_vowels(name):
    vowels = 'АЕОУИЭЮЯ'
    # print(tuple(vowels))
    return name.upper().startswith(tuple(vowels))

result = list(filter(startswith_vowels, list_))
vowels = 'АЕОУИЭЮЯ'
result = list(filter( lambda name: name.upper().startswith(tuple(vowels)), list_))
# print(result)
# print(startswith_vowels('алекс'))

'''======= filter на цикле for ======'''
list_1 = []
for name in list_:
    if startswith_vowels(name):
        list_1.append(name)

# print(list_1)


'''
reduce(func, iterable) -> нужно импортировать с functools. возвращает один результат 
заменили -> sum, min, max
'''
'''
сумма все элементов списка
'''
from functools import reduce

list_ = [5, 2, 9, 6, 4, 3]
# result = reduce(lambda x, y: x + y, list_
# )

'''Произведение всех элементов списка'''
result = reduce(lambda x, y: x * y, list_)
# print(result)

'''reduce на цикле for'''
# x = list_[0]
# for y in list_[1:]:
#     x = (lambda x, y: x * y)(x, y)
# print(result)


'''enumerate(iterable, [start]) -> нумерует элементы последовательности (по дефолту с 0 )'''

list_ = ['hello', 'test', 'john', 'world', 'py30', 'питхаб']

# print(list(enumerate(list_, 9))) # начнет нумерацию с 9

# for i in enumerate(list_):
#     print(i)

# for index, element in enumerate(list_):
#     print(f'index - {index} element - {element}')



''' zip(iterable, iterable, [*iterables]) -> сопаставляет каждый элемент последовательности со следующим'''

# list_ = [1, 2, 3, 4]
# list_2 = [5, 6, 7, 8, 7, 6]
# list_3 = ['hello', 'list', 'zip']
# # for i in zip(list_, list_2, list_3):
# #     print(i)
# print(list(zip(list_, list_2, list_3)))

'''Изменить тип данных значений'''
# dict_ = {1: 2, 3: 4, 5: 6}

# def convert_to_str(value):
#     return str(value)

# result = list(map(convert_to_str, dict_.values()))
# # print(result)
# new_dict = dict(zip(dict_.keys(), result))
# print(new_dict)

"""задача при помощи map() заменить значение чисел словами четное.нечетное"""
# list_ = [1, 2, 3, 4]
# result = list(map(lambda x: 'нечетное' if x % 2 else 'четное', list_))
# print(result)


# all, any
# all()


# list_ = [-1, 6, -9, 7] 
# list_2 = list(map(lambda x: x < 0, list_)) 
# print(list_2) 
# print(any(list_2))

