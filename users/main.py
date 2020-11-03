#!/usr/bin/env python3

import uvicorn
from ariadne import QueryType, load_schema_from_path
from ariadne.asgi import GraphQL
from ariadne.contrib.federation import (FederatedObjectType,
                                        make_federated_schema)
from fastapi import FastAPI

app = FastAPI()

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()
user = FederatedObjectType("User")
schema = make_federated_schema(type_defs, [query, user])
graphql_app = GraphQL(schema)


@query.field("me")
def resolve_me(_, info):
    return users[0]


@user.reference_resolver
def resolve_user_reference(_, _info, representation):
    return get_user_by_email(representation.get("email"))


users = [
    {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com"},
    {"id": 2, "name": "Alan Turing", "email": "alan@example.com"},
]


def get_user_by_email(email: str):
    return next((user for user in users if user["email"] == email), None)


app.add_route("/", graphql_app)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True, log_level="debug")
