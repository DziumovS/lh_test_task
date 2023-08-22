import requests
from faker import Faker
import random


base_url = "http://localhost:5000"

faker = Faker()


forms_in_database = {
    0: {
        "name": "Order_form",
        "user_email": "email",
        "user_phone": "phone",
        "order_date": "date",
        "description": "text"
    },
    1: {
        "name": "MyForm",
        "email": "email",
        "phone": "phone"
    },
    2: {
        "name": "Callback form",
        "username": "text",
        "phone_number": "phone"
    },
    3: {
        "name": "passport_form",
        "username": "text",
        "email": "email",
        "phone_number": "phone",
        "date": "date",
        "comment": "text"
    }
}


def generate_random_test_data():
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


def generate_correct_test_data():
    test_data = []
    for _ in range(len(forms_in_database)):
        correct_data = {
            0: {
                "user_email": "example@example.com",
                "user_phone": "+7 123 456 78 90",
                "order_date": "29.02.2023",
                "description": "test description"
            },
            1: {
                "email": "example@example.com",
                "phone": "+7 123 456 78 90"
            },
            2: {
                "username": "leadhit",
                "email": "example@example.com",
                "phone_number": "+7 123 456 78 90",
                "date": "2023-01-01",
                "comment": "test comment"
            },
            3: {
                "username": "leadhit",
                "phone_number": "+7 123 456 78 90"
            }
        }
        test_data.append(correct_data[_])
    return test_data



test_data = generate_correct_test_data()
#test_data = generate_random_test_data()


for idx, data in enumerate(test_data, start=1):
    response = requests.post(f"{base_url}/get_form", data=data)
    response_data = response.json()

    print(f"Response for Test Case {idx}:\n\t{response_data}\n")
