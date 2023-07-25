from flask import Flask, request, json
import re
from handlers import fields_key_matching, fields_value_structure_matching, get_fields_list_and_they_types, get_form_name
from testdata import test_forms, test_data


#app = Flask(__name__)


# @app.route("/get_form", methods=["POST"])
# def get_form():
#     data = request.form.to_dict()
#     form_name = get_form_name(test_forms, data)
#     if form_name:
#         return jsonify({"form_name": form_name})
#     return jsonify(get_fields_list_and_they_types(data))


for data in test_data:
    form_name = get_form_name(test_forms, data)
    if form_name:
        print({"form_name": form_name})
    print(json.dumps(get_fields_list_and_they_types(data)))
