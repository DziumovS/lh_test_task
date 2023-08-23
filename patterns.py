import re


DATE_PATTERN = re.compile(
    r"^(?:(0[1-9]|[12][0-9]|3[01])\.(0[13578]|1[02])|(0[1-9]|[12][0-9]|30)\.(0[469]|11)|(0[1-9]|[12][0-9])\.02)"
    r"\.(1[0-9]{3}|2[0-9]{3})|(1[0-9]{3}|2[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
)

PHONE_PATTERN = re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$")
EMAIL_PATTERN = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")