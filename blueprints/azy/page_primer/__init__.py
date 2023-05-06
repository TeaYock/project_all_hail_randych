# page1.py
from flask import Flask
app = Flask(__name__)

# blueprints/azy/page_primer/__ini__.py
from flask import Blueprint

blueprint = Blueprint('page', __name__, url_prefix='/azy')

@blueprint.route('/page_primer')
def welcome_text():
    return '<h1>Мне кажется, или я реально уже в браузере?!</h1>'

@app.route('/page_primer')
def welcome_text():
    return '<h1>Мне кажется, или я реально уже в браузере?!</h1>'

if __name__ == "__main__":
    app.run(debug=True)