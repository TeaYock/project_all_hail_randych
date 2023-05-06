from flask import Blueprint
from flask_restx import Api
from swagger.select_swagger import namespace as db_selector

blueprint = Blueprint('swagger', __name__, url_prefix='/swagger')

api_extension = Api(
    blueprint,
    title='Rest API Swagger Selector Documentation',
    version='1.0',
    description='Instructions for the application on the Flask REST API, demonstrating the possibility of obtaining addresses by arguments',
    doc='/doc'
)

api_extension.add_namespace(db_selector)