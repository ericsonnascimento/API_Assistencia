import requests
from model.cliente import ClienteModel

API_URL = "http://127.0.0.1:5000/"
ENDPOINT_GET = API_URL + "clientes"


def get_all(page=None, limit=None):
    if not page or not limit:
        URL = ENDPOINT_GET
    else:
        URL = f"{ENDPOINT_GET}?page={page}&limit={limit}"

    dict_reponse = requests.get(URL).json()
    dict_reponse["clientes"] = [ClienteModel(**h) for h in dict_reponse["clientes"]]
    return dict_reponse


def get(cliente_id):
    URL = ENDPOINT_GET + "/" + str(cliente_id)
    dict_reponse = requests.get(URL).json()
    return ClienteModel(**dict_reponse)


def put(cliente):
    URL = ENDPOINT_GET + "/" + str(cliente.cliente_id)
    requests.put(URL, data=cliente.to_dict())


def post(cliente):
    requests.post(ENDPOINT_GET, data=cliente.to_dict())


def delete(cliente_id):
    URL = ENDPOINT_GET + "/" + str(cliente_id)
    requests.delete(URL)
