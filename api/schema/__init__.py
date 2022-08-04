from ariadne import load_schema_from_path, make_executable_schema, ObjectType

from api.resolvers import login_resolver, register_resolver

query = ObjectType("Query")

query = ObjectType("Mutation")
query.set_field('login', login_resolver)
query.set_field('register', register_resolver)

type_defs = load_schema_from_path("api/schema/schema.graphql")
schema = make_executable_schema(type_defs, query)
