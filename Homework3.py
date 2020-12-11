########################################################################################################################
# 1) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value
# по такому правилу: если value меньше 100, то new_value равно половине значения value,
# в противном случае - противоположне value число


value = 100
new_value = value / 2 if value < 100 else ~value + 1
print(new_value)


########################################################################################################################


# 2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value
# по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0


value = 10
new_value = 1 if value < 100 else 0
print(new_value)


########################################################################################################################


# 3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value
# по такому правилу: если value меньше 100, то new_value равно True, в противном случае - False


value = 10
new_value = True if value < 100 else False
print(new_value)


########################################################################################################################


# 4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.


my_str = "String for homework"
print(my_str.upper())


########################################################################################################################


# 5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.


my_str = "String For HomeWork"
print(my_str.lower())


########################################################################################################################


# 6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же.
# Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.


my_str = "asdf"
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)


########################################################################################################################


# 7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же.
# Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.


my_str = "asdf"
new_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(new_str)


########################################################################################################################


# 8) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые являются буквой или цифрой.


my_str = "hjjh51616nj^%$#56"
for symbol in my_str:
    if symbol.isalnum():
        print("symbol", symbol)


########################################################################################################################


# 9) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.

my_str = "hjjh51616nj^%$#56"
for symbol in my_str:
    if not symbol.isalnum():
        print("symbol", symbol)

########################################################################################################################


# 10) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.


my_str = "hjjh 51616 nj ^%$# 56"
for symbol in my_str:
    if not symbol.isalnum() and not symbol.isspace():
        print("symbol", symbol)