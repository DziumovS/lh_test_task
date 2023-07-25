from validators import validate_value


def fields_value_structure_matching(form, data):
    """
        Проверяем соответствуют ли значения во входящих данных формату значений в соответствующей форме
    """
    for key, value in form.items():
        if key == "name":
            continue
        if not validate_value[value](data[key]):
            return False
    return True


def fields_key_matching(form, data):
    """
        Проверяем есть ли в шаблонах форм хотя бы одна соответствующая форма по ключам
    """
    for key in form:
        if key == "name":
            continue
        if key not in data:
            return False
    return True


def get_fields_list_and_they_types(data):
    """
        Проводим на лету типизацию полей и возвращаем список полей с их типами
    """
    result = {}
    for key in data:
        if validate_value["date"](data[key]):
            result[key] = "date"
            continue
        if validate_value["phone"](data[key]):
            result[key] = "phone"
            continue
        if validate_value['email'](data[key]):
            result[key] = "email"
            continue
        result[key] = "text"
    return result


def get_form_name(forms, data):
    name = None
    for form in forms:
        if not fields_key_matching(form, data):
            continue
        else:
            if fields_value_structure_matching(form, data):
                name = form["name"]
                break
    return name
