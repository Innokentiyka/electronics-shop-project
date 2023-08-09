"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone

class TestCalculateTotalPrice:
    def test_calculate_total_price(self, ):
        obj = Item("Ноут", 10, 5)
        result = obj.calculate_total_price()
        assert result == 50

    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

    if __name__ == '__main__':
        item1 = Item("Ноутбук", 10, 200)
        assert repr(item1) == "Item('Ноутбук', 10, 200)"
        assert str(item1) == 'Ноутбук'

phone1 = Phone("iPhone 14", 120_000, 10, 2)
assert str(phone1) == 'iPhone 14'
assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
assert phone1.number_of_sim == 4
assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 4)"

item1 = Item("Смартфон", 10000, 25)
assert item1 + phone1 == 35
assert phone1 + phone1 == 20
