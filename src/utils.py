import json
import os
# import logging
#
#
# logger = logging.getLogger('utils')
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler("../logs/utils.log", mode='w', encoding='utf-8')
# file_handler.setLevel(logging.INFO)
# file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
# file_handler.setFormatter(file_formatter)
# logger.addHandler(file_handler)


def load_json(file_path: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    if not os.path.exists(file_path):
        # logger.error("Нет файла по указанному пути.")
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

            if not isinstance(data, list):
                # logger.error("Файл не является списком!")
                return []
            # logger.info("Файл найден, возвращается список словарей.")
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        # logger.error("Ошибка! Файл не найден или не преобразован.")
        return []


# print(load_json("../data/operations.json"))
