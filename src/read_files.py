import pandas as pd
import os
import csv
from typing import Any

csv_file_path = os.path.join(os.getcwd(), "data", "transactions.csv")


def read_csv(csv_file_path: str) -> list[Any] | None:
    """Функция для считывания финансовых операций из CSV выдает список словарей с транзакциями."""
    transactions = []

    try:
        with open(csv_file_path, encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=';')
            for row in csv_reader:
                transactions.append(row)
        return transactions

    except FileNotFoundError:
        print(f"Файл не найден {csv_file_path}")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

# print(read_csv(csv_file_path))


excel_file_path = os.path.join(os.getcwd(), "data", "transactions_excel.xlsx")


def read_excel(excel_file_path: str) -> list[Any] | None:
    """Функция для преобразования Excel файла в список словарей с транзакциями"""
    try:
        excel_reader = pd.read_excel(excel_file_path)
        excel_dict = excel_reader.to_dict(orient='records')
        return excel_dict
    except FileNotFoundError:
        print(f"Excel файл не найден {excel_file_path}")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла Excel: {e}")
        return None

# print(read_excel(excel_file_path))
