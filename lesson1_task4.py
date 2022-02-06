# -*- coding: utf-8 -*-
"""
4. Пользователь вводит целое положительное число. 
Найдите самую большую цифру в числе. 
Для решения используйте цикл while и арифметические операции.
"""

number=int(input("Введите любое число: "))

max_digit = 0
while number>0:
    digit = number%10
    if max_digit<digit:
        max_digit = digit
    number = number//10
print("Самая большая цифра: ",max_digit)    

