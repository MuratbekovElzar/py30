'''======== Обработка исключений ========'''

'''
Ошибки -> проблемы с синтаксисом
1. SyntaxError: забыли двоеточие, скобку
2. IndentationError: неправильный отступ
3. TabError: неправильная табуляция
'''
# 2f = 8

# Исключения: (код написан правильно, но работает не так, как ожидалось)
# 1.  ArithmeticError 
#    ZeroDivisioError
# 2. ValueError 
# 3. NameError
# 4. TypeError
# 5. KeyError
# 6. IndexError
# 7. AttributeError
# 8. ImportError
# 9. BaseException (прородитель)

ZeroDivisionError # при делении на 0
# 8 / 0
# 4 // 0
# 3 % 0

ValueError # вызывается при распаковке, переводе одного типа данных в другой
# int('hello')
# a = 'asd'
# k, b = a

NameError # когда обращаемся к несуществующей переменной

# print(b)


TypeError # когда передаем в функцию, метод меньше или больше аргументов, чем требуется

# for i in 2345677:
#     print(i)
# [].append()
# [].append(1, 2, 3)
# '5' + 5

KeyError # при обращении к несуществующему ключу

dict_ = {'a': 1}
# dict_['b']
# dict_.pop('b')

IndexError # при обращении к несуществующему индексу

list_ = ['a', 'b', 'c']
# list_[4]
# list_.pop(3)


AttributeError # когда обращаемся к несуществцющему методу или атрибуту объекта

# a = 12341
# a.upper()
# b = [1, 2, 3]
# b.discard()

ImportError # неправильный импорт

# import math
# from math import pi2


# BaseException -> прородитель


'''===== try except ====='''
# чтобы код не прекращал свою работу

'''Синтаксис'''

# try:
#     тело try
#     # код, который может вызвать ошибку
# except:
#     тело except
#     # код, который сработает, если в try возникнет ошибка
# else:
#     тело else
#     # код, котрый отработает, если в блоке try не возникло ошибки
# finally:
#     тело finally
#     # код, который отработает в любом случае

# def division(num1, num2):
#     return num1/num2

# try:
#     num = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     res = num / num2
#     # res = division(num, num2)
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели не число или на ноль делить нельзя')
    
#     num = int(input('Введите число: '))
#     num2 = int(input('Введите число: '))
#     res = num / num2
#     # res = division(num, num2)
#     print(res)

# # except ZeroDivisionError:
# #     print('На ноль делить нельзу')
# else:
#     print(f'{num} / {num2} = {res}')

# finally:
#     print('Пока')


# try:
#     while True:
#         print('f')
# except KeyboardInterrupt:
#     print('ctrl + c')

# dict_ = {key: key ** 2 for key in range(11)if key % 2 == 0}
# print(dict_)
# try:
#     dict_ = {key: key ** 2 for key in range(11)if key % 2 == 0}
#     # print(dict__)
#     value = dict_[100]
#     print(value)
# # except:
# #     pass
# except NameError:
#     print('Переменна dict__ не объявленна ')
# except KeyError:
#     print('такого ключа нет')
#     print(dict_)
#     key = int(input('Введите ключ: '))
#     print(dict_[key])

# from math import factorial as fact 
# fact()

# try:
#     i = int(input())
# except Exception as e:
#     print(e)

"""напишите программу, в которая будет принимать от пользователя два числа и складывать их"""

# try:
#     num1 = int(input('Введите первое число: '))
#     num2 = int(input('Введите второе число: '))
# except ValueError:
#     # print('Вы ввели не число')
#     # num1 = 10
#     # num2 = 99
#     print(num1 + num2)
# else: 
#     print('ошибка не возникла')
# finally:
#     print(num1 + num2)

# count = 0
# while True:
    
#     try:
#         a = int(input('Введите число: '))
#         b = int(input('Введите число: '))
#         res = a + b
#     except ValueError:
#         a = int(input('Введите число: '))
#         b = int(input('Введите число: '))
#         res = a + b
    
#     count += 1
#     print(res, count)
#     if count == 3:
#         break


'''======   raise   ======'''
# Исскуственно вызывать ошибки
# try:
#     age = int(input('введите возраст: '))
#     if age < 18:
#         raise ValueError('Доступ закрыт')
#     print('чек')
# except ValueError:
#     print('вы ввели не число или вам нет 18')


# a = 1
# b = 2
# if a < b:
#     raise Exception('b должно быть меньше a')

 


