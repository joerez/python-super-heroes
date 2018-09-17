class Dog:
    greeting = "woof!"

    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.greeting)


my_dog = Dog("Spot")
print(my_dog.name)
my_other_dog = Dog("Annie")
print(my_other_dog.name)

my_dog.bark()
my_other_dog.bark()
