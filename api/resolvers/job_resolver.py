from datetime import date
from graphql import GraphQLError
from sqlalchemy.exc import IntegrityError

from api.models import Job
from app import db


validator_schema = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "description": {"type": "string"},
    },
    "required": ["email"]
}


def create_job_resolver(obj, info, input):

    title, description, company_scale, company_tips, job_info = input.get(
        'title'), input.get('description'), input.get('company_scale'), input.get('company_tips'), input.get('job_info')
    try:
        job = Job(
            title=title,
            description=description,
            company_scale=company_scale,
            company_tips=company_tips,
            job_info=job_info,
            user_id=1,
            rate=0,
            created_at=date.today(),
            status="ready",
            approved=False,
        )

        db.session.add(job)
        db.session.commit()

        return {
            'success': True,
            'job': job
        }

    except IntegrityError as err:
        errorInfo = err.orig.args
        raise GraphQLError(message=errorInfo)
