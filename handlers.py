from validators import is_valid_date, is_valid_phone, is_valid_email


def fields_value_structure_matching(form, data, validate_value_func):
    """ Check whether the values in the incoming data correspond to the format of values in the corresponding form """
    for key, value in form.items():
        if key == "name":
            continue
        if not validate_value_func(value, data.get(key)):
            return False
    return True


def fields_key_matching(form, data_keys):
    """ Check if there is at least one corresponding form by keys in the form templates """
    for key in form:
        if key == "name":
            continue
        if key not in data_keys:
            return False
    return True


def get_fields_list_and_they_types(data):
    """ On-the-fly typing of fields and return a list of fields with their types """
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
    """ Define the name of the form """
    data_keys = set(data.keys())  # Save data keys for use in fields_key_matching

    for form in forms:
        if not fields_key_matching(form, data_keys):
            continue
        if fields_value_structure_matching(form, data, validate_value):
            return form["name"]
    return None


def validate_value(value_type, value):
    """ Check the value according to the type """
    if value_type == "date":
        return is_valid_date(value)
    elif value_type == "phone":
        return is_valid_phone(value)
    elif value_type == "email":
        return is_valid_email(value)
    return True
