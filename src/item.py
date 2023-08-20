import csv,os


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity
    def __repr__(self):
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

        return self.price

    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        cls.all.clear()
        if not os.path.exists(path):
            raise FileNotFoundError("_Отсутствует файл item.csv_")
        else:
            with open(path, 'r', encoding='cp1251') as file:

                if len(file.readlines()) != 5:
                    raise InstantiateCSVError("_Файл item.csv поврежден_")
                else:
                    reader = csv.reader(file)
                    for row in reader:
                        name, price, quantity = row
                        cls.all.append(cls(name, price, quantity))

    @staticmethod
    def string_to_number(file):
        return int(float(file))

    @property
    def name(self):
        return f'{self.__name}'

    @name.setter
    def name(self, name):
        if len(name) <= 10:
            self.__name = name
        else:
            raise ValueError("Exception: Длина наименования товара превышает 10 символов")


