"""
2. Пользователь вводит время в секундах. 
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

inputTime = int(input("Введите любое количество секунд: "))

hours = inputTime//3600
minutes = inputTime//60
if minutes>=60:
    minutes=minutes%60
if minutes<10:
    minutes="0"+str(minutes)
seconds = inputTime%60
if seconds<10:
    seconds="0"+str(seconds)
print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
