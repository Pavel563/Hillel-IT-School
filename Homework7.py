import random

########################################################################################################################
# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

my_list = []

while len(my_list) != 20:
    my_list.append(random.randint(1, 100))
print(my_list)

########################################################################################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.

triangle = {"A": (random.randint(-10, 10),
                  random.randint(10, 10),
                  random.randint(-10, 10)),
            "B": (random.randint(-10, 10),
                  random.randint(10, 10),
                  random.randint(-10, 10)),
            "C": (random.randint(-10, 10),
                  random.randint(10, 10),
                  random.randint(-10, 10))
            }
print(triangle)

########################################################################################################################
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***

my_str = "I'm the string"


def my_print(my_str):
    print('***' + my_str + '***')


my_print(my_str)

########################################################################################################################
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 45}, {"name": "Michel", "age": 50}, {"name": "Jack", "age": 15}]
count = 0
sum_age = 0
min_age = 100
len_name = 0
younger = []
long_name = []
for person in persons:
    if person["age"] < min_age:
        min_age = person["age"]
    if len(person["name"]) > len_name:
        len_name = len(person["name"])
    sum_age += person["age"]
    count += 1

for person in persons:
    if min_age == person["age"]:
        younger.append(person["name"])
younger = ', '.join(younger)

for person in persons:
    if len_name == len(person["name"]):
        long_name.append(person["name"])
long_name = ', '.join(long_name)
result = sum_age // count
print(f"Самый молодой: {younger}")
print(f"Самое длиное имя: {long_name}")
print(f"Средний возраст: {result}")

########################################################################################################################
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {"name": "John", "age": 25, "job": "Developer"}
my_dict_2 = {"name": "Michel", "age": 30}
list_a = []
list_b = []
dict_c = {}
new_list = []
new_dict = {}
for key, value in my_dict_1.items():
    if key in my_dict_2:
        list_a.append(key)
        new_dict[key] = [value, my_dict_2[key]]
    if key not in my_dict_2:
        list_b.append(key)
        dict_c[key] = value
        new_dict[key] = value
print(list_a)
print(list_b)
print(dict_c)
print(new_dict)
