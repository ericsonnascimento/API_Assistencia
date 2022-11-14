from model.sql_alchemy import banco
from sqlalchemy import func
from flask import jsonify
import datetime
import json

class ClienteModel(banco.Model):
    __tablename__ = "cliente"  # Mapeamento da tabela
    cliente_id = banco.Column(banco.Integer, primary_key=True, autoincrement=True)
    nome = banco.Column(banco.String(100), nullable=False)
    telefone = banco.Column(banco.String(40), nullable=False)
    email = banco.Column(banco.String(100), nullable=True)
    criado_em = banco.Column(banco.DateTime(timezone=True), server_default=func.now())
    atualizado_em = banco.Column(banco.DateTime(timezone=True), onupdate=func.now())

    @classmethod
    def find_cliente(cls, cliente_id):
        cliente = cls.query.filter_by(cliente_id=cliente_id).first()
        return None if not cliente else cliente

    def update_cliente(self, **dados):
        self.nome = dados["nome"] or self.nome
        self.telefone = dados["telefone"] or self.telefone
        self.email = dados["email"] or self.email

    def delete(self):
        banco.session.delete(self)
        banco.session.commit()

    def save_cliente(self):
        banco.session.add(self)
        banco.session.commit()

    def to_dict(self):
        return {
            "cliente_id": self.cliente_id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "criado_em": self.criado_em,
            "atualizado_em": self.atualizado_em
        }

    def to_json(self):
        to_dict = {
            "cliente_id": self.cliente_id,
            "nome": self.nome,
            "email": self.email,
            "telefone": self.telefone,
            "criado_em": self.criado_em,
            "atualizado_em": self.atualizado_em
        }
        return jsonify(to_dict)

'''def convert_datetime(object_datetime):
            if isinstance(object_datetime, (datetime.date, datetime.datetime)):
                return object_datetime.strftime('%d/%m/%Y %H:%M:%S')

        criado_em_json = json.dumps(self.criado_em, default=convert_datetime)
        atualizado_em_json = json.dumps(self.atualizado_em, default=convert_datetime)'''