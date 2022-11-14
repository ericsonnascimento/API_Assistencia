from flask_restful import Resource, reqparse
from flask import abort
from model.servico import ServicoModel
from resources import http_status_code as http_codes

post_paser = reqparse.RequestParser()
put_parser = reqparse.RequestParser()
get_all_parser = reqparse.RequestParser()

post_paser.add_argument('nome', requered=True, help='O atributo nome é requerido')
post_paser.add_argument('valor', requered=True, help='O atributo valor é requerido')

put_parser.add_argument('nome', type=str)
put_parser.add_argument('valor', type=str)






