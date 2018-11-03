from flask import Blueprint

from core import context, objects, validators
from flapp.di import uses
from flapp.validation.validator import validated
from flapp.web import rest
from flapp.web.auth import make_auth_token


@uses(context.user_dao)
@rest
def authorize(user_dao, data):
    user = user_dao.find_by_credentials(data['username'], data['password'])
    if not user:
        return None
    
    return { 'token': make_auth_token(user.id) }


@uses(context.user_service)
@rest
@validated(validators.register_dto_validator)
def register(user_service, data):
    user = objects.User()
    user.username = data['username']
    user.password = data['password']

    user_service.add(user)



blueprint = Blueprint('auth', __name__)
blueprint.add_url_rule('/auth/sign-in', view_func=authorize, methods=['POST'])
blueprint.add_url_rule('/auth/register', view_func=register, methods=['POST'])
