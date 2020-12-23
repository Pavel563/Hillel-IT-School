import random

########################################################################################################################
# 1. Считать данные из файла domains.txt
# Названия интернет доменов поместить в список (названия сохранить без точки).


with open("domains.txt", 'rt', encoding="utf-8") as domains_file:
    domains = []
    for line in domains_file.readlines():
        line = line.replace('.', '')
        domains.append(line.strip())
print(domains)

########################################################################################################################
# 2. Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

with open("names.txt", 'r') as name_file:
    names = []
    for line in name_file.readlines():
        line = line.replace('.', '')
        names.append(line.split('\t')[1])
print(names)


########################################################################################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
#
# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com

def create_number():
    number = random.randint(100, 999)
    return number


def create_str():
    string = [chr(number) for number in range(ord('a'), ord('z') + 1)]
    string = ''.join([random.choice(string) for element in range(random.randint(5, 7))])
    return string


def create_email(names, domains):
    name = random.choice(names)
    domain = random.choice(domains)
    number = create_number()
    string = create_str()
    result = (f"{name}.{number}@{string}.{domain}")
    return result


e_mail = create_email(names, domains)
print(e_mail)
