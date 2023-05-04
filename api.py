from flask import Flask, request, jsonify
from db_commands import address_selection
import json
import psycopg2

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

def get_db_connection():
    host = user = password = db_name = port = ''
    with open('.env') as dotenv:
        dotenv = json.load(dotenv)
        for k, v in dotenv.items():
            globals()[k] = v
    connection = psycopg2.connect(host=host, user=user, password=password, dbname=db_name, port=port)
    connection.autocommit = True
    return connection

@app.route('/addresses')
def addresses():
    region = request.args.get('region', '')
    settlement = request.args.get('settlement', '')
    street = request.args.get('street', '')
    house = request.args.get('house', '')
    post_code = request.args.get('post_code', '')

    connection = get_db_connection()
    selected_addresses = address_selection(connection, region, settlement, street, house, post_code)
    connection.close()
    return jsonify(selected_addresses)

if __name__ == '__main__':
    app.run(debug=True)
