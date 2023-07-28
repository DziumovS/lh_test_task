from validators import is_valid_date, is_valid_phone, is_valid_email


def fields_value_structure_matching(form, data, validate_value_func):
    """ Проверяем соответствуют ли значения во входящих данных формату значений в соответствующей форме """
    for key, value in form.items():
        if key == "name":
            continue
        if not validate_value_func(value, data.get(key)):
            return False
    return True


def fields_key_matching(form, data_keys):
    """ Проверяем есть ли в шаблонах форм хотя бы одна соответствующая форма по ключам """
    for key in form:
        if key == "name":
            continue
        if key not in data_keys:
            return False
    return True


def get_fields_list_and_they_types(data):
    """ Проводим на лету типизацию полей и возвращаем список полей с их типами """
    result = {}
    for key, value in data.items():
        if is_valid_date(value):
            result[key] = "date"
        elif is_valid_phone(value):
            result[key] = "phone"
        elif is_valid_email(value):
            result[key] = "email"
        else:
            result[key] = "text"
    return result


def get_form_name(forms, data):
    """ Определяем имя формы """
    data_keys = set(data.keys())  # Сохраняем ключи данных для использования в fields_key_matching

    for form in forms:
        if not fields_key_matching(form, data_keys):
            continue
        if fields_value_structure_matching(form, data, validate_value):
            return form["name"]
    return None


def validate_value(value_type, value):
    """ Проверяем значение в соответствии с типом """
    if value_type == "date":
        return is_valid_date(value)
    elif value_type == "phone":
        return is_valid_phone(value)
    elif value_type == "email":
        return is_valid_email(value)
    return True
