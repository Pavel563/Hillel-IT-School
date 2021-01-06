# Задания
# data.json - файл с данными о некоторых математиках прошлого.

import json
import re


########################################################################################################################
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def read_json_file(filename):
    with open(filename, "r", encoding="utf-8") as data_file:
        data_list = json.load(data_file)
    return data_list


data = read_json_file("data.json")


########################################################################################################################
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.

def key_sorted_by_lastname(dict_data):
    name = re.findall(r'[A-Z]+[a-z]+', dict_data["name"])
    lastname = name[-1]
    return lastname


data_sorted_by_lastname = sorted(data, key=key_sorted_by_lastname)
print(data_sorted_by_lastname)

print('----------------------------------------------')


########################################################################################################################
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.

def key_sorted_by_death_date(obj_dict):
    years = re.findall(r'[0-9]+', obj_dict["years"])
    d_date = -int(years[-1]) if "BC" in obj_dict["years"] else int(years[-1])
    return d_date


data_sorted_by_death_date = sorted(data, key=key_sorted_by_death_date)
print(data_sorted_by_death_date)

print('----------------------------------------------')


########################################################################################################################
# 4. Написать функцию сортировки по количеству слов в поле "text"


def key_sorted_by_count_words(obj_dict):
    text = obj_dict["text"].split(' ')
    return len(text)


data_sorted_by_count_words = sorted(data, key=key_sorted_by_count_words)
print(data_sorted_by_count_words)
