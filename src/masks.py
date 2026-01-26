import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", mode='w', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_cart: str) -> str:
    """Функция принимает на вход номер карты и возвращает её маску."""
    if len(number_cart) != 16:
        logger.error("Некорректный номер карты!")
        return "Некорректный номер карты!"
    logger.info(f"Карта успешно замаскирована.")
    return f"{number_cart[0:4]} {number_cart[4:6]}** **** {number_cart[-4:]}"


def get_mask_account(number_personal_account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""
    if len(number_personal_account) < 12:
        logger.error("Некорректный номер счета!")
        return "Некорректный номер счета!"
    number_mask = number_personal_account[-4:]
    logger.info(f"Номер счета успешно замаскирован.Длина {len(number_personal_account)} цифр, "
                f"Маска: **{number_mask}")
    return f"**{number_mask}"
