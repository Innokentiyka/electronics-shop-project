"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
class TestCalculateTotalPrice:
    def test_calculate_total_price(self):
        obj = Item("Ноут", 10, 5)
        result = obj.calculate_total_price()
        assert result == 50

