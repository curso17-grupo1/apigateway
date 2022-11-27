from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config

candidato_blueprints = Blueprint('candidato_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-resultados') + "/candidato"


@candidato_blueprints.route("/candidato", methods=['GET'])
def get_all_candidatos() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@candidato_blueprints.route("/candidato/<string:id_>", methods=['GET'])
def get_candidato_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@candidato_blueprints.route("/candidato/insert", methods=['POST'])
def insert_candidato() -> dict:
    candidato = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=candidato)
    return response.json()


@candidato_blueprints.route("/candidato/update/<string:id_>", methods=['PUT'])
def update_candidato(id_: str) -> dict:
    candidato = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=candidato)
    return response.json()


@candidato_blueprints.route("candidato/delete/<string:id_>", methods=['DELETE'])
def delete_candidato(id_: str) -> dict:
    candidato = request.get_json()
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS, json=candidato)
    return response.json()

