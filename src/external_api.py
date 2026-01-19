import os
from dotenv import load_dotenv

import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")


def amount_rub(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    if transaction["operationAmount"]["currency"]["code"] != "RUB":
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            result = response.json()
            return float(result["result"])
        else:
            print(f"Ошибка API: {response.status_code}")
            return 0.0
    else:
        return float(transaction["operationAmount"]["amount"])


if __name__ == "__main__":

    transaction = {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }
    print(amount_rub(transaction))
