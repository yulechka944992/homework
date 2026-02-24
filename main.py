# from src.masks import get_mask_account, get_mask_card_number
import os.path

from src.generators import filter_by_currency
from src.search import process_bank_search
from src.processing import filter_by_state, sort_by_date
from src.read_files import read_csv, read_excel
from src.utils import load_json
from src.widget import mask_account_card, get_date

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

choice_func = {
    '1': ("JSON", load_json, "operations.json"),
    '2': ("CSV", read_csv, "transactions.csv"),
    '3': ("XLSX", read_excel, "transactions_excel.xlsx")
}


def ask_yes_no(question: str) -> bool:
    """"""
    while True:
        answer = input(f"Программа: {question} (Да/Нет): ").strip().lower()
        if answer in ('да', 'нет'):
            return answer == 'да'
        print('Программа: Пожалуйста, введите "Да", "Нет".')


def main():
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:\n "
          "1. Получить информацию о транзакциях из JSON-файла\n "
          "2. Получить информацию о транзакциях из CSV-файла\n "
          "3. Получить информацию о транзакциях из XLSX-файла")

    # 1. Выбор файла
    while True:
        choice = input('Пользователь:').strip()
        if choice in choice_func:
            format_file, func, file_type = choice_func[choice]
            print(f'Программа: Для обработки выбран {format_file}.')
            transactions = func(os.path.join(DATA_DIR, file_type))
            break
        print("Выбран неверный формат! Пожалуйста,выберите 1,2 или 3.")

    # 2. Фильтр по статусу
    filter_statuses = {'EXECUTED', 'CANCELED', 'PENDING'}
    while True:
        print('Программа: Введите статус, по которому необходимо выполнить фильтрацию.')
        print(f'Доступные статусы: {", ".join(filter_statuses)}')
        status = input('Пользователь: ').strip().upper()
        if status in filter_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status}"')
            transactions = filter_by_state(transactions, status)
            break
        print(f'Программа: Статус операции "{status}" недоступен.')

    # 3. Сортировка по дате
    if ask_yes_no('Отсортировать операции по дате?'):
        while True:
            print('Программа: Отсортировать по возрастанию или по убыванию?')
            order = input('Пользователь: ').strip().lower()
            if order in ['по возрастанию', 'по убыванию']:
                transactions = sort_by_date(transactions, is_reverse=(order == 'по убыванию'))
                break
            else:
                print('Программа: Пожалуйста, введите "по возрастанию" или "по убыванию".')

    # 4. Фильтр по рублевым транзакциям
    if ask_yes_no('Выводить только рублевые транзакции?'):
        transactions = list(filter_by_currency(transactions, "RUB"))

    # 5. Фильтр по слову в описании
    if ask_yes_no('Отфильтровать список транзакций по слову в описании?'):
        keyword = input('Программа: Введите слово для фильтрации:\nПользователь: ').strip()
        transactions = process_bank_search(transactions, keyword)

    # 6. Вывод результата
    print('Программа: Распечатываю итоговый список транзакций...\n')
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    if len(transactions) > 0:
        for transaction in transactions:
            print(get_date(transaction.get("date")), transaction.get("description"))
            if not transaction.get("from"):
                print(mask_account_card(transaction.get("to")))
            elif not transaction.get("to"):
                print(mask_account_card(transaction.get("from")))
            else:
                print(mask_account_card(transaction.get("from"))), "->", mask_account_card(transaction.get("to"))
            amount = (
                    transaction.get('operationAmount', {})
                    .get('amount')
                    or transaction.get('amount', 'Сумма не указана')
            )
            print(f"Сумма: {amount}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == '__main__':
    main()

# print(get_mask_card_number("7000792289606361"))
# print(get_mask_account("736541084301"))
