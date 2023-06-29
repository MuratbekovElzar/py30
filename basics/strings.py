'''=========== Строки =========='''
# неизменяемый тип данных, который предназначен для хранения последовательности символов, заключенной в одинарныйе или двойные кавычки


string = "Строка"
string2 = 'Строка'
# string3 = "неправильно'
string4 = "don't"
string5 = 'he: "hello"'

string6 = '''
hello
hkdfl'
adfshbger"
asdfsgh''""""""
'''
string7 = """
hello
hkdfl
adfshbger
asdfsgh
"""


# print(string6)


'''Экранированные последовательности'''
# последовательность символов, начинающаяся с  -> \
'\n' # -> перенос на следующую строку
'\t' # -> табуляция
'\\' # -> для отображения \
'\'' # -> для отоюражения '
'\"' # -> для отображения "
'\r' # -> возвращает каретку в начало строки
'\v' # -> вертикальная табуляция



# string = 'hello vfyxucgivhbojnpkmolpl;kbhvgjcfhjgvhkbjln;\'fuibolp;lmkpnjbhivgcf\\'
# string = 'hello\vmakers\vincubator'
# print(string)  

'''конкатенация -> склеивание строк'''
str_1 = 'Hello '
str_2 = 'World'

# print(str_1 + ' ' + str_2)


'''Дублирование строк'''

# print(str_1, str_1, str_1)
# print(str_1*100)

'''======== Форматирование строк ======='''
# 1. с использование %
# 2. с использованием метода .format()
# 3. интерполяция строк (f-строки)

# %
# name = input('Enter your name: ')
# a = input()
# result = 'Hello, %s' %name
# print(result)

# .format()
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# test = input('Enter your age: ')
# result = 'hello, {} {} {}'.format(name, age, test)
# print(result)

# f-строки

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# test = input('Enter your age: ')
# result = f'hello {name} your are{age} years old  {test} '
# print(result)


'''=========== Индексы =========='''
# Порядковый номер символов в строке
' h e l l o   w o r l d'
# 0 1 2 3 4 5 6 7 8 9 10
#-11-10-9-8-7-6-5-4-3-2-1
str_ = 'hello world test hello'
# print(str_[0]) # получение первого эл-та строки 'h'
str_[1] # 'e'
str_[-1] #получение последнего элемента строки 'd'

'''========= Срезы ========='''
# получение подстраки (какой-то части строки)
# Синтаксис [начало : конце : шаг]
# print(str_[:5])
# print(str_[6:])
# print(str_[:-2])

'переверните строку используя срезы '
'''
пример: str_ = 'hello'
вывод: 'olleh'
'''
# str_ = 'hello'
# print(str_[-2::-1])
# Срезы по индексу -> [3:] -> начиная с 3 индекса до самого конца, [:6]-> с 0 индекса до 6(не включительно), [::]  [:] [0::1] -> вся строка, [::-1] -> перевернуть строку

'''=========== Методы строк =========='''
# метод - та же самая функция, но обращаемся к нему через точку

# print(dir('hello'))

# методы на is -> проверяют
# возвращают True/False
# str.isalnum() -> состоит ли строка только из букв и/или чисел
# str.isalpha() -> состоит ли строка только из букв
# str.isdigit() #->  состоит ли строка толлько из чисел
# str.islower() #-> находится ли строка в нижнем регистре
# str.isupper() # -> состоит ли строка из символов верхнего регистра
# str.isspace() # -> состоит ли строка из неотображаемых символов (пробелы и экранированные последовательности)
# str.isnumeric() # ->  состоит ли строка толлько из чисел

# print('hello9'.isalpha())
# print('1234 '.isdigit())


# str.upper() -> переводит в верхний регистр
# str.lower() -> переводит в гижний регистр

# str_ = 'Makers'
# a = str_.lower() #makers
# print(a)

# str_ = 'Makers'
# a = str_.upper() #MAKERS
# print(a)

# str.title() -> каждое слово в строке запишет с заглавной буквы

# str.capitalize() -> только самое первое слово в строке запишет с заглавной 

# str_ = 'hello Makers'
# print(str_.title()) # Hello Makers
# print(str_.capitalize()) #Hello makers

# strip() -> убирает пробелы в начале и в конце строки (rstrip, lstrip)
# len() -> возвращает длину строки
# 
# a = input('here: ')
# b = a.strip()
# print(len(a), a, len(b), b)


# str.replace(old, new, count) -> заменяет old значение в строке на new, count - отвечает за кол-во замен

# str_ = 'ha ha ha a'
# new_str = str_.replace('ha', 'new', 1)
# print(new_str)

# str.split('разделитель') -> делит строку по разделителю и возвращает список. разделитель по умолчанию -> пробел

# a = 'hello makers boot incubator test'
# b = a.split('t')
# print(b)

# 'объединитель'.join(list_)  -> переводи список в тип данных строки
 
# ''.join(['a', 'b', 'c']) -> 'abc'