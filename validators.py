import re


def is_valid_date(date):
    """ На вход подается строка с датой в формате DD.MM.YYYY или YYYY-MM-DD
        YYYY = True если значение находится в диапазоне от 1000 по 9999 включительно
        MM = True если значение находится в диапазоне от 01 по 12 включительно, где 01 - январь, 02 - февраль и т.д.
        DD = True если значение как в реальности: число соответствует возможному числу в месяце """
    date_pattern = r"^(?:(?:(?:(?:0[1-9]|[1-2][0-9]|3[0-1])\.(?:0[13578]|1[02]))|(?:(?:0[1-9]|[1-2][0-9]|30)\." \
                   r"(?:0[469]|11))|(?:(?:0[1-9]|[1-2][0-9])\.02))\." \
                   r"(?:1[0-9][0-9][0-9]|2[0-9][0-9][0-9]))|(?:(?:29\.02\." \
                   r"(?:1[0-9][0-9][0-9]|2[0-9][0-9][0-9])))$|^(?:(?:1[0-9][0-9][0-9]|2[0-9][0-9][0-9])-" \
                   r"(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])))$"

    if not re.match(date_pattern, date):
        return False

    if "." in date:
        day, month, year = map(int, date.split("."))
    else:
        year, month, day = map(int, date.split("-"))

    if month == 2:
        if 1 <= day <= 29 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            return True
        elif 1 <= day <= 28:
            return True
        else:
            return False
    elif month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    else:
        return 1 <= day <= 31


def is_valid_phone(phone_number):
    """ Проверяем соответствует ли номер телефона маске: +7 xxx xxx xx xx """
    phone_number_pattern = r"^\+7 \d{3} \d{3} \d{2} \d{2}$"
    return True if re.match(phone_number_pattern, phone_number) else False


def is_valid_email(email):
    """ Проверяем соответствует ли email маске: x@x.xx """
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return True if re.match(email_pattern, email) else False


def is_valid_text(text):
    return True


validate_value = {"date": is_valid_date, "phone": is_valid_phone, "email": is_valid_email, "text": is_valid_text}
