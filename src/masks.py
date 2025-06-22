def get_mask_card_number(number_cart: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску."""
    return f"{number_cart[0:4]} {number_cart[4:6]}** **** {number_cart[-4:]}"


def get_mask_account(number_personal_account: str) -> str:
    """Функция принимает на вход номер счета  и возвращает его маску."""
    number_mask = number_personal_account[-4:]
    return f"**{number_mask}"
