import requests
from faker import Faker


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


def generate_test_data():
    test_data = []
    for _ in range(len(forms_in_database)):
        correct_data = {
            0: {
                "user_email": faker.email(),
                "user_phone": "+7 " + faker.numerify('### ### ## ##'),
                "order_date": faker.date(),
                "description": faker.sentence()
            },
            1: {
                "email": faker.email(),
                "phone": "+7 " + faker.numerify('### ### ## ##')
            },
            2: {
                "username": faker.name(),
                "email": faker.email(),
                "phone_number": "+7 " + faker.numerify('### ### ## ##'),
                "date": faker.date(),
                "comment": faker.sentence()
            },
            3: {
                "username": faker.name(),
                "phone_number": "+7 " + faker.numerify('### ### ## ##')
            }
        }
        test_data.append(correct_data[_])
    return test_data


test_data = generate_test_data()


for idx, data in enumerate(test_data, start=1):
    response = requests.post(f"{base_url}/get_form", data=data)
    response_data = response.json()

    print(f"Test Case {idx}\nInput data:\n\t{data}\nResponse:\n\t{response_data}\n")
