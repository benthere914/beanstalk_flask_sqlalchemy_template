from flask import Flask
from config import Config
from models import db
from routes.example import example_routes
# import any blueprints from routes folder

application = Flask(__name__)
application.config.from_object(Config)
application.register_blueprint(example_routes, url_prefix='/examples')
# register blueprints to application

db.init_app(application)
if __name__ == "__main__":
    application.debug = True
    application.run()
