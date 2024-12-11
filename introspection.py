import inspect


def introspection_info(obj):
    # Определяем тип объекта
    type_ = type(obj).__name__

    # Получаем список всех атрибутов объекта
    attributes = dir(obj)

    # Фильтруем методы от других атрибутов
    methods = [attr for attr in attributes if callable(getattr(obj, attr))]

    # Определяем модуль, к которому относится объект
    module = getattr(obj, '__module__', None)

    # Собираем всю информацию в словарь
    info = {
        'type': type_,
        'attributes': attributes,
        'methods': methods,
        'module': module
    }

    return info


# Пример использования
number_info = introspection_info(42)
print(number_info)
