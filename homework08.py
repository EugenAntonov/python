"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать 
дату в виде строки формата «день-месяц-год». В рамках класса реализовать два 
метода. Первый, с декоратором @classmethod. 
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, 
месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.
"""

class Date:
    def __init__(self, date_input):
        self.date_input = date_input
        
    @classmethod
    def date_tranform(cls, date_input):
        date_day = int(date_input.split("-")[0])
        date_month = int(date_input.split("-")[1])
        date_year = int(date_input.split("-")[2])
        if cls.day_validation(date_day, date_month, date_year):
            return True
        else:
            return False
    
    @staticmethod
    def day_validation(date_day, date_month, date_year):
        day_dict = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        if date_month > 0  and date_month <= 12:            
            if date_day > 0 and date_day <= day_dict[date_month]:
                return True
            else:
                print("Incorrect day")
                return False
        else:
            print("Incorrect month")
            return False
    
my_obj = Date("6-02-2022")
my_obj.date_tranform("6-10-2021")
my_obj.date_tranform("46-10-2021")
my_obj.date_tranform("16-13-2021")

Date.date_tranform("01-07-2004")
Date.date_tranform("11-17-2004")



"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать 
эту ситуацию и не завершиться с ошибкой.
"""

class My_exception:
    def __init__(self, a, b):
        self.a = float(a)
        self.b = float(b)
        try:
            a/b
        except ZeroDivisionError:
            print("You CAN NOT divede by zero")
        else:
            print("Everything is ok")
        finally:
            print("Finished")
            
            
my_obj = My_exception(22, 0)
my_obj = My_exception(22, 44)



"""
3. Создайте собственный класс-исключение, который должен проверять содержимое 
списка на наличие только чисел. Проверить работу исключения на реальном примере. 
Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать 
проверку типа элемента. Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и 
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""

class My_exception:
    def __init__(self):
        self.my_list=[]
        self.fill_list()

    def fill_list(self):
        while True:
            self.a = input("Input number (or 'stop' if you want to finish): ")
            if self.a == "stop":
                break
            else:
                if self.check(self.a):
                    self.my_list.append(self.a)
                else:
                    print("It is not a number, try again.")
            
    def check(self, a):
        if a.isdigit():
            return True
        else:
            return False
        
    
my_obj = My_exception()
print(my_obj.my_list)




"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, 
описывающий склад. А также класс «Оргтехника», который будет базовым 
для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для 
каждого типа оргтехники.
"""

class Warehouse:
    pass

class Office_tech:
    def __init__(self, name, count, price):
        self.name = name
        self.count = int(count)
        self.price = float(price)

class Printer(Office_tech):
    def __init__(self, name, count, price, pr_type):
        super().__init__(name, count, price)
        self.pr_type = pr_type
        
class Scanner(Office_tech):
    def __init__(self, name, count, price, scan_type):
        super().__init__(name, count)
        self.scan_type = scan_type
        
class Xerox(Office_tech):
    def __init__(self, name, count, price, xer_type):
        super().__init__(name, count)
        self.xer_type = xer_type
        
a = Printer("Brother 1500", 15, 45000, "Laser")
a.price

"""
5. Продолжить работу над первым заданием. Разработайте методы, 
которые отвечают за приём оргтехники на склад и передачу в определённое 
подразделение компании. Для хранения данных о наименовании и количестве 
единиц оргтехники, а также других данных, можно использовать любую 
подходящую структуру (например, словарь).
"""

class Warehouse:
    def __init__(self):
        self.target_set = {"London", "Paris", "Berlin"}
        self.item_dict = {}

    def get_item(self, name, count):
        try: 
            self.item_dict[name] = self.item_dict[name] + int(count)
            print("Success. Position is added")
        except KeyError:
            self.item_dict[name] = int(count)

    def send_item(self, name, count, target):
        try: 
            self.item_dict[name]
            if target in self.target_set:                
                if self.item_dict[name] < count:
                    print(f"Not enough amount of {name}")
                else:
                    self.item_dict[name] = self.item_dict[name] - int(count)
                    print("Success. Position is sent")
            else:
                print(f"Such direction ({target}) does not exist")
        except KeyError:
            print(f"Such position ({name}) is absent")

class Office_tech:
    def __init__(self, name, count, price):
        self.name = name
        self.count = int(count)
        self.price = float(price)

    def add_item(self, target):
        target.get_item(self.name, self.count)

class Printer(Office_tech):
    def __init__(self, name, count, price, pr_type):
        super().__init__(name, count, price)
        self.pr_type = pr_type
        
class Scanner(Office_tech):
    def __init__(self, name, count, price, scan_type):
        super().__init__(name, count, price)
        self.scan_type = scan_type
        
class Xerox(Office_tech):
    def __init__(self, name, count, price, xer_type):
        super().__init__(name, count, price)
        self.xer_type = xer_type

my_wareh = Warehouse()

a = Printer("Brother 1500", 15, 45000, "Laser")
b = Printer("Brother 1500", 155, 15000, "Laser")
c = Printer("Hp X", 15, 18000, "Laser")
d = Scanner("Epson", 125, 8000, "hor")

a.add_item(my_wareh)
b.add_item(my_wareh)
c.add_item(my_wareh)
d.add_item(my_wareh)
print(my_wareh.item_dict)

my_wareh.send_item("Brother 1500", 4, "Smolensk")
my_wareh.send_item("Brother 500", 4, "London")
my_wareh.send_item("Brother 1500", 400, "London")
my_wareh.send_item("Brother 1500", 10, "London")
print(my_wareh.item_dict)

"""
6. Продолжить работу над вторым заданием. 
Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, 
нельзя использовать строковый тип данных.
"""

class Printer(Office_tech):
    def __init__(self, name, count, price, pr_type):
        super().__init__(name, count, price)
        self.pr_type = pr_type
        self.count = self.check_count(count)        

    def check_count(self, count):
        if type(count) == str:
            print("Count is NOT a number")
        elif type(count) != int:
            print("Count shoud be integer")
        else:
            return count
       
a = Printer("Brother 1500", 100, 45000, "Laser")
print(a.count)

b = Printer("Brother 1500", '100', 45000, "Laser")
print(b.count)

c = Printer("Brother 1500", 100.78, 45000, "Laser")
print(c.count)
