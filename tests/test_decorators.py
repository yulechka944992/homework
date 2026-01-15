import os

import pytest

from src.decorators import log
from src.widget import mask_account_card


def test_my_function_success(capsys):
    """Проверка на успешное выполнение функции"""

    @log()
    def my_function(x, y):
        return x / y

    result = my_function(4, 2)
    assert result == 2
    captured = capsys.readouterr()
    assert "my_function ок. Результат: 2.0" in captured.out


def test_my_function_division_by_zero(capsys):
    """Проверка обработки ошибки деления на 0"""

    @log()
    def my_function(x, y):
        return x / y

    result = my_function(4, 0)
    captured = capsys.readouterr()

    assert result is None
    assert "my_function error: ZeroDivisionError. Inputs: (4, 0), {}\n" in captured.out


def test_my_function_log_txt():
    """Проверка на вывод в файл"""

    @log(filename="test_log.txt")
    def my_function_sum(x, y):
        return x + y

    my_function_sum(2, 3)

    with open("test_log.txt", "r", encoding="utf-8") as file:
        content = file.read()

    assert "Функция my_function_sum ок. Результат: 5" in content
    os.remove("test_log.txt")


@log()
def my_function_key_error():
    return {"a": 1}["b"]


def test_my_function_key_error(capsys):
    """Проверка обработки исключений"""
    my_function_key_error()
    captured = capsys.readouterr()
    assert "my_function_key_error error: KeyError" in captured.out


def test_mask_account_card_with_log_success(capsys):
    """Тест успешного маскирования карты с логированием"""

    @log()
    def masked_card(card_number):
        return mask_account_card(card_number)

    result = masked_card("Visa Platinum 7000792289606361")

    assert "7000 79** **** 6361" in result

    # Проверяем лог в консоли
    captured = capsys.readouterr()
    assert "masked_card ок. Результат:" in captured.out
    assert "7000 79** **** 6361" in captured.out
