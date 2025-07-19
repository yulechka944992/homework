from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


def test_empty_string_card_number() -> None:
    """Пустая строка возвращает строку с пробелами и звёздочками."""
    assert get_mask_card_number("") == " ** **** "


def test_get_mask_account() -> None:
    assert get_mask_account("73654108430135874305") == "**4305"


def test_empty_string_mask_account() -> None:
    """Пустая строка возвращает строку со звёздочками."""
    assert get_mask_account("") == "**"
