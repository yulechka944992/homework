from typing import Any, Generator, Iterator


def filter_by_currency(transactions_dict: list[dict], currency: str) -> Iterator[dict]:
    """
    Функция принимает список словарей на вход и возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует currency.
    """

    for transaction in transactions_dict:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions_dict: list) -> Generator[Any, Any, None]:
    """Генератор принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for transaction in transactions_dict:
        yield transaction["description"]


def card_number_generator(start: int=1, stop: int=9999999999999999) -> Generator:
    """Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    current = start
    while current <= stop:
        num_str = f"{current:016d}"
        yield " ".join([num_str[i : i + 4] for i in range(0, 16, 4)])
        current += 1
