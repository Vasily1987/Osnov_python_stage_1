#Модуль № 6 ДЗ

start = input("Добро пожаловать в игру! Вам нужно верно назвать год рождения известных людей. Вас ждут 5 вопросов. Хотите поучавствовать в викторине?  ")
while start.lower() == "да":
    kol_True = 0
    kol_false = 0
    vsego = 5
    print("Вопрос № 1")
    otv = input("Год рождения Альфреда Нобеля? ")
    if otv == "1833":
        kol_True = kol_True + 1
    else:
        kol_false = kol_false + 1
    print("Вопрос № 2")
    otv = input("Год рождения Иосифа Сталина? ")
    if otv == "1878":
        kol_True = kol_True + 1
    else:
         kol_false = kol_false + 1
    print("Вопрос № 3")
    otv = input("Год рождения Николо Тесла? ")
    if otv == "1891":
        kol_True = kol_True + 1
    else:
        kol_false = kol_false + 1
    print("Вопрос № 4")
    otv = input("Год рождения Пушкина? ")
    if otv == "1799":
        kol_True = kol_True + 1
    else:
        kol_false = kol_false + 1
    print("Вопрос № 5да")
    otv = input("Год рождения Лермантова? ")
    if otv == "1814":
        kol_True = kol_True + 1
    else:
        kol_false = kol_false + 1
    cent_true = (kol_True*100)/vsego
    cent_false = (kol_false*100)/vsego
    print("правельных ответов ", kol_True)
    print("не правильных ", kol_false)
    print(cent_true, " % верных ответов ")
    print(cent_false, " % неверных ответов ")
    start= input("Хотите попробовать свои силы еще раз ")
print("Ну тогда в следущий раз!")