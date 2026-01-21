import json
import os


def load_json(file_path: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях
    """
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)

            if not isinstance(data, list):
                return []

            return data

    except (FileNotFoundError, json.JSONDecodeError):
        return []


print(load_json("../data/operations.json"))
