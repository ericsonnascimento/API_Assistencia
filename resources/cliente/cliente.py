from flask_restful import reqparse, Resource
from flask import abort, jsonify
from model.cliente import ClienteModel
from resources import http_status_code as http_codes

post_parser = reqparse.RequestParser()
put_parser = reqparse.RequestParser()

post_parser.add_argument("nome", required=True, help="O atributo nome é requerido")
post_parser.add_argument("telefone", required=True, help="O atributo telefone é requerido")
post_parser.add_argument("email", required=False, help="O atributo email é requerido")

put_parser.add_argument("nome", type=str)
put_parser.add_argument("telefone", type=str)
put_parser.add_argument("email", type=str)

get_all_parser = reqparse.RequestParser()

get_all_parser.add_argument("page", type=int, location="args")
get_all_parser.add_argument("limit", type=int, location="args")


def abort_if_cliente_id_exits(cliente_id):
    if ClienteModel.find_cliente(cliente_id):
        abort(http_codes.CONFLIT_STATUS_CODE, "ID do Cliente já existe!")


class ClientesResource(Resource):
    def get(self):
        pagination_data = get_all_parser.parse_args()
        page = pagination_data["page"] or 1
        limit = pagination_data["limit"] or 10
        pagination = ClienteModel.query.paginate(page, limit, error_out=False)

        data = {
            "clientes": [h.to_dict() for h in pagination.items],
            "pages": pagination.pages,
            "total": pagination.total,
            "page": page,
            "limit": limit,
        }

        if pagination.has_next:
            data["next"] = f"/clientes?page={pagination.next_num}&limit={limit}"

        if pagination.has_prev:
            data["prev"] = f"/clientes?page={pagination.prev_num}&limit={limit}"

        return jsonify(data)

    def post(self):
        dados = post_parser.parse_args()  # Criado fora do contexto da classe
        novo_cliente = ClienteModel(**dados)
        novo_cliente.save_cliente()
        return novo_cliente.to_json(), http_codes.CREATED_STATUS_CODE


class ClienteResource(Resource):
    def get(self, cliente_id):
        cliente = ClienteModel.find_cliente(cliente_id)
        if not cliente:
            abort(
                http_codes.NOT_FOUND_STATUS_CODE, f"Cliente id {cliente_id} não encontrado"
            )

        return cliente.to_json(), http_codes.OK_STATUS_CODE

    def put(self, cliente_id):
        dados = put_parser.parse_args()
        cliente = ClienteModel.find_cliente(cliente_id)

        if not cliente:
            abort(
                http_codes.NOT_FOUND_STATUS_CODE,
                f"Cliente de id {cliente_id} não encontrado",
            )

        cliente.update_cliente(**dados)
        cliente.save_cliente()
        return cliente.to_json(), http_codes.CREATED_STATUS_CODE

    def delete(self, cliente_id):
        cliente = ClienteModel.find_cliente(cliente_id)
        if not cliente:
            abort(
                http_codes.NOT_FOUND_STATUS_CODE, f"Cliente id {cliente_id} não encontrado"
            )
        cliente.delete()
        return "", http_codes.NO_CONTENT_STATUS_CODE
