# page2.py
from flask import Flask, request
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

# blueprints/azy/primery_api/__ini__.py
from flask import Blueprint, request

blueprint = Blueprint('api', __name__, url_prefix='/azy')

@blueprint.route('/primery_api', methods=['GET', 'POST'])
def sushchnosti():
    if request.method == "GET":
        return {
            'сообщение': 'Настоящий API запрос должен возвращать'
                         ' список сущностей',
            'метод': request.method
        }
    if request.method == "POST":
        return {
            'сообщение': 'Данный API запрос обеспечивает создание'
                         ' дополнительной сущности',
            'дополнительная_сущность': request.json,
            'метод': request.method
            }

@blueprint.route('/primery_api/<int:element_id>', methods=['GET', 'PUT', 'DELETE'])
def element(element_id):
    if request.method == "GET":
        return {
            'id': element_id,
            'сообщение': 'Настоящий API запрос возвращает информацию об отдельной сущности {}'.format(element_id),
            'метод': request.method
        }
    if request.method == "PUT":
        return {
            'id': element_id,
            'сообщение': 'Данный API запрос обновляет отдельную сущность {}'
            .format(element_id),
            'метод': request.method,
        'body': request.json
        }
    if request.method == "DELETE":
        return {
            'id': element_id,
            'сообщение': 'Настоящий API запрос удаляет отдельную сущность {}'
            .format(element_id),
            'метод': request.method
        }

if __name__ == "__main__":
    app.run(debug=True)