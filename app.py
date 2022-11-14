from flask import Flask
from flask_restful import Api
from resources.cliente.cliente import ClientesResource, ClienteResource
from model.sql_alchemy import banco

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///banco.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

api.add_resource(ClientesResource, "/clientes")
api.add_resource(ClienteResource, "/clientes/<string:cliente_id>")

with app.app_context():
    banco.init_app(app)
    banco.create_all()

'''
@app.before_first_request
def criar_banco():
    banco.init_app(app)
    banco.create_all()'''

if __name__ == "__main__":
    app.run(debug=True)
