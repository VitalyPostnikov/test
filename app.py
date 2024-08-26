class Cat():
 def __init__ (self, breed, color, age):
    self.breed = breed
    self.color = color
    self.age = age
 def meow(self):
  print("Мяу!")
 def purr(self):
  print("Мррр!")

cat1 = Cat("Абиссинская", "Рыжая", 4)
cat2 = Cat("Британская", "Серая", 2)
class Cat():
 def __init__(self, breed, color, age):
            self._breed = breed
            self._color = color
            self._age = age
 @property
 def breed(self):
    return self._breed

 @property
 def color(self):
    return self._color

 @property
 def age(self):
    return self._age

 @age.setter
 def age(self, new_age):
        if new_age > self._age:
            self._age = new_age
        return self._age

cat = Cat("Абиссинская", "Рыжая", 4)
cat.age = 5
print(cat.age)
class HomeCat(Cat):
 def __init__(self, breed, color, age, owner, name):
    super().__init__(breed, color, age)
    self._owner = owner
    self._name = name
@property
def owner(self):
  return self._owner
@property
def name(self):
  return self._name
def getTreat(self):
    print('Мяу-Мяу')
MyCat = HomeCat("Сиамская", "Серый", 5, "Виталий", "Чика")

print(MyCat.breed)
print(MyCat.owner)
MyCat.getTreat()
MyCat.meow()