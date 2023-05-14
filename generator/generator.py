import random

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()

# Создает класс с данными пользователя, заполненными через Faker
def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(10, 80),
        department=faker_ru.job(),
        salary=random.randint(100, 1000),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )

# in progress
# def generated_file():
#     path = rf'C:\Users\Forsworn\PycharmProjects\pythonProject1{random.randint(0, 999)}.txt'
#     file = open(path, 'w+')
#     file.write(f'Hello World{random.randint(0, 999)}')
#     file.close()
#     return file.name, path
