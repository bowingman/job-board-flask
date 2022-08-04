from tkinter import N
from graphql import GraphQLError
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash

from api.models import User
from app import db


def create_user_resolver(obj, info, input):
    name, password, role, title, description = input.get('name'), input.get(
        'password'), input.get('role'), input.get('title'), input.get('description')

    user = User.query.filter_by(name=name).first()

    if user:
        return {
            'success': False,
            'errors': [f'{user.name} is already exists']
        }

    hashed_password = generate_password_hash(password)

    try:

        new_user = User(
            name=name,
            password=hashed_password,
            role=role,
            title=title,
            description=description,
            rate=0,
            approved=False,
        )

        db.session.add(new_user)
        db.session.commit()

        return {
            'success': True,
            'user': new_user,
        }
    except IntegrityError as err:
        errorInfo = err.orig.args
        raise GraphQLError(message=errorInfo)


def get_users_resolver(obj, info):
    try:
        users = User.query.all()

        return {
            'success': True,
            'users': users
        }

    except Exception as err:
        errorInfo = err.orig.args
        raise GraphQLError(message=errorInfo)


def get_user_resolver(obj, info, user_id):
    try:
        user = User.query.filter_by(id=user_id).first()

        if user is None:
            return {
                'success': False,
                'errors': [f'Not found {user.id}']
            }

        return {
            'success': True,
            'user': user,
        }
    except Exception as err:
        errorInfo = err.orig.args
        raise GraphQLError(message=errorInfo)
