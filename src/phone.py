from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, col_sim):
        super().__init__(name, price, quantity)
        self.__col_sim = col_sim

    @property
    def number_of_sim(self):
        return self.__col_sim

    @number_of_sim.setter
    def number_of_sim(self, col_sim):
        if col_sim > 0:
            self.__col_sim = col_sim
        else:
            raise ValueError("Exception: Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__col_sim})"

    def __str__(self):
        return f"{self.name}"