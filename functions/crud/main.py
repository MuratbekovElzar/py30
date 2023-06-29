from views import *

def main():
    print('Привет, Тебе доступны следующие действия: 1 - listing, 2 - retrive, 3 - create, 4 - update, 5 - delete ')
    choise = input('Выберите действие: ')
    if choise == '1':
        print(get_courses())

    elif choise == '2':
        id = int(input('Введите id курса: '))
        print(get_course(id))
    
    elif choise == '3':
        print(create_course())
    
    elif choise == '4':
        id = int(input('Введите id курса: '))
        print(update_course(id))
    
    elif choise == '5':
        id = int(input('Введите id курса: '))
        print(delete_course(id))

    else:
        print('Такого действия нет')
    
    ask = input('Хотите продолжить? да/нет: ')
    if ask.lower() == 'да':
        main()
    else:
        print('Пока')

main()
