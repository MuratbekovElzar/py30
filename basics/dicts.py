'''========= Словари (dict) ========'''
# изменяемый, неидексируемый, упорядолченный, итерируемый тип данных

# {ключ: значение}

# {} -литералы
'''Способы создания словарей'''
# dict_ = {'a': 'hello'}
# print(type(dict_))

# dict_1 = dict(a='hello', b=1)
# print(dict_1)

# dict_ = dict((['key', 'value'], ['o', 'v']))

# dict_ = dict(['12', 'cd'])
# print(dict_)

# key, value = 'ab'
# print(key, value)



#  ключи должны быть неименяемым типом данных

# {[]: 1} -> TypeError: unhashable type: 'list'

# ключи -> должны быть уникальными

# a = {1: 'hello', 1: 'world', 1: 1}
# print(a) #{1: 1}

# значения -> могут относиться к любому типу данных

dict_ = {
    'name': 'Aiana',
    'last_name': None, 
    'email': True, 
    'info': [1, 2, 3, 4]
}

# print(dict_['info']) #получение значения по ключу

# dict_['email'] = 'test@gmail.com' #изменение значения по ключу
# print(dict_)
# dict_['email1'] # KeyError: 'email1'
# dict_['email1'] = 12 # добавляет новую пару в словарь {...,'email1': 12} 

# print(dict_)

'''========= Методы словарей ========'''
# print(dir(dict))

# dict.items() -> возвращает все пары в словаре, в виде списка с кортежами
# print(dict_.items()) #dict_items([('name', 'Aiana'), ('last_name', None), ('email', True), ('info', [1, 2, 3, 4])])

# for key, value in dict_.items():
#     # print(i)
#     print(key, '--->', value)

# a, b, c = (1, 2, 3)
# print(a, '---> ', b, '--->', c)


# dict.values()  -> для получения всех значений словаря

# print(dict_.values())
# for i in dict_.values():
#     print(i)


# dict.keys() -> для получения всех ключей словаря

# print(dict_.keys()) 
# for i in dict_.keys():
#     print(i)


# dict.clear() -> очищает словарь
# dict_.clear()
# print(dict_)

# del dict_ -> удаление объекта
# print(dict_)

# dict.copy() -> возвращает копию словаря
# dict_copy = dict_.copy()
# print(dict_copy)


# dict.fromkeys(seq, [default]) -> создает словарь с ключами из последовательности (seq) и значением default (None)

list_ = ['name', 'hello', 'test']
# dict_ = dict.fromkeys(list_, 1)
# print(dict_)

dct = dict.fromkeys('as')
# print(dct)

# dict.get(key, [default]) -> возвращает значение по ключу, если такого ключа нет, не бросает искючение (вызывает ошибку), а возвращает default, если default не указан, возвращает None

# dict[key] -> бросает исключение, если такого ключа нет (вызывает ошибку)

# dict_ = {1: 'one', 2: 'two'}
# print(dict_.get(1, 'no such key')) # one
# print(dict_.get(3, 'no such key')) # 'no such key'
# print(dict_.get(3)) # None
# print(dict_[3]) # KeyError


# dict.update(new_dict) -> добавляет new_dict в наш словарь

# dict_ = {1: 'one', 2: 'two'}
# # dict_[5] = 'five' # добавляет только одну пару
# dict_.update({3: 'three', 4: 'four'})
# new_dict = {5: 'five', 6: 'six'}
# dict_.update(new_dict)
# print(dict_)


# dict.setdefault(key, [default_value]) -> 1. Работает как get
# 2. если  ключа нет, создает новую пару key: default_value, если не указать default_value -> None

# 1.
dict_ = {1: 'one', 2: 'two'}
# print(dict_.setdefault(1)) # one

# 2.
# print(dict_.setdefault(3, 'three')) # three
# print(dict_.setdefault(4)) # None
# print(dict_)


'''Удаление элементов словаря'''
# dict.pop(key, [message]) -> удаляет пару улюч, значение и возвращает значение, если ключа нет выводит message (по умолчанию бросает исключение)

dict_ = {'a': 'one', 'b': 'two', 'c': 'three'}

# deleted = dict_.pop('a')
# print(dict_, deleted)
# print(dict_.pop('d')) #KeyError: d
# print(dict_.pop('d', 'no such key')) #'no such key'
# print(dict_, deleted)

# dict.popitem() -> удаляет последнюю пару ключ и значение и возвращает ключ и значени
# lifo fifo
# print(dict_.popitem()) # ('c', 'three')
print(dict_)


'''поменять местами ключи и значения'''
# new_dict = {}
# for key, value in dict_.items():
#     new_dict.update({value: key})
#     # new_dict[value] = key

# print(new_dict)


# Дан словарь dict1. Создайте словарь dict2, с ключами как в словаре dict1, а значениями пусть будут произведение чисел внутренних словарей
dict1 = {'a': {'d': 1, 'e': 4}, 'b': {'f': 2, 'j': 4}, 'c': {'h': 3, 'i': 9}}
dict2 = {}
for key, value in dict1.items():
  v = value.values()
  new_value = 1
  for i in v:
        new_value *= i
        # new_value = new_value * i
#   print(new_value)        
  dict2.update({key: new_value})
# Вывод:
# {'a': 4, 'b': 8, 'c': 27}
# print(dict2)


# print(a := 12)
# print(a == 12)

# a = 19
# if a == 19:
#     pass

# = -> присваивание
# == -> сравнение


