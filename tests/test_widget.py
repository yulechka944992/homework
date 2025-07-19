import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "input_card, expected",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("", "Номер карты короткий или пустой"),
        ("Maestro 7000792289606361", "Maestro 7000 79** **** 6361"),
    ],
)
def test_mask_account_card(input_card: str, expected: str) -> None:
    assert mask_account_card(input_card) == expected


def test_get_date() -> None:
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("") == ".."
