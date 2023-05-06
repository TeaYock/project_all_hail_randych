# blueprints/final_servis/__init__.py
from flask import Blueprint
from flask_restx import Api
from blueprints.final_servis.page_primer import namespace as page_primer_ns
from blueprints.final_servis.primery_api import namespace as sushchnosti_ns

blueprint = Blueprint('swagger', __name__, url_prefix='/swagger')

api_extension = Api(
    blueprint,
    title='Rest API Swagger documentation',
    version='1.0',
    description='Instructions for the application on the Flask REST API, demonstrating the possibility of obtaining addresses by arguments',
    doc='/doc'
)

api_extension.add_namespace(page_primer_ns)
api_extension.add_namespace(sushchnosti_ns)