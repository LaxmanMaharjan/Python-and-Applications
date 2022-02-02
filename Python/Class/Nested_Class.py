class Human:
    def __init__(self):
        self.name = "Justin"
        self.head = self.Head()

    def display(self):
        self.head.talk()
        self.head.brain.think()

    class Head:
        def __init__(self):
            self.brain = self.Brain()

        def talk(self):
            print("Talking")

        class Brain:
            def think(self):
                print("thinking")

p = Human()
p.display()