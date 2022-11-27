from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config

permiso_blueprints = Blueprint('permiso_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-resultados') + "/permiso"


@permiso_blueprints.route("/permiso", methods=['GET'])
def get_all_permisos() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@permiso_blueprints.route("/permiso/<string:id_>", methods=['GET'])
def get_permiso_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@permiso_blueprints.route("/permiso/insert", methods=['POST'])
def insert_permiso() -> dict:
    permiso = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=permiso)
    return response.json()


@permiso_blueprints.route("/permiso/update/<string:id_>", methods=['PUT'])
def update_permiso(id_: str) -> dict:
    permiso = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=permiso)
    return response.json()


@permiso_blueprints.route("permiso/delete/<string:id_>", methods=['DELETE'])
def delete_permiso(id_: str) -> dict:
    permiso = request.get_json()
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS, json=permiso)
    return response.json()

