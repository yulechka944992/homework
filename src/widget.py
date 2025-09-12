from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_number: str ) -> str:
    """Функция, которая маскирует информацию о картах и счетах"""
    if not card_number or len(card_number) < 16:
        return "Номер карты короткий или пустой"
    card_number_split = card_number.split()
    card_number_digit = ""
    card_number_alpha = ""
    for card_number_item in card_number_split:
        if card_number_item.isdigit():
            card_number_digit += card_number_item
        if card_number_item.isalpha():
            card_number_alpha += card_number_item


    if card_number_alpha == "Счет":
        return f"{card_number_alpha} {get_mask_account(card_number_digit)}"
    else:
        return card_number.replace(card_number[-16:], get_mask_card_number(card_number[-16:]))


def get_date(date: str) -> str | None:
    """Функция преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
