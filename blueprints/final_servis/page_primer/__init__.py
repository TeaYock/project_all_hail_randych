# blueprints/final_servis/page_primer/__init__.py
from flask import request
from flask_restx import Namespace, Resource, fields

namespace = Namespace('address_selection',
                      'Selection of addresses matching the arguments')

welcome_text_model = namespace.model('Addresses Selection', {
    'Selected addresses': fields.String(
        readonly=True,
        description='<h1>Мне кажется, или я реально уже в браузере?!</h1>'
    )
})

welcome_text_primer = {'message': 'Мне кажется, или я реально уже в браузере?!'}

@namespace.route('')
class WelcomeText(Resource):
    @namespace.marshal_list_with(welcome_text_model)
    @namespace.response(500, 'Internal Server error')
    def get(self):
        '''Getting a selection of addresses by given arguments'''
        return welcome_text_primer