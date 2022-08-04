from graphql import GraphQLError
from api import db
from api.models import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from graphql import GraphQLError


def login_resolver(obj, info, input):
    return {
        'success': False,
        'token': '123',
        'errors': ['erorr']
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
