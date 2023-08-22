def insert_test_forms(db_instance):
    db_instance.insert({
        "name": "Order_form",
        "user_email": "email",
        "user_phone": "phone",
        "order_date": "date",
        "description": "text"
    })
    db_instance.insert({
        "name": "MyForm",
        "email": "email",
        "phone": "phone"
    })
    db_instance.insert({
        "name": "passport_form",
        "username": "text",
        "email": "email",
        "phone_number": "phone",
        "date": "date",
        "comment": "text"
    })
    db_instance.insert({
        "name": "Callback form",
        "username": "text",
        "phone_number": "phone"
    })

