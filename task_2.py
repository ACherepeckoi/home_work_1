"""
Задание 2.

Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.

Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
time_inp = float(input('Введите время в секундах: '))
hour = time_inp / 3600
minute = time_inp / 60
seconds = time_inp
print(f"{hour},: {minute}, : {seconds}")

