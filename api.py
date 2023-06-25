import flask
from flask import Flask, request, jsonify
from db_commands import address_selection
from flask_cors import CORS
import json
import re
import psycopg2

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
host = user = password = db_name = port = ''
with open('db_variables') as db_info:
    db_info = json.load(db_info)
    for k, v in db_info.items():
        globals()[k] = v

@app.route('/addresses')
def addresses():
    region = request.args.get('region', '')
    settlement = request.args.get('settlement', '')
    street = request.args.get('street', '')
    house = request.args.get('house', '')
    post_code = request.args.get('post_code', '')

    error_validation_message = [('Address not valid')]

    if region != '' and re.match("^[а-яА-ЯіІїЇёЁ ]+$", region) is None:
        return json.dumps(error_validation_message).encode('utf8')
    if settlement != '' and re.match("^[а-яА-ЯіІїЇёЁ ]+$", settlement) is None:
        return json.dumps(error_validation_message).encode('utf8')
    if street != '' and re.match("^[а-яА-ЯіІїЇёЁ0-9. ]+$", street) is None:
        return json.dumps(error_validation_message).encode('utf8')
    if house != '' and re.match("^[а-яА-ЯіІїЇёЁ0-9. ]+$", house) is None:
        return json.dumps(error_validation_message).encode('utf8')
    if post_code != '' and re.match("^[0-9]{0,5}$", post_code) is None:
        return json.dumps(error_validation_message).encode('utf8')

    connection = psycopg2.connect(host=host, user=user, password=password, dbname=db_name, port=port)
    connection.autocommit = True
    selected_addresses = address_selection(connection, region, settlement, street, house, post_code)
    connection.close()
    if selected_addresses == []:
        no_address_messege = [('No such address')]
        return json.dumps(no_address_messege).encode('utf8')
    resp = flask.Response(json.dumps(selected_addresses, ensure_ascii=False).encode('utf8'))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
