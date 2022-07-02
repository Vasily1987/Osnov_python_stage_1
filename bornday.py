#Модуль № 3 ДЗ

ayrsu = int(input("Введите год рождения А.С. Пушкина "))

if ayrsu == 1799:
    hppy_dau = int(input("Верно,теперь введите день рождения "))
    if hppy_dau == 6:
        print("Верно")
    elif hppy_dau != 6:
        print("Не верный день рождения")
else: print("Неверный год рождения")