import requests
from faker import Faker
import random


base_url = "http://localhost:5000"

faker = Faker()


def generate_test_data():
    test_data = []
    for _ in range(18):
        valid = random.choice([True, False])
        data = {
            "user_email": faker.email() if valid else "invalid_email",
            "user_phone": "+7 " + faker.numerify('### ### ## ##') if valid else "invalid_phone",
            "order_date": faker.date() if valid else "25-08-2023",
            "description": faker.sentence() if valid else "Invalid order description",
            "email": faker.email() if valid else "invalid_email",
            "phone": faker.phone_number() if valid else "1234567890",
            "username": faker.name() if valid else "Invalid User",
            "phone_number": faker.phone_number() if valid else "invalid_phone",
            "date": faker.date() if valid else "2023-09-15",
            "comment": faker.sentence() if valid else "Invalid comment"
        }
        test_data.append(data)
    return test_data


test_data = generate_test_data()


for idx, data in enumerate(test_data, start=1):
    response = requests.post(f"{base_url}/get_form", data=data)
    response_data = response.json()

    print(f"Response for Test Case {idx}:\n\t{response_data}\n")
