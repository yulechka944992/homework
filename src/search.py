import re


def process_bank_search(process_bank_list:list[dict[str, str]], search:str)->list[dict[str, str]]:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
        а возвращает список словарей, у которых в любом значении есть данная строка."""
    try:
        pattern = re.compile(search, re.IGNORECASE)
        new_list_dict = []
        for item in process_bank_list:
            if any(pattern.search(str(value)) for value in item.values()):
                new_list_dict.append(item)

    except Exception as e:
        print(f"Внимание! Ошибка {e}! Введены не корректные данные!")

    return new_list_dict


list_sort_data = [
    {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]

print(process_bank_search(list_sort_data, "EXECUTED"))
print(process_bank_search(list_sort_data, "41428829"))