# -*- coding: utf-8 -*-
"""
1. Создать программный файл в текстовом формате, записать в него построчно 
данные, вводимые пользователем. Об окончании ввода данных 
будет свидетельствовать пустая строка.
"""
import os

with open(os.path.join(os.getcwd(),"my_text_file.txt"), "w") as f_obj:
    a = "text"
    while a != "":
        a = input("Print any text: ")
        print(a, file=f_obj)


"""
2. Создать текстовый файл (не программно), сохранить в нём несколько строк, 
выполнить подсчёт строк и слов в каждой строке.
"""
os.getcwd()

with open("test2.txt", "w", encoding="utf-8") as my_file:
    my_file.write("""Робин-Бобин
Кое-как
Подкрепился
Натощак:
Съел теленка
Утром рано,
Двух овечек
И барана""")

with open("test2.txt", "r", encoding="utf-8") as my_file:
    content=my_file.read();
    print(content)

my_f = open("test2.txt", "r", encoding="utf-8")
content = my_f.readlines()
print("Число строк: ", len(content))
for x in range(len(content)):
    y = content[x].split()
    print("Число слов в строке " + str(x+1) + ": " + str(len(y)))
my_f.close()

os.remove("test2.txt")
os.listdir()

"""
3. Создать текстовый файл (не программно). Построчно записать фамилии 
сотрудников и величину их окладов (не менее 10 строк). Определить, кто из 
сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников.
"""
my_str = """Иванов 20000
Петров 35000
Сидоров 15000
Семенов 7000
Зайцев 120000
Смирнов 19500
Козлов 18000
Сергеев 21000
Александров 11000
Карасев 49000
Волков 33000
Щукин 14000
Дятлов 100000"""

with open("test3.txt", "w", encoding="utf-8") as my_file:
    my_file.write(my_str)

limit = 20000
sum_1 = 0
my_f = open("test3.txt", "r", encoding="utf-8")
content = my_f.readlines()
i = 1
print(f"Список сотрудников с окладом менее {limit}:")
for x in content:
    y = x.split()
    sum_1 = sum_1 + int(y[1])
    if int(y[1]) < limit:
        print("  " + str(i) + ". " + y[0])
        i += 1
aver_salary = round(sum_1/len(content),0)
print(f"Средняя зарплата сотрудников составляет {aver_salary}")
my_f.close()

os.remove("test3.txt")

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

russian_numbers=["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
my_str = """One — 1
Two — 2
Three — 3
Four — 4
"""

with open("test4.txt", "w", encoding="utf-8") as my_file:
    my_file.write(my_str)

my_f = open("test4.txt", "r", encoding="utf-8")
content = my_f.readlines()
print(content)
new_content = ""
for x in range(len(content)):
    y = int(content[x].split()[2])
    z = russian_numbers[y] + " - " + str(y)
    new_content = new_content + "\n" + z
my_f.close()

my_f = open("test4_1.txt", "w", encoding="utf-8")
a = my_f.write(new_content)
my_f.close()

my_f = open("test4_1.txt", "r", encoding="utf-8")
content=my_f.read()
print(content)
my_f.close()

os.remove("test4.txt")
os.remove("test4_1.txt")


"""
5. Создать (программно) текстовый файл, записать в него программно 
набор чисел, разделённых пробелами. Программа должна подсчитывать сумму 
чисел в файле и выводить её на экран.
"""
import random

new_content = [random.randint(1, 100) for x in range(100)]
new_str = str()
for x in new_content:
    new_str = new_str + " " + str(x)
    
my_f = open("test5.txt", "w", encoding="utf-8")
my_f.write(new_str)
my_f.close()

my_f = open("test5.txt", "r", encoding="utf-8")
content = my_f.read()
a = content.split()
test_sum = 0
for x in a:
    test_sum += int(x)
print(test_sum)
my_f.close()

os.remove("test5.txt")



"""
6. Сформировать (не программно) текстовый файл. В нём каждая строка должна 
описывать учебный предмет и наличие лекционных, практических и лабораторных 
занятий по предмету. Сюда должно входить и количество занятий. Необязательно, 
чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий 
по нему. Вывести его на экран.

Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

my_str="""Физика: 30(л) - 10(лаб)
Физкультура: - 30(пр) -
Алгебра: 10(л) 10(пр) 15(лаб)
Геометрия: 12(л) 8(пр) 11(лаб)
Химия: 5(л) 15(пр) 20(лаб)
История: 20(л) 20(пр) -
Английский язык: 10(л) 20(пр) -
Биология: 10(л) 12(пр) 18(лаб)
Трудовое воспитание: - - 25(лаб)"""

with open("test6.txt", "w", encoding="utf-8") as my_file:
    my_file.write(my_str)


my_f = open("test6.txt", "r", encoding="utf-8")
content = my_f.readlines() # читаем содержимое файла в список
my_dict = dict() # объявляем пустой словарь
for x in content: # цикл по элементам списка содержимого файла
    sum_hours = int() # объявляем переменную для суммы часов
    a = x.split() # разбиваем строку на список
    if a[1][-1:] == ":": # проверяем, не состоит ли предмет из нескольких слов
        a[0] = a[0] + " " + a[1] # если состоит, объединяем первые два слова
        a.pop(1) # лишний элемент вырезаем из списка
    for i in range(1,4): # запускаем цикл по значениям часов занятий
        b = a[i].split("(")[0] # отрезаем скобку от часов
        if b.isnumeric(): # проверяем, является ли количество часов числом
            sum_hours += int(b) # если является, суммируем с общим количеством часов
    a_1 = a[0][:len(a[0])-1] # отрезаем от названия предмета двоеточие
    dict2 = {a_1:sum_hours}  # формируем элемент словаря 
    my_dict.update(dict2)    # добавляем в финальный словарь новый элемент
my_f.close() # закрываем файл
print(my_dict) 

os.remove("test6.txt")


"""
7. Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка будет содержать данные о фирме: название, форма 
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, 
а также среднюю прибыль. Если фирма получила убытки, в расчёт средней 
прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, также 
добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""

my_str = """firm_x ООО 10000 5000
firm_2 ОО1 100000 15000
firm_a ОО1 105500 55000
firm_s ООО 10008 25000
firm_ww ОО1 5000 53000
firm_ee1 ОО2 44000 55000
firm_deko ООО 111000 65000
firm_101 ОО2 10330 25000
firm_7 ОО1 40040 8000
firm_50 ОО3 70000 65000
firm_axof ОО3 590000 1000"""

with open("test7.txt", "w", encoding="utf-8") as my_file:
    my_file.write(my_str)

my_dict = dict()
average_profit = int()
sum_profit = int()

my_f = open("test7.txt", "r", encoding="utf-8")
content=my_f.readlines()
for x in content:
    y = x.split()
    z = int(y[2]) - int(y[3])
    sum_profit += z
    my_dict1 = {y[0]:z}
    my_dict.update(my_dict1)
average_profit = round(sum_profit/len(content),0)
my_f.close()
my_list = [my_dict,{"average_profit":average_profit}]
print(my_list)

import json

with open("test7_j.json", "w") as write_f:
    json.dump(my_list, write_f)
    
os.remove("test7.txt")
os.remove("test7_j.json")
