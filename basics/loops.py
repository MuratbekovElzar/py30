'''Циклы'''
# повторяющийся блок кода

# for -> проходится по итерируемому объекту
# list -> [1, 2, 4]; str -> 'hello world'; set -> {'hello', 'test', 'makers' }; dict -> {1: 'a', 2: 'b'}; tuple -> (1, 4, 7, 8) 

# while -> работает пока условие верно

# while <логическое выражение>:
#     тело

'''Бесконечный цикл'''
# a = 0
# while True:
#     # a = a +1 
#     a += 1
#     print(f'hello {a}')

'''цикл, который никогда не заработает'''
# while False:
#     print('hello')


# a = 0
# while a < 10:
#     # a = a +1 
#     a += 1
#     print(f'hello {a}')

# a = 11
# while a > 0:
#     print(a)
#     a -= 1


# a = 0
# while a != 100:
#     a += 1
#     print(a)

# list_ = ' '
# print(bool(list_))

'''найти сумму цифер целого числа'''
# number = int(input('Enter number: '))
# 12345 -> 15
# 1 + 2 + 3 + 4 + 5 = 15

# sum_ = 0
# for i in str(number):
#     sum_ += int(i)

# print(sum_)

# sum_ = 0
# l = 0

# while l < len(str(number)):
#     # print(str(number)[l])
#     sum_ += int(str(number)[l])
#     l += 1
    

# print(sum_)

# '4134567432'
# '4' -> 4
# for i in 12345665432:
#     print(i)


'''бесконечный цикл for'''
# list_ = [1, 2]
# for i in list_:
#     list_.append(i)
#     print(i)

# string = 'hello'
# print(id(string))

# for i in string:
#     print(i)
#     string = string + 'hello' # меняется ссылка на объект
# print(id(string))



'''break, continue, pass, else'''
# break -> полностью выйти из цикла, досрочное прерываение цикла
# continue -> перейти к следующей итерации
# (начинает следующий проход цикла, минуя оставшееся тело цикла)

# a = 0
# while a != 10:
#     a += 1
#     print(a) 
#     if a == 5:
#         break
    
    
# for i in range(11):
#     if i == 4:
#         break
#     print(i)

# i = 0
# while i < 6:
#     i += 1
#     if i == 3:
#         print('Это 3')
#         continue
#         print('hello')
#     print(i)


# a = [1, 2, 3, 4, 'hello', 9, False]

# sum_ = 0
# for i in a:
#     # print(i)
#     if type(i) not in (int, float):
#         continue
#     sum_ += i
#     # print(sum_)
# print(sum_)


# for i in range(1, 4):
#     print(f'это i {i}')

#     for j in range(11):
#         print(f'это j {j}')
#         if j == 3: 
#             break
#     print('hello')
#     if i == 2: 
#         break

# while True:
#     print(1)
#     break
#     # continue
#     print(2)


'''
else в циклах -> проверяет, был ли произведен выход из цикла инструкцией break или 'естественным' путем. Блок кода в else выполнится только в том случае, если выход из цикла был без break
'''
# for i in range(1, 11):
#     if i == 20:
#         break
#     print(i)
# else:
#     print('выход из цикла без break')


'''pass'''
# ничего не делает, просто выступает в роли заглушки

# if 4 == 0:
#     pass

# for i in range(1, 11):
#     pass


"""
Напишите программу, которая будет находить наибольшую цифру натурального
числа. Натуральное число вводится с клавиатуры. Найти его наибольшую цифру.

"""
number = int(input('Enter number: '))
max_number = 0

while number > 0:
    if number % 10 > max_number:
        max_number = number % 10
    number = number // 10
print(max_number)
