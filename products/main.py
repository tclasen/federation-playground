#!/usr/bin/env python3

from ariadne import QueryType, graphql_sync, load_schema_from_path
from ariadne.constants import PLAYGROUND_HTML
from ariadne.contrib.federation import (FederatedObjectType,
                                        make_federated_schema)
from flask import Flask, jsonify, request

app = Flask(__name__)

type_defs = load_schema_from_path("schema.graphql")
query = QueryType()
product = FederatedObjectType("Product")
schema = make_federated_schema(type_defs, [query, product])


@app.route("/", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code


@query.field("topProducts")
def resolve_top_products(*_, first):
    return products[:first]


@product.reference_resolver
def resolve_product_reference(_, _info, representation):
    return get_product_by_upc(representation["upc"])


products = [
    {"upc": "1", "name": "Table", "price": 899, "weight": 100},
    {"upc": "2", "name": "Couch", "price": 1299, "weight": 1000},
    {"upc": "3", "name": "Chair", "price": 54, "weight": 50},
]


def get_product_by_upc(upc: str):
    return next((product for product in products if product["upc"] == upc), None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
