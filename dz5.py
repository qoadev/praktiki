print("Ввод роста 5 человек:")
arr=[int(input()) for x in range(5)]
print(arr)
p=int(input("Рост Пети:"))
arr.append(p)
arr.sort()
print(arr)
print("Номер в строю:", arr.index(p)+1)
