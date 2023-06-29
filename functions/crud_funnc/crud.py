'''CRUD'''
# create read update delete
# hash() -> возвращает хэш значение объекта, если оно есть


# from  scopes import couter

db = [
    {'username': 'hello', 'password': hash('1234test')},
    {'username': 'JhonSnow', 'password': hash('19283746')}
]

def in_database(username: str) -> bool:
    for user in db:
        if user['username'] == username:
            return True
    return False

def get_user(username: str, password: str) -> dict:
    if not in_database(username):
        raise Exception('Такого пользователя нет')
    for user in db:
        if user['username'] == username:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный')
            else:
                return user

# print(get_user('hell', '1234tes'))

def register(username: str, password: str, password_confirm: str) -> str:
    if in_database(username):
        raise Exception('Пользователь с таким именем уже существует')
    if password != password_confirm:
        raise Exception('Пароли не совпадают')
    # print('Все ок')
    new_user = {'id': couter(), 'username': username, 'password': hash(password)}
    db.append(new_user)
    return 'Вы успешно зарегистрировались'


def login(username: str, password: str) -> str:
    get_user(username, password)
    return 'Вы успешно зашли на свой аккаунт'


def change_password(username, password):
    user = get_user(username, password)
    new_password = input('Введите новый пароль: ')
    index = db.index(user)
    user_from_db = db[index]
    user_from_db['password'] = hash(new_password)
    return 'Пароль успешно обнавлен'


def delete_account(username: str, password: str):
    user = get_user(username, password)
    db.remove(user)
    return 'Аккаунт успешно удален'



def main():
    print('Добро пожаловать!')
    while True:
        try:
            action = input('1-регистрация, 2-login, 3-изменить пароль, 4-удалить аккаунт, 5-выйти: ')
            if action == '5':
                break
            elif action == '1':
                username = input('Введите имя пользователя: ')
                password = input('Введите пароль: ')
                password1 = input('Введите подтверждение пароля: ')
                print(register(username, password, password1))
                print(db)
            elif action == '2':
                username = input('Введите имя пользователя: ')
                password = input('Введите пароль: ')
                print(login(username, password))
            else:
                print('Не корректный ввод')

        except Exception as error:
            print(error)

# if __name__ == '__main__': 
#     main()

# main()
    
    





