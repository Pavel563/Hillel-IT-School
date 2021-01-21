# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroPython_18_11/blob/main/Homeworks/lesson8.txt

# Суть задания - сздать класс EmailGenerator
#
# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")
#
# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names(). (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = self.get_domains()
# self.names = self.get_names()
#
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
#
# 4. Написать метод экземпляра класса generate_email() (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com

import random


class EmailGenerator:

    def __init__(self, domain_address, name_address):
        self.domain_address = domain_address
        self.name_address = name_address
        self.domains = self.get_domains()
        self.names = self.get_names()

    def __repr__(self):
        return f"len domains = {len(self.domains)}, len names = {len(self.names)}"

    def get_domains(self):
        with open(self.domain_address, 'r', encoding="utf-8") as domains_file:
            domains = []
            for line in domains_file.readlines():
                line = line.replace('.', '')
                domains.append(line.strip())
        return domains

    def get_names(self):
        with open(self.name_address, 'r') as names_file:
            names = []
            for line in names_file.readlines():
                line = line.replace('.', '')
                names.append(line.split('\t')[1])
        return names

    def generate_email(self):
        random_str = ''.join([chr(random.randint(97, 122)) for symbol in range(random.randint(5, 7))])
        e_mail = (f'{random.choice(self.names)}.{random.randint(100, 999)}@{random_str}.{random.choice(self.domains)}')
        return e_mail


email_generator = EmailGenerator("domains.txt", "names.txt")
e_mail = email_generator.generate_email()
print(email_generator, e_mail, sep="\n")
