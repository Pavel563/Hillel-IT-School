import random
import json
import csv


# Цель задания - создать функции, которые будут генерировать случайные данные нужного формата
# для записи в файлы разных типов.
########################################################################################################################
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.


def create_text_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('a'), ord('z'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def create_number_line(min_len, max_len):
    txt_list = [chr(random.randint(ord('0'), ord('9'))) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def split_txt_line(txt_line):
    space_count = len(txt_line) // 5
    space_index_list = []
    while len(space_index_list) < space_count:
        index = random.randint(1, len(txt_line) - 2)
        if (index not in space_index_list
                and index - 1 not in space_index_list
                and index + 1 not in space_index_list):
            space_index_list.append(index)
    for index in space_index_list:
        txt_line = txt_line[:index] + " " + txt_line[index + 1:]
    return txt_line


def replace_text_to_number(word):
    if len(word) > 5:
        return word
    else:
        create_number_line(len(word), len(word))
    return create_number_line(len(word), len(word))


def replace_first_letter(word):
    return word.replace(word[0], word[0].upper(), 1)


def replace_last_letter(word):
    sings = ',.;:!?'
    if len(word) < 4:
        return word
    return word[:-1] + random.choice(sings)


def create_random_txt_data(min_len=100, max_len=1000):
    txt_line = create_text_line(min_len, max_len)
    txt_line = split_txt_line(txt_line)
    new_words = []
    for word in txt_line.split():
        case = random.randint(1, 100)
        if not case % 10:
            new_word = replace_text_to_number(word)
        elif not case % 5:
            new_word = replace_first_letter(word)
        elif not (case + 1) % 5:
            new_word = replace_last_letter(word)
        else:
            new_word = word
        new_words.append(new_word)
    return " ".join(new_words)


########################################################################################################################
# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.

def create_random_key():
    key = "".join(chr(random.randint(ord("a"), ord("z"))) for _ in range(5))
    return key


def create_value():
    n = random.randrange(3)
    if n == 0:
        value = random.randint(-100, 100)
    elif n == 1:
        value = random.uniform(0, 1)
    else:
        value = bool(random.randint(0, 1))
    return value


def create_dict():
    my_dict = {}
    n = random.randint(5, 20)

    for item in range(n):
        key = create_random_key()
        value = create_value()
        my_dict[key] = value
    return my_dict


########################################################################################################################
# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.

def create_list():
    m = random.randint(3, 10)
    n = random.randint(3, 10)
    my_list = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]
    return my_list


########################################################################################################################
# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"

def write_txt(filename):
    with open(filename, "w") as txt_file:
        txt_data = create_random_txt_data()
        txt_file.write(txt_data)


def write_json(filename):
    with open(filename, "w") as json_file:
        json.dump(create_dict(), json_file, indent=2)


def write_csv(filename):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(create_list())


def generate_and_write_file(filename):
    my_format = filename.split('.')[-1]
    if my_format == "txt":
        result = write_txt(filename)
    elif my_format == "json":
        result = write_json(filename)
    elif my_format == "csv":
        result = write_csv(filename)
    else:
        print("Unsupported file format")
    return result


generate_and_write_file('test.json')
