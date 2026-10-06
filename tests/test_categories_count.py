from typing import Counter

import pytest

from src.categories_count import process_bank_operations
from tests.conftest import transactions_dict


def test_process_bank_operations(transactions_dict: list[dict[str, str]]) -> dict:
    """Тест успешной работы функции"""
    categories_test = ["Перевод с карты на карту", " Перевод организации"]
    test_count_category = process_bank_operations(transactions_dict, categories_test)
    result = dict(test_count_category)
    assert result


def test_process_bank_operations_empty():
    """Тест пустого входного списка- выдает пустой список"""
    categories = ["Первод с карты на карту", "Перевод со счета на счет"]
    result = process_bank_operations([], categories)
    assert result == {}


def test_process_bank_operations_error():
    """Тест: при некореттных данных выдает пустой список"""
    result = process_bank_operations(1, [])
    assert result == {}




