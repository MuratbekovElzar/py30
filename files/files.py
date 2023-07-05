'''Работа с файлами. Модули и пакеты. JSON'''

'''========== Работа с файлами =========='''

# open('path/file_name.txt', режим) -> функция, которая позволяет открыть файл и работать с ним

# file1 = open('test.txt')
# print(file1.read())
# file1 = open('test.txt', 'w')
# file1.write('hello')
# print(file1)

'''========= Режимы ========'''
# 1. r (read) -> Открывает файл для чтения. Режим по умолчанию. Если такого файла нет, то ошибка
# file1 = open('file_name.py')
# file1 = open('file_name.py', 'r')

# 2. w (write) -> Открывает файл для записи. Перезаписывает весь файл (очищает файл, потом записывает). Если такого файла нет, то создаст его

# file1 = open('test1.py', 'w') -> создает пустой файл

# 3. a (append) -> Открывает файл для добавления. Все новое добавляется в конец файла, если такого файла нет, то создаст его

# file1 = open('hello.txt', 'a')

# 4. x(exclusive) -> Создает файл с уникальным названием. Если в директории есть такой файл, то ошибка
# file1 = open('e.txt', 'x')

# 5. t (text) -> Открывает файл в текстовом виде
# rt == r

# 6. b (binary) -> Открывает файл в юинарном виде
# file1 = open('test.txt', 'rb')
# rb
# wb
# ...

# 7. + -> открывает файл в режиме чтения и в режиме записи
# r+
# w+
# file = open('test.txt', 'w+')
# print(file.read())
# file.seek(0)
# print(file.read())
# # file.seek(4)
# print(file.tell())
# file.seek(15)
# print(file.tell())
# print(file.read())
# file.write('\nMakers')
# file.close()
# print(file.closed) -> для проверки закрытия файла


# file.seek(0) -> перемещает курсор в начало файда
# file.close() -> закрывает файл

# file.tell() -> Возвращает индекс, где находится курсор

'''========== Методы режима 'r' ========='''
# 1. read(index) -> считывает весь файл, если указть считывает до index 
# 2. readline(кол-во символов) -> считывает одну строку из файла
# 3. readlines(кол-во символов) -> считывает построчно и сохраняет их в виде списка

# file = open('test.txt')
# print(file.read(10))
# file.close()

# file = open('test.txt')
# print(file.readline())
# print(file.readline())
# print(file.readline())
# file.close()

# file = open('test.txt')
# # print(file.readlines())
# for line in file:
#     print(line)
# file.close()

'''========= Методы режимв "w" ========='''
# 1. write('string') -> записывает string в файл
# 2. writelines(list) 

# f = open('test.txt', 'w')
# f.write('Привет, вас беспокоит компания  Makers')
# f.write('Привет, вас беспокоит компания  Makers')
# f.close()

# f = open('test.txt', 'w')
# f.writelines(['hello world\n', 'Привет\n', 'Makers\n'])
# f.close()


# Контекстный менеджер. Открывает файл и при любом раскладе будет его закрывать
# with open('file_name.txt', 'режим') as file:
    # тело

# with open('test.txt', 'r') as file:
#     data = file.read()
#     print(data)


'''============= JSON ============='''
'''
JSON (JavaScript Object Notation) -> Единый текстовый формат передачи данных между приложениями, компьтерами и языками програмирования
'''


# {
#     "id": 1,
#     "author": "usenovatest@gmail.com",
#     "posts": null
# }
# Пример JSON

# Разница типов
# Python    JSON
# None      null
# dict      object
# list      Array
# str       String
# int       Number
# float     Number
# True      true
# False     false

# import json
# print(dir(json))

'''
Сериализация и десириализация
'''
# Сериализация -> запись данных в JSON (перевод Python объекта в JSON)
# dump() -> метод записывает  объект Python в файл в формате json
# dumps() -> метод записывает Python объект в json строку

'''Десириализация -> (Чтение данных из JSON)  (перевод JSON в Python объект)'''
# load(file) -> метод, который считывает файл в формате JSON и переводит его в объект Python
# loads(string) -> метод, который считывает текст/строку в формате JSON и переводит в объект Python

import json

# person = '{"name" : "Sam", "age": 25, "is_working": false}'
# result = json.loads(person)
# print(result)
# print(type(person), type(result))


# with open('file.json', 'w+') as file:
#     person = '{"name" : "Sam", "age": 25, "is_working": false}'
#     file.write(person)
#     file.seek(0)
#     data = json.load(file)
#     print(data.get('name'))

# json.dumps(python_object) -> переводит Python объект в JSON

# data = {
#     'email': 'testUser@gmail.com',
#     'password': '12345678'
# }
# data_json = json.dumps(data)
# print(type(data_json))


# # json.dump(python_object, file)
# data = {
#     'email': 'testUser@gmail.com',
#     'password': '12345678'
# }

# with open('file.json', 'w+') as file:
#     json.dump(data, file)
#     file.seek(0)
#     print(type(file.read()))

# # CSV JSON


# print('1\n2\n3')