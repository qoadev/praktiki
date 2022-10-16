from collections import namedtuple
Employe = namedtuple('Employe', 'name stazh city days')

employees=(Employe("Александр Карюк Евгеньевич", 2, "Москва", 3),
           Employe("Салихов Руслан Ринтович", 23, "Краснодар", 3),
           Employe("Утегенов Султан Иванович", 4, "Москва", 4),
           Employe("Дригин Иван Иванович",7,"Москва",5),
            Employe("Петров Иван Иванович",3,"Краснодар",5))
counter=0
arr=[]
for i in range(len(employees)):
    if employees[i][3] >=3:
        arr.append(employees[i][2])
s = set(arr)
for i in s:
    if arr.count(i)>1:
        counter+= arr.count(i)
#Задача 1
print("Кол-во сотрдуников командированные в одинаковые города:", counter)

#Задача 2
for i in range(len(employees)):
    if employees[i][1] >=1 and employees[i][1]<= 5:
        print("Стаж работы от 1 до 5 лет", employees[i][0])
    if employees[i][1] >5:
        print("Стаж работы более 5 лет", employees[i][0])
