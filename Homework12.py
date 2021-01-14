# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

# import requests
#
# import csv
#
#
# def get_quotes(count):
#     quote_dict_list = []
#     i = 0
#     url = "http://api.forismatic.com/api/1.0/"
#
#     params = {"method": "getQuote",
#               "format": "json",
#               "key": 1,
#               "lang": "ru"}
#     while i != count:
#         params["key"] = i
#         r = requests.get(url, params=params)
#         quote = r.json()
#         quote_dict = {"Author": "", "Quote": "", "URL": ""}
#         if len(quote["quoteAuthor"]) > 0:
#             quote_dict["Author"] = quote["quoteAuthor"]
#             quote_dict["Quote"] = quote["quoteText"]
#             quote_dict["URL"] = quote["quoteLink"]
#             quote_dict_list.append(quote_dict)
#             i += 1
#     return quote_dict_list
#
#
# quotes = get_quotes(10)
#
#
# def key_sorted_by_name(quote):
#     return quote["Author"]
#
#
# quotes = sorted(quotes, key=key_sorted_by_name)
#
#
# def write_quotes_csv(filename="quotes.csv"):
#     with open(filename, "w", encoding="utf-8") as csv_file:
#         fieldnames = {"Author": "", "Quote": "", "URL": ""}
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',')
#         writer.writeheader()
#         writer.writerows(quotes)
#
#
# write_quotes_csv()

########################################################################################################################
# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.


def read_txt_file(filename):
    with open(filename, "r") as txt_file:
        data = []
        for line in txt_file.readlines():
            if line.find("'s") >= 0 and (line.find("birthday") >= 0 or line.find("death") >= 0):
                data.append(line)
    return data


authors = read_txt_file("authors.txt")
print(authors)

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]

import re


def make_dict():
    authors_dict_list = []
    for text in authors:
        name = re.findall(r"[a-zA-Z. ]+[']", text)
        name = [i.strip(' \'') for i in name]
        name = "".join(name)
        numbers = re.findall(r'[0-9]+', text)
        dd = numbers[0] if len(numbers[0]) > 1 else '0' + numbers[0]
        if 'January' in text:
            mm = '01'
        elif 'February' in text:
            mm = '02'
        elif 'March' in text:
            mm = '03'
        elif 'April' in text:
            mm = '04'
        elif 'May' in text:
            mm = '05'
        elif 'June' in text:
            mm = '06'
        elif 'July' in text:
            mm = '07'
        elif 'August' in text:
            mm = '08'
        elif 'September' in text:
            mm = '09'
        elif 'October' in text:
            mm = '10'
        elif 'November' in text:
            mm = '11'
        elif 'December' in text:
            mm = '12'
        yyyy = numbers[-1]
        date = f"{dd}/{mm}/{yyyy}"
        author_dict = {"name": name, "date": date}
        authors_dict_list.append(author_dict)
    return authors_dict_list


authors_list = make_dict()
print(authors_list)

# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.
