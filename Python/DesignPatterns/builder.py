class Burger:
    def __init__(self, buns: str = None, patty: str = None, cheese: str = None) -> None:
        self._buns = buns
        self._patty = patty
        self._cheese = cheese

    @property
    def buns(self) -> str:
        return self._buns

    @property
    def patty(self) -> str:
        return self._patty

    @property
    def cheese(self) -> str:
        return self._cheese

    def __str__(self) -> str:
        return f"Buns: {self.buns}, Patty: {self.patty}, Cheese: {self.cheese}"


class BurgerBuilder:
    def __init__(self) -> None:
        self._buns: str = None
        self._patty: str = None
        self._cheese: str = None
    
    def add_buns(self, bun_style: str) -> 'BurgerBuilder':
        self._buns = bun_style
        return self

    def add_patty(self, patty_style: str) -> 'BurgerBuilder':
        self._patty = patty_style
        return self

    def add_cheese(self, cheese_style: str) -> 'BurgerBuilder':
        self._cheese = cheese_style
        return self
    
    def build(self) -> Burger:
        return Burger(self._buns, self._patty, self._cheese)


if __name__ == '__main__':
    burger = BurgerBuilder() \
                .add_buns("sesame") \
                .add_patty("fish-patty") \
                .add_cheese("swiss cheese") \
                .build()
    print(burger)
