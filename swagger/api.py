from flask import Flask, request, jsonify
from db_commands import address_selection
import json
import re
import psycopg2


app = Flask(__name__)

from flask import Blueprint
blueprint = Blueprint('swaggerAPI', __name__, url_prefix='/swaggerAPI')

app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False
host = user = password = db_name = port = ''
with open('.env') as db_info:
    db_info = json.load(db_info)
    for k, v in db_info.items():
        globals()[k] = v

@app.route('/addresses')
def addresses():
    region = request.args.get('region', '')
    if re.match("^[а-яА-ЯіІїЇёЁ\s]+$", region) == False:
        return json.dumps('[Address not valid]').encode('utf8')
    settlement = request.args.get('settlement', '')
    if re.match("^[а-яА-ЯіІїЇёЁ]+$", settlement) == False:
        return json.dumps('[Address not valid]').encode('utf8')
    street = request.args.get('street', '')
    if re.match("^[а-яА-ЯіІїЇёЁ0-9.\s]+$", street) == False:
        return json.dumps('[Address not valid]').encode('utf8')
    house = request.args.get('house', '')
    if re.match("^[а-яА-ЯіІїЇёЁ0-9.\s]+$", house) == False:
        return json.dumps('[Address not valid]').encode('utf8')
    post_code = request.args.get('post_code', '')
    if re.match("^[0-9]{5}$", post_code) == False:
        return json.dumps('[Address not valid]').encode('utf8')

    connection = psycopg2.connect(host=host, user=user, password=password, dbname=db_name, port=port)
    connection.autocommit = True
    selected_addresses = address_selection(connection, region, settlement, street, house, post_code)
    connection.close()
    return json.dumps(selected_addresses, ensure_ascii=False).encode('utf8')

if __name__ == '__main__':
    app.run(debug=True)
