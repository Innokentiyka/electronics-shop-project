"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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

