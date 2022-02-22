from flask import Blueprint
from models.example_model import Example
example_routes = Blueprint('examples', __name__)

@example_routes.route('/')
def example_end_point():
    return {'all example items': [example.to_dict() for example in Example.query.all()]}
