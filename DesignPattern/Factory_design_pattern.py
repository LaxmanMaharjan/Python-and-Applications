
class Animal():
    def speak(self):
        pass

    def prefered_action(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Dog says Bow Bow")

    def prefered_action(self):
        print("Dog prefer Barking")

class Tiger(Animal):
    def speak(self):
        print("Tiger says Roar")

    def prefered_action(self):
        print("Tiger prefer Hunting")

class AnimalFactory:
    @classmethod
    def create(self):
        return Animal()

class DogFactory(AnimalFactory):
    @classmethod
    def create(self):
        return Dog()

class TigerFactory(AnimalFactory):
    @classmethod
    def create(self):
        return Tiger()

print("----"*20)
print("Creating a Dog using Dog Factory")
d = DogFactory.create()
d.speak()
d.prefered_action()
print("----"*20)
print("Creating a Tiger using Tiger Factory")
t = TigerFactory.create()
t.speak()
t.prefered_action()