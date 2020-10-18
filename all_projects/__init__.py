from flask import Flask
app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = 'mysecretkey'
from all_projects.core.views import core
app.register_blueprint(core)
