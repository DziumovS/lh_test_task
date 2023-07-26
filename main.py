from flask import Flask, request, jsonify
from tinydb import TinyDB
from handlers import get_fields_list_and_they_types, get_form_name


db = TinyDB('db.json')
app = Flask(__name__)


@app.route("/get_form", methods=["POST"])
def get_form():
    data = request.json
    forms_from_db = db.all()
    form_name = get_form_name(forms_from_db, data)
    if form_name:
        return jsonify({"form_name": form_name})
    return jsonify(get_fields_list_and_they_types(data))


if __name__ == '__main__':
    app.run(debug=True)