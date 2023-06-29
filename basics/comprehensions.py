'''======= Comprehension ======'''
# генерация последовательности в одну строку используя цикл for (синтаксический сахар)

# for переменная in диапазон:
#     тело

"""Синтаксис"""
#1. результат for элемент in итерируемый объект

# 2.  результат for элемент in итерируемый объект if фильрт


'''========= List comprehension ========='''
# упрощение процесса создания списков

# list_ = []
# for i in 'hello':
#     list_.append(i)
# print(list_)

# list_0 = list((i for i in 'hello'))

# list_1 = [i for i in 'hello']
# print(list_1)

# import time

# start_time = time.time()
# list_ = []
# for i in range(1, 1000001):
#     list_.append(i)

# print(time.time() - start_time)


# start_time = time.time()
# list_num = [number for number in range(1, 1000001)]
# print(time.time() - start_time)
# end_time = time.time()

'''создайте список от 1 до 10, состоящий только из четных элементов'''

# list_ = [i for i in range(1, 11) if i % 2 == 0 ]
# list_ = [i for i in range(2, 11, 2)]
# print(list_)

# list_ = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_.append(i)
# print(list_)

# print(['hello' for i in range(10)])

# print([input() for i in range(10)])

'''синтаксис'''
# [элемент if условие else элемент2 for i in итерируемый_объект]

# a = [
#     'четное' 
#     if i % 2 == 0 
#     else 'нечетное' 
#     for i in range(1, 11)
#     ]
# print(a)

# list_str = []
# for i in range(1, 11):
#     if i % 2 == 0:
#         list_str.append('четное')
#     else:
#         list_str.append('нечетное')


'''===== Set comprehension ====='''
# list_ = [1, 2, 3, 1,'test', 'python', 'makers', 1, 2, 3, 4, 5, 6, 'hello']
# set_l = {i + ' world' for i in list_ if type(i) == str}

# set_l = {i + ' world' if type(i) == str else i + 1 for i in list_ }
# print(set_l)

# set_ = set()
# for i in list_:
#     set_.add(i)

# print(set_)


'''======= Dict comprehension ========'''

# dict_ = {1: 'a', 2: 'b', 3: 'c'}

# dict_1 = {}
# for k, v in dict_.items():
#     dict_1.update({v: k})

# print(dict_1)

# dict_1 = {v: k for k, v in dict_.items()}
# print(dict_1)

# dict_ = {}
# for i in range(1, 11):
#     dict_.update({i: i**2})

# print(dict_)

# # [(1, 2), (3, 4)]
# dict_ = {i: i ** 2 for i in range(1, 11)}
# print(dict_)


# list_ = [1, 1, 2, 1, 3, 7, 8, 4, 4, 5]
# dict_1 = {i: list_.count(i) for i in list_}
# print(dict_1)

# dict_ = {'a' : 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# {'a': 'нечетное', 'b': 'четное'}

# dict_abc = {k: ('нечетное' if v % 2 else 'четное') for k, v in dict_.items()}
# print(dict_abc)

# 'даны 2 списка, создайте словарь, где ключи - элементы 1 списка, а значения - второго'
# list1 = [1,2,3,4,5]
# list2 = ['a','b','c','d','e']
# dict_list = {
#     list1[index]: '->'.join(list2) 
#     for index in range(len(list1))
#     }

# print(dict_list)

# 'объединитель'.join(list_)  -> переводи список в тип данных строки
 
# ''.join(['a', 'b', 'c']) -> 'abc'


'''======= вложенные comprehensions ====='''

# dct = {
#     i: 
#     [j for j in range(1, i+1)]
#     for i in range(1, 6)
#     }
# print(dct)
# 1: [1] 2: [1, 2]

# list_ = [
#     ['hello world' for i in range(2)] #element 
#     for i in range(3)
#     ]
# print(list_)


employees = {
    'id1': {
        'first name': 'Александр',
        'last name' : 'Иванов',
        'age': 30,
        'job':'программист'
            },
    'id2': {
        'first name': 'Ольга',
        'last name' : 'Петрова',
        'age': 35,
        'job':'ML-engineer'
            }
}


# dct = {
#     id_: 
#     {k: float(v) 
#     if k == 'age' else v 
#     for k, v in info.items()
#     }
#     for id_, info in 
#     employees.items()
#     }

# print(dct)

for info in employees.values():
    for k, v in info.items():
        if k == 'age':
            info[k] = float(v)

print(employees)