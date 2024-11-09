from typing import List

class Pizza:
    def __init__(self, crust: str, sauce: str, cheese: str, toppings: List[str]) -> None:
        self._crust = crust
        self._sauce = sauce
        self._cheese = cheese
        self._toppings = toppings

    @property
    def crust(self) -> str:
        return self._crust

    @property
    def sauce(self) -> str:
        return self._sauce

    @property
    def cheese(self) -> str:
        return self._cheese

    @property
    def toppings(self) -> List[str]:
        return self._toppings

    def __str__(self) -> str:
        return (f"Pizza with {self.crust} crust, {self.sauce} sauce, "
                f"{self.cheese} cheese, and toppings: {', '.join(self.toppings)}")


class PizzaBuilder:
    def __init__(self) -> None:
        self._crust: str = "regular"
        self._sauce: str = "tomato"
        self._cheese: str = "mozzarella"
        self._toppings: List[str] = []

    def set_crust(self, crust: str) -> 'PizzaBuilder':
        self._crust = crust
        return self

    def set_sauce(self, sauce: str) -> 'PizzaBuilder':
        self._sauce = sauce
        return self

    def set_cheese(self, cheese: str) -> 'PizzaBuilder':
        self._cheese = cheese
        return self

    def add_topping(self, topping: str) -> 'PizzaBuilder':
        self._toppings.append(topping)
        return self

    def build(self) -> Pizza:
        return Pizza(self._crust, self._sauce, self._cheese, self._toppings)


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder) -> None:
        self._builder = builder

    def construct_veggie_pizza(self) -> Pizza:
        return (self._builder
                    .set_crust("thin")
                    .set_sauce("pesto")
                    .set_cheese("goat cheese")
                    .add_topping("bell peppers")
                    .add_topping("olives")
                    .add_topping("onions")
                    .build())

    def construct_meat_lovers_pizza(self) -> Pizza:
        return (self._builder
                    .set_crust("thick")
                    .set_sauce("barbecue")
                    .set_cheese("cheddar")
                    .add_topping("pepperoni")
                    .add_topping("sausage")
                    .add_topping("bacon")
                    .build())


if __name__ == '__main__':
    builder = PizzaBuilder()
    director = PizzaDirector(builder)

    # Construct a veggie pizza
    veggie_pizza = director.construct_veggie_pizza()
    print(veggie_pizza)

    # Construct a meat lovers pizza
    meat_lovers_pizza = director.construct_meat_lovers_pizza()
    print(meat_lovers_pizza)

    # Custom pizza without using the director
    custom_pizza = (builder
                        .set_crust("stuffed")
                        .set_sauce("alfredo")
                        .set_cheese("provolone")
                        .add_topping("mushrooms")
                        .add_topping("spinach")
                        .build())
    print(custom_pizza)
