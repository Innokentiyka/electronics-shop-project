import pytest
from src.phone import Phone
from src.item import Item

phone1 = Phone("iPhone 14", 120_000, 10, 2)
assert str(phone1) == 'iPhone 14'
assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
assert phone1.number_of_sim == 4
assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 4)"

item1 = Item("Смартфон", 10000, 25)
assert item1 + phone1 == 35
assert phone1 + phone1 == 20
