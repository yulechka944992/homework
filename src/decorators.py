from functools import wraps


def log(filename=None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                name_func = func.__name__
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"Функция {name_func} ок. Результат: {result}" + "\n")
                    file.close()
                else:
                    print(f"{name_func} ок. Результат: {func(*args, **kwargs)}")
            except Exception as e:
                result = None
                print(f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}")
            return result

        return wrapper

    return decorator
