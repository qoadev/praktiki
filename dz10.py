class Basket:
  abst_basket = {
    'bread': 45,
    'potatoes': 15,
    'cucumbers': 30,
    'orange': 40,
    'meat': 250,
    'fish': 200,
    'milk': 50,
    'eggs': 90,
    'oil': 100,
    'salt': 15  
  }
  def __init__(self,basket, age):
    self.basket = basket
    self.age = age

  def calculation_sum(self):  
    sum = self.calculation()
    if self.age < 18:
      if (sum * 0.9) <= 9900:
        return 'ребенок', sum
      else: 
          return 'не входит'
    elif 18 <= self.age < 65:
      if (sum * 0.89) <= 10800:
        return 'трудоспособный', sum
      else: return 'не входит'
    else:
      if (sum * 0.85) <= 8200:
        return 'пенсионерка', sum
      else: return 'не входит'
      
   
  def calculation(self):
    total = 0
    for name, count in self.basket.items():
      total += self.abst_basket[name]*count
    return total

Lexa = Basket({
    'bread': 4,
    'potatoes': 1,
    'cucumbers': 3,
    'orange': 4,
    'meat': 25,
    'fish': 20,
    'milk': 5,
    'eggs': 9,
    'oil': 1,
    'salt': 1  
  }, 15)
print(Lexa.calculation_sum())

Gela = Basket({
    'bread': 4,
    'potatoes': 1,
    'cucumbers': 3,
    'orange': 4,
    'meat': 25,
    'fish': 2,
    'milk': 5,
    'eggs': 9,
    'oil': 1,
    'salt': 1  
  }, 30)
print(*Gela.calculation_sum())

Karolina = Basket({
    'bread': 4,
    'potatoes': 1,
    'cucumbers': 3,
    'orange': 4,
    'meat': 25,
    'fish': 20,
    'milk': 5,
    'eggs': 9,
    'oil': 1,
    'salt': 1  
  }, 40)
print(*Karolina.calculation_sum())

ivan = Basket({
    'bread': 4,
    'potatoes': 1,
    'cucumbers': 3,
    'orange': 4,
    'meat': 25,
    'fish': 20,
    'milk': 5,
    'eggs': 9,
    'oil': 1,
    'salt': 1  
}, 24)
print(*ivan.calculation_sum())

petr = Basket({
    'bread': 4,
    'potatoes': 1,
    'cucumbers': 3,
    'orange': 4,
    'meat': 25,
    'fish': 20,
    'milk': 5,
    'eggs': 9,
    'oil': 1,
    'salt': 1  
}, 22)
print(*petr.calculation_sum())
