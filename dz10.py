class Basket:
  baskets = {
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
    suma = self.calculation()
    if self.age < 18:
      if (suma * 0.9) <= 9900:return 'Ребенок', suma
      else:return 'Не входит'
    elif 18 <= self.age < 65:
      if (suma * 0.89) <= 10800:return 'Трудоспособный', suma
      else: return 'Не входит'
    else:
      if (suma * 0.85) <= 8200:return 'Пенсионер', suma
      else: return 'Не входит'
      
   
  def calculation(self):
    total = 0
    for name, count in self.basket.items():
      total += self.baskets[name]*count
    return total

human1 = Basket({
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


human2 = Basket({
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


human3 = Basket({
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


human4 = Basket({
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


human5 = Basket({
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
print(human1.calculation_sum(),*human2.calculation_sum(),*human3.calculation_sum(),*human4.calculation_sum(),*human5.calculation_sum())
