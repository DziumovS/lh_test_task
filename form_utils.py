from patterns import DATE_PATTERN, PHONE_PATTERN, EMAIL_PATTERN


VALIDATION_FUNCTIONS = {
    "date": lambda x: bool(DATE_PATTERN.match(x)),
    "phone": lambda x: bool(PHONE_PATTERN.match(x)),
    "email": lambda x: bool(EMAIL_PATTERN.match(x))
}


TYPE_MAPPING = {
    "date": "date",
    "phone": "phone",
    "email": "email"
}


def fields_value_structure_matching(form, data):
    """ Check whether the values in the incoming data correspond to the format of values in the corresponding form """
    for key, value in form.items():
        if key == "name":
            continue
        validation_function = VALIDATION_FUNCTIONS.get(value, lambda x: True)
        if not validation_function(data.get(key)):
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
        display_type = TYPE_MAPPING.get(value, "text")
        result[key] = display_type
    return result


def get_form_name(forms, data):
    """ Define the name of the form """
    data_keys = set(data.keys())  # Save data keys for use in fields_key_matching

    for form in forms:
        if not fields_key_matching(form, data_keys):
            continue
        if fields_value_structure_matching(form, data):
            return form["name"]
    return None


def validate_value(value_type, value):
    """ Check the value according to the type """
    validation_function = VALIDATION_FUNCTIONS.get(value_type, lambda x: True)
    return validation_function(value)
