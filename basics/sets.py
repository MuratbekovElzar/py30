'''Множества -> set()'''
# изменяемый, неупорядоченный, неиндуксируемый, итерируемый тип данных, который хранит в себе только уникальные значения
# лиреталы -> {}

'''создание пустого множества'''
# set_a = set()
# print(type(set_a))

# set_b = {1, 2, 3}
# print(set_b)

'''Элементами множества могут быть только неизменяемые типы данных'''


# set_ = set({1: 'a', 2: 'b', 3: 'c'})
# set_ = set([1, 2, 3, 4, 1, 2, 1, 3])
# set_ = set('Makersaaadddsss')
# print(set_)

'''Методы множеаств'''
# print(dir(set))

# set.add(element) -> добавляет element во множество
'''если добавляем tuple, то все его элементы должны быть неизм неизменяемыми'''
set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'test', 'world'}
# set_a.add('hello') #добавит слово целиком
# a = 4
# set_a.add(a)
# print(set_a)

# for i in range(101):
#     set_a.add(i)
# print(set_a)


# set.update(iterable) ->  добавляет элементы из последовательности во множество
# set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'test', 'world'}
# # set_a.update([1, 2, 3, 'Makers', 'makers'])
# set_a.update('hello') # добавит слово поэлементно
# print(set_a)

# set_b = set()
# a = [[1, 2, 3], [4, 5, 6, 1], [7, 8, 9, 4]]
# for i in a:
#     print(i)
#     set_b.update(i)

# print(set_b)


# set.clear() -> очищает множество
# set_a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 'hello', 'test', 'world'}
# set_a.clear()
# print(set_a)

# set.pop() -> удаляет рандомный элемент из множества (первый в терущем порядке)

# set_a = { 'world', 8, 9, 'hello', 'test'}
# print(set_a)
# print(set_a.pop())
# print(set_a)
# print(set_a.pop())
# print(set_a)
# print(set_a.pop())
# print(set_a)

# set_a.difference(set_b) -> возвращает элементы, которые есть в set_a ,но нет в set_b (можно использовать "-")

# set_a = {1, 2, 3, 4, 5, 'test', 'hello'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# print(set_a-set_b)
# print(set_a.difference(set_b))
# print(set_b.difference(set_a))


# set_a.symmetric_difference(set_b) -> возвращает уникальные элементы для set_a и set_b (уникальные для обоих множеств )
# set_a = {1, 2, 3, 4, 5, 'test', 'hello'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# print(set_a.symmetric_difference(set_b))
# print(set_b ^ set_a)


# set_a.intersection(set_b) -> возвращает схожие элементы обоих множеств
# set_a = {1, 2, 3, 4, 5, 'test', 'hello'}
# set_b = {4, 5, 6, 7, 8, 'test'}
# print(set_a.intersection(set_b))
# print(set_a & set_b)

# set_a.union(set_b) -> соединяет два множества
set_a = {1, 2, 3, 0, 'hello'}
set_b = {4, 5, 6, 7, 8, 'test'}
# print(set_a.isdisjoint(set_b))
# list_ = [8, 9, 0, 't']
# print(set_a.union(set_b))
# print(set_a | set_b)
# print(set_a.union(list_))
# print(set_a | list_) Error

''' Д/з
set.difference_update()
set.intersection_update()
set.symmetric_difference_update()
set.isdisjoint()
set.issuperset()
set.issubset()
'''


# Экстра-задание 1
# Создайте переменную a в которой будет хранится список из 3 пустых множеств.
# От пользователя, вы получаете строку Hello world, которую надо сохранить в переменной inp1.

# Также, вы получаете число, от 1 до 3, которое нужно сохранить в переменную inp2.

# Число 1 соответствует первому множеству в списке a, число 2 второму, а 3 третьему.

# В зависимости от переданного числа, сохраните строку в inp1, в одно из пустых множеств внутри списка a. В остальные множества добавьте строку "default value".

# В конце, выведите получившийся список.

# Например, если пользователь ввел Hello world и 1, то вывод:

# [{'Hello world'}, {'default value'}, {'default value'}]
# Для проверки кода, введите строку Hello world и число в поля во вкладке INPUT.

# a = [ set(), set(), set()]
# inp1 = input()
# inp2 = int(input())
# 1, 2, 3
# a[inp2-1].add(inp1)
# print(a)