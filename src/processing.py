def filter_by_state(list_of_dicts: list, id_state: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    new_list_of_dicts = []
    for dictionary in list_of_dicts:
        if dictionary.get("state") == id_state:
            new_list_of_dicts.append(dictionary)
    return new_list_of_dicts


def sort_by_date(list_of_dicts: list, is_reverse: bool = True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Функция возвращает новый список, отсортированный по дате."""
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=is_reverse)
    return sorted_list
