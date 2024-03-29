"""
1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
list1 = [1,"2",3.0,4,5]

for a in list1:
    print(type(a))






"""
2. Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().
"""
list2 = [1, "2", 3.0, 4, 5, "aaa", 687, 5.5]
list2.append(input("Enter new element: "))
i=0
while i < len(list2):
    if i+1>len(list2)-1:
        break
    list2[i],list2[i+1]=list2[i+1],list2[i]    
    print("after ", list2)
    i+=2







"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict.
"""
# вариант 1
list3=["зима","весна","лето","осень"]
month=int(input("Введите номер месяца: "))
if month<3 or month==12:
    print(list3[0])
elif month<6:
    print(list3[1])
elif month<9:
    print(list3[2])
else:
    print(list3[3])
    
# вариант 2
list3=["зима","зима","весна","весна","весна","лето","лето","лето","осень","осень","осень","зима",]
month=int(input("Введите номер месяца: "))
print(list3[month-1])

# вариант 3
dict1 = {(1,2,12):"зима", (3,4,5):"весна", (6,7,8):"лето", (9,10,11):"осень"}
month = int(input("Введите номер месяца: "))
output = next(v for k, v in dict1.items() if month in k)
print("Время года - ",output)




"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. Строки нужно пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове.
"""

str1 = input("Введите текст, используя пробелы: ")
str2 = str1.split(" ")
i = 1
for x in str2:
    print(str(i),x[:10])
    i+=1





"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. 
У пользователя нужно запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
print(my_list)
new_element = 0
# new_element = input("Введите целое натуральное число: ")
i = 0
while i < len(my_list):
    if new_element > my_list[i]:
        my_list.insert(i, new_element)
        break
    else:
        if i == len(my_list)-1:
            my_list.append(new_element)
            break
        else:
            i +=1        
print(my_list)




"""
6. * Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами, 
то есть характеристиками товара: название, цена, количество, единица измерения. 
Структуру нужно сформировать программно, запросив все данные у пользователя.
Пример готовой структуры:

[
(1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]

Нужно собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. 
Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:

{
"название": ["компьютер", "принтер", "сканер"],
"цена": [20000, 6000, 2000],
"количество": [5, 2, 7],
"ед": ["шт."]
}
"""
new_list=[]
new_tuple=()
user_prop = input("Введите параметры товара через запятую (без пробелов): ")
list_prop = user_prop.split(",")
new_dict = {}
for a in range(10):
    i = int(input("Введите номер товара: "))
    for s in list_prop: # цикл по параметрам товара
        str1 = "Введите " + s + ": "
        a = input(str1)
        new_dict[s]=a #
        new_tuple = i, new_dict
    new_list.append(new_tuple)    
    ask_for_new = input("Ввести еще один товар? (да/нет)  ")
    if ask_for_new == "да":
        continue
    else:
        break
print("New list: ",new_list)


new_list = [(1, {"название": "ноутбук", "цена": 20000, "количество": 5, "eд": "шт."}),(2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),(3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})]
list_keys = new_list[0][1].keys() #формируем список ключей из первого элемента
dict_final = {} #задаем пустой словарь, который будет в конце заполнен
for x in list_keys:    # итерация по списку ключей
    i = 0    # начинаем счетчик
    b = []    # задаем пустой список значений для каждого ключа
    while i < len(new_list):        # запускаем цикл по элементам исходного списка
        b.append(new_list[i][1][x])        # записываем в список значения одного ключа
        i +=1           # увеличиваем счетчик на 1
    b = list(set(b))    # оставляем только уникальные значения списка
    dict2 = {x:b}       # формируем элемент словаря ключ-список
    dict_final.update(dict2)    # добавляем в финальный словарь новый элемент
print(dict_final)
    
    
