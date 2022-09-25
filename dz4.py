friends=["Роман Петреченков", "Андрей Хапка","Даниил Гарилов","Вадим Куертов"]
print(*friends, sep=',')
friends.remove("Роман Петреченков")
print("Роман Петреченков не сможет прийти.")
#В начало списка
friends.insert(0,"Иван Володин")
print(*friends, sep=',')
del friends[0]
#В середину списка
friends.insert(1,"Иван Володин")
print(*friends, sep=',')
del friends[1]
#В конец списка
friends.append("Иван Володин")
print(*friends, sep=',')
