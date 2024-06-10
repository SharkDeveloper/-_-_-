import pickle
import pytest

#Lab4
# Базовый класс Item
class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def __str__(self):
     return f"{self.name} - {self.description}"

# Класс оружия
class Weapon(Item):  
  def __init__(self, name, description, damage):
     super().__init__(name, description)
     self.damage = damage

# Класс брони     
class Armor(Item):
  def __init__(self, name, description, defense):
     super().__init__(name, description)      
     self.defense = defense

# Декоратор запоминания объектов       
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

#end Lab4

# Ввод и проверка данных
def input_item():
  while True:
    try:
        name = input("Введите имя: ")
        if not name:
            raise ValueError("Имя не может быть пустым")
        break
    except ValueError as e:
        print(e)

  type = input("Введите тип (1 - оружие, 2 - броня): ")
  if type not in ["1", "2"]:
     raise ValueError("Некорректный тип")

  if type == "1":
     damage = float(input("Укажите урон: "))
     item = Weapon(name, "Оружие", damage)
  else:     
     defense = int(input("Укажите защиту: "))
     item = Armor(name, "Броня", defense)

  return item

# Сохранение/загрузка объектов
def save_objects(objects):
  try:
     with open('data.bin', 'wb') as f:
        pickle.dump(objects, f)
  except IOError as e:
     print("Ошибка записи файла:", e)

def load_objects():
  try:     
     with open('data.bin', 'rb') as f:    
        return pickle.load(f)
  except IOError:
     print("Ошибка чтения файла")
     return []
  except pickle.PickleError as e:
     print("Некорректные данные в файле:", e)
     return []

# Пользовательское исключение     
class MyError(Exception):
  pass

# Тесты
@pytest.fixture
def weapon():
  return Weapon(10, 2)

def test_mul(weapon):
  res = weapon * 3
  assert res.damage == 10
  assert res.count == 6

def test_input():
  item = input_item()
  assert isinstance(item, (Weapon, Armor))

def test_save_load(weapon):
  objects = [weapon]
  save_objects(objects)
  loaded = load_objects()
  assert loaded[0] == weapon

if __name__ == "__main__":
  item = input_item()
  print(item)