class Person:
    def __init__(self,name,height):
        self.name=name
        self.height=height

    def health(self):
        print(f"my name is {self.name} and my height is {self.height}")

person = Person("Priya", 160)
person.health()
