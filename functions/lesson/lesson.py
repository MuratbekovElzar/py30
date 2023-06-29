def add_one(x: int) -> int:
    return x + 1


def division(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError
    return x / y


def sum_(num1: int, num2: int) -> int:
    return num1 + num2


'''
является ли строка палиндром
оно довод -> True
на привет -> False
'''

def p(x: str) -> bool:
    if x.lower() == x[::-1].lower():
        return True
    else:
        return False


# 5! -> 1*2*3*4*5
def count_factorial(number: int) -> int:
    factorial = 1
    for i in range(2, number+1):
        factorial *= i
    return factorial

# print(count_factorial(5))


# def list_count(l: list):
#     l

a = 1, 2, 3