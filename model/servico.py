from model.sql_alchemy import banco

class ServicoModel(banco.Model):
    __tablename__ = 'servico'
    servico_id = banco.Column(banco.Integer, primary_key=True, autoicrement=True)
    nome = banco.Column(banco.String(100), nullable=False)
    valor = banco.Column(banco.Float(precision=2), nullable=False)

    @classmethod
    def find_id(cls, servico_id):
        servico = cls.query.filter_by(servico_id=servico_id).first()
        return None if not servico else servico

    def delete(self):
        banco.session.delete(self)
        banco.session.commit()

    def save_servico(self):
        banco.session.add(self)
        banco.session.commit()

    def update_servico(self, **dados):
        self.nome = dados['nome'] or self.nome
        self.valor = dados['nome'] or self.nome

    def to_dict(self):
        return {
            'servico_id': self.servico_id,
            'nome': self.nome,
            'valor': self.valor
        }
