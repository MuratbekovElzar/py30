# Вам нужно реализовать функционал CRUD курса. 

# При создании курса Пользователь должен заполнить следующие поля:

# - Категория - ограничить выбор категории из следующих:
#     - Веб-разработка
#     - Разработка мобильных приложений
#     - Разработка игр
# - Подкатегория - ограничить выбор подкатегории из следующих:
#     - Python
#     - JavaScript
#     - Java
# - Заголовок курса (максимум 60 символов)
# - Описание к курсу (минимум 10 слов)
# - Уровень - ограничить выбор уровня из следующих:
#     - начальный
#     - средний
#     - профессиональный
# - Цена курса  - все суммы конвертировать в сомы
#     - валюта
#     - сумма

categories = [
    'веб-разработка', 
    'разработка мобильных приложений', 
    'разработка игр'
]

subcategories = [
    'python', 
    'javaScript', 
    'java'
]

levels = [
    'начальный', 
    'средний', 
    'профессиональный'
]

currensies = [
    'dollar',
    'сом'
]

id = 0
def get_id():
    def inner():
        global id 
        id += 1
    inner() 
    return id
    
db = {
    get_id(): {
        'category': 'Веб-разработка', 
        'subcategory': 'Python', 
        'level': 'начальный',
        'title': 'Веб-разработка для начинающих',
        'description': 'Изучать любой предмет на практике намного интереснее и эффективнее, чем сидя за партой во время лекции. Это особенно применимо к программированию! Если ты хочешь научиться получить практический опыт на Python и узнать как же думает программист, то ты пришел в нужное место.',
        'price': {'currency': 'dollar', 'amount': 50}
    },
}

# [{"id": 0, "name": "Iphone 13 Pro Max", "price": 1000}, {"id": 1, "name": "Samsung Galaxy S22 Ultra", "price": 1200}, {"id": 4, "name": "Iphone 8s", "price": 400.0}, {"id": 5, "name": "Iphone XR", "price": 800.0}]
# # print(db)

def get_courses():
    return db

def get_course(id: int):
    course = db.get(id)
    if course:
        return course
    else:
        raise Exception('Такого курса нет')
    



            
def validate_data(data):
    if data['category'].lower() not in categories:
        raise Exception('Такой категории нет')
    if data['subcategory'].lower() not in subcategories:
        raise Exception('Такой подкатегории нет')
    if data['level'].lower() not in levels:
        raise Exception('Такого уровня нет')
    if len(data['title']) > 60:
        raise Exception('Заголовок курса не должен превышпть 60 символов')
    if len(data['description'].split()) < 10:
       raise Exception('Слишком короткое описание, минимум 10 слов')
    # if currensy not in currensies:
    #     return 'Мы '
    if data['price']['currency'] == 'dollar':
        data['price']['currency'] = 'сом'
        data['price']['amount']*= 87.3 
    return data

# data = db[1]
# (print(validate_data(data)))

            

def create_course():
    #     product = {
    #     'id': get_id(),
    #     'title': input('Vvedite nazvaniye producta: '),
    #     'price': float(input('Vvedite price producta: ')),
    #     'description': input('Vvedite opisaniye: ')
    # }
    data = {
        'category': input(f'Выберите категорию: {categories} '), 'subcategory': input(f'Выберите подкатегорию: {subcategories} '), 'level': input(f'Выберите уровень: {levels} '), 'title': input('Введите название: '), 'description': input('Введите описание курса: '), 'price':{'currency': input('Введите  валюту (dollar/сом): '), 'amount': int(input('Ведите стоимость: '))}}
    validated_data = validate_data(data)
    new_course = {get_id(): validated_data}
    db.update(new_course)
    return 'Курс упешно создан'

# print(create_course())

def delete_course(id: int):
    try:
        db.pop(id)
    except KeyError:
        return f"Курса с id - {id} нет"
    
def update_course(id: int):
    course = get_course(id)
    print(course)
    
    choice = input('Что вы хотите изменить(title-1, price-2, description-3): ')
    if choice == '1':
        course['title'] = input('Vvedite novoe nazvaniye: ')
    elif choice == '2':
        course['price']['amount'] = float(input('vvedite novyi prcie: '))
    elif choice == '3':
        course['description'] = input('Vvedite novoe opisaniye: ')
    else:
        return 'Invalid choice to update!'
    validate_data(course)
    db.update(course)
    return course
    

