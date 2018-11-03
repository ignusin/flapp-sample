from flask import Flask

import api


app = Flask(__name__)
app.register_blueprint(api.auth.blueprint, url_prefix='/api')
