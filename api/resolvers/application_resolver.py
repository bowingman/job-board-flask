from sqlite3 import IntegrityError
from graphql import GraphQLError
from sqlalchemy.exc import IntegrityError

from api.models import Application
from app import db


def create_application_resolver(obj, info, input):
    content, rate, job_id = input.get(
        'content'), input.get('rate'), input.get('job_id')

    try:
        new_application = Application(
            content=content,
            rate=rate,
            job_id=job_id,
            user_id=2,
        )

        db.session.add(new_application)
        db.session.commit()

        return {
            'success': True,
            'application': new_application,
        }
    except IntegrityError as err:
        errorInfo = err.orig.args
        raise GraphQLError(message=errorInfo)
