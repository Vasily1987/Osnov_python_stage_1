#Модуль № 5 ДЗ

ayrsu = int(input("Введите год рождения А.С.Пушкина "))

while ayrsu != 1799:
   ayrsu = int(input("Неверно! Введите верный год рождения А.С.Пушкина "))
if ayrsu == 1799:
    hppy_dau = int(input("Верно,теперь введите день рождения "))
    while hppy_dau != 6:
        hppy_dau = int(input("Неверно! Введите верный день рождения А.С.Пушкина "))
#if hppy_dau == 6:
print("Верно!")
