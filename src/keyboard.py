from src.item import Item


class KeyBoard(Item):

    def __init__(self, name: str, price: float, quantity: int, language="EN"):
        super().__init__(name, price, quantity)
        self.language = language


    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"

