from flask import request
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

namespace = Namespace('db_selector',
                      'An example of an API request that collects addresses from the database by arguments')

model_sushchnosti = namespace.model('One Address', {
    'address_id': fields.Integer(
        readonly=True,
        description='address id in data base'
    ),
    'region': fields.String(
        required=True,
        description='region of Ukraine'
    ),
    'settlement': fields.String(
        required=True,
        description='settlement in Ukraine'
    ),
    'street': fields.String(
        required=True,
        description='street in Ukrainian settelement'
    ),
    'house': fields.String(
        required=True,
        description='house number'
    ),
    'post_code': fields.String(
        required=True,
        description='address postal code'
    ),
})

entity_list_model = namespace.model('Addresses List', {
    'addresses': fields.Nested(
        model_sushchnosti,
        description='addresses list',
        as_list=True
    ),
    'total selected addresses': fields.Integer(
        description='Number of addresses in the sample',
    ),
})

primer_sushchnosti = {'address_id': 1, 'region': 'Київська область', 'settlement': 'Київ', 'street': 'Київська вулиця', 'house': 'буд.1', 'post_code': '00000'}

@namespace.route('')
class sushchnosti(Resource):
    '''Get list of addresses'''
    @namespace.response(500, 'Internal Server error')
    @namespace.marshal_list_with(entity_list_model)
    def get(self):
        '''Get list of addresses'''
        entity_list = [primer_sushchnosti]
        return {
            'entities': entity_list,
            'total_records': len(entity_list)
        }