#Базовый класс Item:
class Item:
   def __init__(self, name, description):
      self.name = name
      self.description = description
      
   def __str__(self):
      return f"{self.name} - {self.description}"
   
#Класс Weapon(Item)
class Weapon(Item):
   def __init__(self, name, description, damage):
      super().__init__(name, description)
      self.damage = damage

#Класс Armor(Item):
class Armor(Item):
   def __init__(self, name, description, defense):
      super().__init__(name, description)
      self.defense = defense 

#Декоратор @remember:
memory = {}

def remember(cls):
   def inner(*args, **kwargs):
      key = str(args) + str(kwargs)  
      if key in memory:
         raise Exception("Object already exists")
      obj = cls(*args, **kwargs)   
      memory[key] = obj
      return obj
   return inner

#Перегрузка оператора *:
@remember  
class Weapon:
   def __init__(self, damage, count):
      self.damage = damage 
      self.count = count

   def __mul__(self, count):
      return Weapon(self.damage, self.count*count)

weapon = Weapon(10, 2) 
weapon = weapon * 3 

