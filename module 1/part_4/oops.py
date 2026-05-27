class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


cat = Cat("Jerry", "brown")
print(cat.name)


class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof")

dog = Dog("TOM", "German")
print(dog.bark)

class AIChatbot:
    def __init__(self, model):
        self.model = model

    def chat(self, message):
        return f"{self.model} says: {message}"


openAi_bot = AIChatbot("gpt-4.o")
print(openAi_bot.chat(f"Hello this is {openAi_bot.model}"))
