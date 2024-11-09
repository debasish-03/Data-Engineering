

class Burger:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)


class BurgerFactory:

    def createCheeseBurger(self):
        ingredients = ["bun", "cheese", "chicken"]
        return Burger(ingredients)
    
    def createDeluxCheeseBurger(self):
        ingredients = ["bun", "tomatos", "lettuce", "cheese", "chicken"]
        return Burger(ingredients)
    
    def createVeganBurger(self):
        ingredients = ["bun", "tomatos", "veggie-patty"]
        return Burger(ingredients)


if __name__ == '__main__':
    burgerFactory = BurgerFactory()
    burgerFactory.createCheeseBurger().print()
    burgerFactory.createDeluxCheeseBurger().print()
    burgerFactory.createVeganBurger().print()