def filter_by_state(list_dict: list[dict[str, int | str]], id_state: str = "EXECUTED") -> list[dict[str, int | str]]:
    """Функция, которая принимает список словарей и значение для ключа state(по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению.
    """
    new_list_dict = []
    for dictionary in list_dict:
        if dictionary.get("state") == id_state:
            new_list_dict.append(dictionary)
    return new_list_dict


def sort_by_date(list_dict: list[dict[str, int | str]], is_reverse: bool = True) -> list[dict[str, int | str]]:
    """Функция, которая принимает список словарей и необязательный параметр, задающий порядок сортировки.
    Функция возвращает новый список, отсортированный по дате."""
    sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=is_reverse)
    return sorted_list
