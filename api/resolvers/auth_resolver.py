import jwt
from graphql import GraphQLError
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from graphql import GraphQLError

from api import db
from api.models import User
from api.helpers.encode_jwt import encode_jwt


def login_resolver(obj, info, input):
    name, password = input.get('name'), input.get('password')

    user = User.query.filter_by(name=name).first()

    if user is None:
        return {
            'success': False,
            'errors': [f"They are not user {name}."]
        }

    valid_password = check_password_hash(user.password, password)

    if not valid_password:
        return {
            'success': False,
            'errors': ["Wrong Password"]
        }

    try:
        token = encode_jwt(user.id, life=3600)

        return {
            'success': True,
            'token': token,
            'user': user,
        }

    except Exception as err:
        return {
            'success': False,
            'errors': ['123'],
        }


def register_resolver(obj, info, input):
    clean_input = {
        'name': input.get('name'),
        'password': input.get('password'),
        'role': input.get('role'),
        'title': input.get('title'),
        'description': input.get('description'),
    }

    try:
        hashed_password = generate_password_hash(clean_input['password'])
        user = User(
            name=clean_input['name'],
            password=hashed_password,
            role=clean_input['role'],
            title=clean_input['title'],
            description=clean_input['description'],
            rate=0,
            approved=False,
        )

        db.session.add(user)
        db.session.commit()

        return {
            'success': True,
            'user': user
        }

    except IntegrityError as err:
        errorInfo = err.orig.args
        raise GraphQLError(message=errorInfo)


def login_by_token_resolver(obj, info, token):
    decoded_data = jwt.decode(token, "secret", algorithms=["HS256"])

    if decoded_data is None:
        return {
            'success': False,
            'errors': ['Wrong Token!']
        }

    user = User.query.filter_by(id=decoded_data['sub']).first()

    if user is None:
        return {
            'success': False,
            'errors': ['Wrong Token!']
        }

    return {
        'success': True,
        'user': user,
    }
