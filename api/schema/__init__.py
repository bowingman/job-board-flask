from ariadne import load_schema_from_path, make_executable_schema, ObjectType

from api.resolvers import login_resolver, register_resolver, login_by_token_resolver

query = ObjectType("Query")
query.set_field('loginByToken', login_by_token_resolver)

mutation = ObjectType("Mutation")
mutation.set_field('login', login_resolver)
mutation.set_field('register', register_resolver)

type_defs = load_schema_from_path("api/schema/schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)
