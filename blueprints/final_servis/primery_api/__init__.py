# blueprints/final_servis/primery_api/__init__.py
from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('sushchnosti',
                      'Примеры API запросов, оперирующих сущностями')

model_sushchnosti = namespace.model('Element', {
    'id': fields.Integer(
        readonly=True,
        description='Идентификатор сущности'
    ),
    'name': fields.String(
        required=True,
        description='Имя сущности'
    )
})

entity_list_model = namespace.model('SpisokElementov', {
    'entities': fields.Nested(
        model_sushchnosti,
        description='Список сущностей',
        as_list=True
    ),
    'total_records': fields.Integer(
        description='Общее количество сущностей',
    ),
})

primer_sushchnosti = {'id': 1, 'name': 'Имя сущности'}

@namespace.route('')
class sushchnosti(Resource):
    '''Получение списка уже имеющихся сущностей, а также создание новой сущности'''
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(entity_list_model)
    def get(self):
        '''Получение списка со всеми уже имеющимися сущностями'''
        entity_list = [primer_sushchnosti]
        return {
            'entities': entity_list,
            'total_records': len(entity_list)
        }
    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(model_sushchnosti)
    @namespace.marshal_with(model_sushchnosti, code=HTTPStatus.CREATED)
    def post(self):
        '''Создание новой (дополнительной) сущности'''

        if request.json['name'] == 'Имя сущности':
            namespace.abort(400, 'Entity with the given name already exists')
        return primer_sushchnosti, 201

@namespace.route('/<int:entity_id>')
class element(Resource):
    '''Чтение, обновление и удаление отдельно указываемой сущности'''
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_with(model_sushchnosti)
    def get(self, entity_id):
        '''Получение информации об отдельно указанной сущности'''
        return primer_sushchnosti

    @namespace.response(400, 'Entity with the given name already exists')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    @namespace.expect(model_sushchnosti, validate=True)
    @namespace.marshal_with(model_sushchnosti)
    def put(self, entity_id):
        '''Обновление (изменение) отдельно указанной сущности'''
        if request.json['name'] == 'Имя сущности':
            namespace.abort(400, 'Entity with the given name already exists')
        return primer_sushchnosti

    @namespace.response(204, 'Request Success (No Content)')
    @namespace.response(404, 'Entity not found')
    @namespace.response(500, 'Internal Server error')
    def delete(self, entity_id):
        '''Удаление отдельно указанной сущности'''
        return '', 204