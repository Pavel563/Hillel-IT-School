########################################################################################################################
# 1) Написать программу, которая считывает введенное число и выводит умноженное на 2 значение, если это число
# делится на 5 и выводит 0 в других случаях. Т.е. если ввести 15, то выведет 30, а если 13, то 0.

value = input("Введите число: ")
value = float(value)

if (value * 2) % 5 == 0:
    print(value * 2)
else:
    print(0)


########################################################################################################################


# 2) Написать программу, которая считывает введенный месяц года (в виде числа, например 04) и выводит
# количество дней в этом месяце. Считаем, что год не высокосный, т.е. в феврале 28 дней.

mounth = input("Введите номер месяца: ")
mounth = int(mounth)

if mounth == 1 or mounth == 3 or  mounth == 5 or mounth == 7 or mounth == 8 or mounth == 10 or mounth == 12:
    print(f"В месяце: {mounth} Количество дней: {31}")
elif mounth == 4 or mounth == 6 or mounth == 9 or mounth == 11:
    print(f"В месяце: {mounth} Количество дней: {30}")
elif mounth == 2:
    print(f"В месяце: {mounth} Количество дней: {28}")
else:
    print("Нет такого месяца!")


########################################################################################################################


# 3) Написать программу, которая считывает введенный месяц года (в виде строки, например Апрель) и выводит количество
#    дней в этом месяце. Считаем, что год не высокосный, т.е. в феврале 28 дней.

mounth = input("Введите месяц: ")

if mounth == "Январь" or mounth == "Март" or  mounth == "Май" or mounth == "Июль" or mounth == "Август" or mounth == "Октябрь" or mounth == "Декабрь":
    print(f"В месяце: {mounth.capitalize()} Количество дней: {31}")
elif mounth  == "Апрель" or mounth == "Июнь" or mounth == "Сентябрь" or mounth == "Ноябрь":
    print(f"В месяце: {mounth.capitalize()} Количество дней: {30}")
elif mounth == "Февраль":
    print(f"В месяце: {mounth.capitalize()} Количество дней: {28}")
elif mounth == "январь" or mounth == "март" or  mounth == "май" or mounth == "июль" or mounth == "август" or mounth == "октябрь" or mounth == "декабрь":
    print(f"В месяце: {mounth.capitalize()} Количество дней: {31}")
elif mounth  == "апрель" or mounth == "июнь" or mounth == "сентябрь" or mounth == "ноябрь":
    print(f"В месяце: {mounth.capitalize()} Количество дней: {30}")
elif mounth == "февраль":
    print(f"В месяце: {mounth.capitalize()} Количество дней: {28}")
else:
    print("Нет такого месяца!")