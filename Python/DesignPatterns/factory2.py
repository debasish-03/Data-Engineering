
from abc import ABC, abstractmethod

'''
Example Scenario
Imagine you have a pet store that sells different types of pets, like Dog and Cat. You want to create these pets using a factory.

Step-by-Step Implementation
1. Define the Pet Interface: Create an interface or a base class for the pet objects.
2. Implement Concrete Pet Classes: Create specific classes for each type of pet that implements the Pet interface.
3. Create the Factory Class: This class will have a method that returns a new instance of the pet based on some input.
'''

class Pet(ABC):
    '''Define the Pet Interface'''
    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


# Implement Concrete Pet Classes
class Dog(Pet):
    def speak(self):
        return "Woof!"
    
    def __str__(self):
        return "Dog"
    
class Cat(Pet):
    def speak(self):
        return "Meow!"
    
    def __str__(self):
        return "Cat"


class PetFactory:
    '''Factory Class'''
    @staticmethod
    def get_pet(pet_type):
        if pet_type == "dog":
            return Dog()
        elif pet_type == "cat":
            return Cat()
        else:
            raise ValueError("Unknown pet type")
        

if __name__ == '__main__':
    pet_type = input("Enter the type of pet (dog/cat): ").strip().lower()
    try:
        pet = PetFactory.get_pet(pet_type=pet_type)
        print(f"A {pet} says '{pet.speak()}'")
    except ValueError as e:
        print(e)
