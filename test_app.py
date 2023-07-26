import pytest
import main


@pytest.fixture
def client():
    main.app.testing = True
    return main.app.test_client()


def test_correct_data(client):
    data = {
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90",
        "order_date": "01.01.2023",
        "description": "Test order"
    }
    response = client.post('/get_form', json=data)
    assert response.status_code == 200


def test_incorrect_data(client):
    data = {
        "user_email": "invalid_email",
        "user_phone": "123",
        "order_date": "2023-01-01",
        "description": "Test order"
    }
    response = client.post('/get_form', json=data)
    assert response.status_code == 200


def test_missing_fields(client):
    data = {
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90"
    }
    response = client.post('/get_form', json=data)
    assert response.status_code == 200


def test_non_matching_template(client):
    data = {
        "name": "TestForm",
        "user_email": "test@example.com",
        "user_phone": "+7 123 456 78 90",
        "order_date": "01.01.2023",
        "description": "Test order"
    }
    response = client.post('/get_form', json=data)
    assert response.status_code == 200


def test_single_field_data(client):
    data = {
        "user_email": "test@example.com",
    }
    response = client.post('/get_form', json=data)
    assert response.status_code == 200
