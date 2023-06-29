'''Тип данных Списки (list)'''
# изменяемый, упорядоченный, индексируемый, итерируемый тип данных.

# [] -> литералы (выражения или константы, которые создают объект )

# list_ = [1, 2, [True, 'hello'], 'hello', {1: 'one'}, (1, 2, 3), None]
# [1, 2, 'hello']
# print(id(list_))
# print(list_[0])
# print(list_[2][0])
# print(list_[-1])
# print(list_[:3])
# str_ = 'hello'
# str_[0] = 'a'

# list_[0] = 'привет'
# print(id(list_))
# print(list_)


'''======== Создание списков ======='''
# 1.  list(iterable)
# list_1 = list('hello world')
# print(list_1)

# 2. [] 
# a = []
# print(type(a))

# 3. range() -> возвращает последовательность 
# list_2 = list(range(11))
# print(list_2)
# range(start, end, step)
# start -> с какого числа начать (по умолчанию 0)
# end -> до какого элемента (не включительно end)
# step -> шаг (какие элементы пропустить)


# print(range(4))

'''========= Методы списков ========'''
# list.append(element) -> добавляет element в конец списка

# list_3 = [1, 2, 3, 'hello', 'world', 'test']
# # list_3.append(4)
# list_3.append([1, 2, 3])
# print(list_3)

# list.extend([iterable]) -> расширяет список
# добавляет каждый элемент iterable по отдельности в конец списка
# list_3 = [1, 2, 3, 'hello', 'world', 'test']

# list_3.extend([1, 2, 3])
# list_3.extend('hello')
# # list_3.extend({1: 5})
# print(list_3)


# list.insert(index, element) -> добавляет element по индексно (по указанному индексу)
# list_3 = [1, 2, 3, 'hello', 'world', 'test']
# list_3.insert(3, 4)
# list_3.insert(0, 'makers')
# print(list_3)

# list.index(element, [start, end]) -> возвращает индекс элемента
# list_3 = [1, 2, 3, 'hello', 'world', 'test', 1, 2, 3]
# print(list_3.index(1))
# print(list_3.index(1, 7)) -> будет ошибка, если такого элемента нет в списке

# print(dir(list))

# list.clear() -> очищает список
# list_3 = [1, 2, 3, 'hello', 'world', 'test']
# list_3.clear()
# print(list_3)

# list.count(element) -> возвращает кол-во вхождений элемента в список

# list_3 = [1, 2, 3, 'hello', 'world', 'test', 1, 2, 3, 1, 1]
# print(list_3.count(1))
# print(list_3.count('hello'))

# list.pop([index]) -> удаляет элементы по индексно, возвращает удаленный элемент. По умолчанию удаляет последний элемент списка
list_3 = [1, 2, 3, 'hello', 'world', 'test', 1]
# print(list_3.pop())
# print(list_3.pop(0))
# print(list_3.pop(100)) IndexError: pop index out of range
# print(list_3)

# list.remove(element) -> удаляет element
# list_3.remove(1)
# list_3.remove(1)
# print(list_3)

# list.reverse() -> переворачивает список
# print(list_3)
# list_3.reverse()
# print(list_3)

# list.sort() -> сортирует список, состоящий из элементов одного типа. Сортирует в порядке возрастания, если указать reverse=True (по умолчанию reverse=False) то сортирует в порядке убывания
# list_3 = [5, 2, 4, 6, 7]
# list_3.sort(reverse=True)
# print(list_3)
# list_ = ['f', 'a', 'h', 'o', 'p', '_', ' '] # 
# list_.sort()
# print(list_)

# list.copy() -> поверхносное копирование
# list_ = ['hello', 1, 2, 3, 4]
# list_1 = list_.copy()
# # list_1 = list_
# list_.pop()
# print(id(list_))
# print(id(list_1))

'''======== Цикл for ========'''
# повторяющийся блок кода

# list_ = [1, 2, 3, 4, 5]
 

# for i in list_:
#     print(i)

# for i in list_:
#     print(i ** 2)

# str_ = 'hello'
# for i in str_:
#     print(i)

# for i in range(11):
#     print(i)

# for i in range(11):
#     if i % 2:
#         print(i,'нечетное')
#     else:
#         print(i, 'четное')

# for i in  range(1, 5):
#     print()
#     print(i)
#     for b in range(i):
#         print(b)





# list_ = [1, 'hello', 2, 3, 4, 5, 'test', 'world']
# list_index = []
# for i in list_:
#     if type(i) != int:
#         list_index.append(i)

# for i in list_index:
#     list_.remove(i)
# print(list_)

'''========== Tuple ========='''
# кортеж - неизменяемым, индексируемым, упорядоченный, итерируемым типом данных 

# литералы -> (,)
# 
a = 1, 2, 3
# a = (8,)
# print(type(a)) 

# print(dir(tuple))

'''========== Методы tuple ========'''
# tuple.count(element) -> считает кол_во вхождений element
a = 1, 2, 3, 4, 1, 'hello', [1, [1, 2, 3]]
# print(a.count(1))

# tuple.index(element) -> возвращает индекс первого вхождения element 
# print(a.index(1))

print(tuple([1, 2, 3, ['hello']]))






