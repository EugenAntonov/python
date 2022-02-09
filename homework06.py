# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 09:49:35 2022

@author: 1
"""

"""
1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, 
второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке 
(красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов. 
При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""

import time

class TrafficLight:
    __color = "red"
    def running(self):
            print("red")
            result = "r"
            time.sleep(7)
            print("yellow")
            result = result + "y"
            time.sleep(2)
            print("green")
            result = result + "g"
            time.sleep(10)
            return result
        
a = TrafficLight()
if a.running() == "ryg":
    a.running()
else:
    print("Wrong color consequence")

"""
2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия 
одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода.
Например: 20 м*5000 м*25 кг*5 см = 12500 т.
"""

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def cover_count(self, thick):
        cover_weight = self._length * self._width * 25 * thick
        return cover_weight


a = Road(800, 12)
print(a.cover_count(7)/1000, "tonn")
        
    
"""
3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, 
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника 
(get_full_name) и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса 
Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.w_dic = {"wage": wage, "bonus": bonus}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.w_dic["wage"]
        
class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname    
    def get_total_income(self):
        return self.w_dic["wage"] + self.w_dic["bonus"]
    
a = Position("Nick", "Smith", "Manager", 5000, 1000)
b = Position("Anna", "Cohan", "Junior Manager", 2000, 500)
print("Name", "\t\t", "Total income")
print(a.get_full_name(), "\t\t", a.get_total_income())
print(b.get_full_name(), "\t\t", b.get_total_income())

        
    

"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, 
что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать 
текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print("Машина поехала")
    def stop(self):
        print("Машина остановилась")
    def turn(self, direction):
        print("Машина повернула ", direction)
    def show_speed(self):
        print("Текущая скорость ", self.speed)

class TownCar(Car):
    def show_speed(self):
        print("Текущая скорость ", self.speed)        
        if self.speed > 60:
            print("Превышение скорости")

class WorkCar(Car):
    def show_speed(self):
        print("Текущая скорость ", self.speed)        
        if self.speed > 40:
            print("Превышение скорости")

class SportCar(Car):
    def set_type(self):
        self.is_police = False

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = True

a = TownCar(50, "blue", "ford", False)
print(f"Model: {a.name}\nColor: {a.color}")
a.show_speed()

b = WorkCar(60, "red", "opel", False)
print(f"Model: {b.name}\nColor: {b.color}")
b.show_speed()

c = PoliceCar(100, "white", "cadillac", False)
c.show_speed()
print(c.is_police)

d = SportCar(120, "purple", "cadillac", True)
# d.is_police = False
print(d.is_police)

e = SportCar(180, "green", "mustang", None)
e.set_type()
print(e.is_police)

"""
5. Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. 
Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Это экземпляр ручки")
    
class Pencil(Stationery):
    def draw(self):
        print("Это экземпляр карандаша")
    
class Handle(Stationery):
    def draw(self):
        print("Это экземпляр маркера")
        
d = Stationery("канцелярия")
a = Pen("ручка")
b = Pencil("карандаш")
c = Handle("маркер")

d.draw()
a.draw()
b.draw()
c.draw()
    





















