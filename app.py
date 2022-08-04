from flask import jsonify, request
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML

from api import app, db
from api import models
from api.schema import schema


@app.route('/graphql', methods=['GET'])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request
    )

    status_code = 200 if success else 400

    return jsonify(result), status_code
