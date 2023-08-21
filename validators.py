import re


date_pattern = re.compile(
    r"^(?:(?:(?:(?:0[1-9]|[1-2][0-9]|3[0-1])\.(?:0[13578]|1[02]))|(?:(?:0[1-9]|[1-2][0-9]|30)\." \
    r"(?:0[469]|11))|(?:(?:0[1-9]|[1-2][0-9])\.02))\." \
    r"(?:1[0-9][0-9][0-9]|2[0-9][0-9][0-9]))|(?:(?:29\.02\." \
    r"(?:1[0-9][0-9][0-9]|2[0-9][0-9][0-9])))$|^(?:(?:1[0-9][0-9][0-9]|2[0-9][0-9][0-9])-" \
    r"(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|[1-2][0-9]|3[0-1])))$"
)

phone_pattern = re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$")
email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def is_valid_date(date):
    """ Check if the date corresponds to the format DD.MM.YYYY or YYYY-MM-DD """
    return bool(date_pattern.match(date))


def is_valid_phone(phone_number):
    """ Check if the phone number matches the mask: +7 xxx xxx xx xx """
    return bool(phone_pattern.match(phone_number))


def is_valid_email(email):
    """ Check if the email matches the email mask: x@x.xx """
    return bool(email_pattern.match(email))
