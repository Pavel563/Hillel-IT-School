########################################################################################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

my_list = ['sdcs', 'sdcwe', 'qwlkmf', 'oirv']
new_list = []
for index, string in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(string)
    else:
        new_list.append(string[::-1])
print(new_list)

########################################################################################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".


my_list = ["ajn", "guyj", "buyvjuyv", "agvyyt"]
new_list = []
for string in my_list:
    if string.startswith("a"):
        new_list.append(string)
print(new_list)

########################################################################################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.


my_list = ["jan", "guyj", "buyavjuyv", "gvyyt"]
new_list = []
for string in my_list:
    if 'a' in string:
        new_list.append(string)
print(new_list)

########################################################################################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.


my_list = ["jan", 49, "guyj", 54, "buyavjuyv", 88, "gvyyt", "gcfc", 99]
new_list = []
for string in my_list:
    string = str(string)
    if string.isalpha():
        new_list.append(string)
print(new_list)

########################################################################################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.


my_str = "asdfgqwertyasdfg"
my_list = []
for symb in my_str:
    count = my_str.count(symb)
    if count == 1:
        my_list.append(symb)
print(my_list)

########################################################################################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "qwertyasdfg"
my_str_2 = "qwertyzxcvbzx"
my_list = []
for symb in my_str_1:
    if symb in my_str_1 and symb in my_str_2:
        my_list.append(symb)
print(my_list)

########################################################################################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.


my_str_1 = "qwertyasdfgy"
my_str_2 = "qwertyzxcvbt"
my_list = []
for symb in my_str_1:
    count1 = my_str_1.count(symb)
    count2 = my_str_2.count(symb)
    if symb in my_str_1 and symb in my_str_2:
        if count1 == 1 and count2 == 1:
            my_list.append(symb)

print(my_list)

########################################################################################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

name = {"l_name": "Ivanov",
        "f_name": "Petr",
        "age": 35}
address = {"country": "Ukraine",
           "city": "Dnipro",
           "street": "Polya"}
job = {"availability": "Yes",
       "position": "Python developer"}
person = {"name": name,
          "address": address,
          "job": job}

print(person)

########################################################################################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло


cake = {"flour": "300 grams",
        "milk": "200 milliliter",
        "oil": "100 grams",
        "agg": "4 pieces"}
cream = {"sugar": "250 grams",
         "oil": "150 grams",
         "vanilla": "30 grams",
         "sour cream": "200 grams"}
glaze = {"cocoa": "40 grams",
         "sugar": "100 grams",
         "oil": "120 grams"}
cake_composition = {"cake": cake,
                    "cream": cream,
                    "glaze": glaze}
print(cake_composition)
