from flask import Flask, request, jsonify
from tinydb import TinyDB
from form_utils import get_fields_list_and_they_types, get_form_name


db = TinyDB('db.json')
app = Flask(__name__)


@app.route("/get_form", methods=["POST"])
def get_form():
    data = request.form.to_dict()
    forms_from_db = db.all()

    if not data:
        return jsonify({"error": "No data in the request"})

    fields_and_types = get_fields_list_and_they_types(data)

    form_name = get_form_name(forms_from_db, data)

    if form_name:
        return jsonify({"form_name": form_name})

    return jsonify(fields_and_types)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
