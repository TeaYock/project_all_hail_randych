from flask import Flask
from api import blueprint as api
from final_service import blueprint as final_servis

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(final_servis)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

if __name__ == "__main__":
    app.run(debug=True)