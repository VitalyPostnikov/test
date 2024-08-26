class Cat:
    def sleep(self):
        print("Свернулся в клубочек и сладко спит.")
class Horse:
    def sleep(self):
        print("Лошадь ебанутая спит на ногах.")
def homeSleep(animal):
    animal.sleep()
cat = Cat()
horse = Horse()
homeSleep(cat)
homeSleep(horse)