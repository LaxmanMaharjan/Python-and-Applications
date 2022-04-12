class Animal():
    def speak(self):
        pass

    def prefered_action(self):
        pass

class Tiger(Animal): pass
class Dog(Animal): pass

class PetDog(Dog):
    def speak(self):
        print("Dog says Bow Bow")

    def prefered_action(self):
        print("Dog prefer Barking")


class WildDog(Dog):
    def speak(self):
        print("Dog says Agressive Bow Bow")

    def prefered_action(self):
        print("Dog prefer Biting")

class PetTiger(Tiger):
    def speak(self):
        print("Tiger says Roar")

    def prefered_action(self):
        print("Tiger prefer stay at home")

class WildTiger(Tiger):
    def speak(self):
        print("Tiger says agressive Roar")

    def prefered_action(self):
        print("Tiger prefer Hunting in jungle")
        
class AnimalFactory:
    @classmethod
    def create_Dog(self):
        return Dog()
    @classmethod
    def create_Tiger(self):
        return Tiger()
    
class WildAnimalFactory(AnimalFactory):
    @classmethod
    def create_Dog(self):
        return WildDog()
    @classmethod
    def create_Tiger(self):
        return WildTiger()
    
class PetAnimalFactory(AnimalFactory):
    @classmethod
    def create_Dog(self):
        return PetDog()
    @classmethod
    def create_Tiger(self):
        return PetTiger()

if __name__ == '__main__':
    print("-----"*20)
    print("Creating Wild dog through WildAnimal Factory")
    mydog = WildAnimalFactory.create_Dog()
    mydog.speak()
    mydog.prefered_action()

    print("-----"*20)
    print("Creating Wild Tiger through WildAnimal Factory")    
    mytiger = WildAnimalFactory.create_Tiger()
    mytiger.speak()
    mytiger.prefered_action()
    
    print("-----"*20)
    print("Creating Pet dog through PetAnimal Factory")
    mydog1 = PetAnimalFactory.create_Dog()
    mydog1.speak()
    mydog1.prefered_action()

    print("-----"*20)
    print("Creating Pet Tiger through PetAnimal Factory")
    mytiger1 = PetAnimalFactory.create_Tiger()
    mytiger1.speak()
    mytiger1.prefered_action()    
    
    



















