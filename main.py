# main.py
from flask import Flask
from blueprints.azy.page_primer import blueprint as page_primer
from blueprints.azy.primery_api import blueprint as primery_api
from blueprints.final_servis import blueprint as final_servis

app = Flask(__name__)
app.register_blueprint(page_primer)
app.register_blueprint(primery_api)
app.register_blueprint(final_servis)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run(debug=True)