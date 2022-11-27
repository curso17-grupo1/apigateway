from flask import Blueprint, request
import requests

from utils import HEADERS, load_file_config

user_blueprints = Blueprint('user_blueprints', __name__)
data_config = load_file_config()
url_base = data_config.get('url-backend-resultados') + "/user"


@user_blueprints.route("/user", methods=['GET'])
def get_all_users() -> dict:
    url = url_base + "/all"
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/<string:id_>", methods=['GET'])
def get_user_by_id(id_: str) -> dict:
    url = f'{url_base}/{id_}'
    response = requests.get(url, headers=HEADERS)
    return response.json()


@user_blueprints.route("/user/insert", methods=['POST'])
def insert_user() -> dict:
    user = request.get_json()
    url = f'{url_base}/insert'
    response = requests.post(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("/user/update/<string:id_>", methods=['PUT'])
def update_user(id_: str) -> dict:
    user = request.get_json()
    url = f'{url_base}/update/{id_}'
    response = requests.patch(url, headers=HEADERS, json=user)
    return response.json()


@user_blueprints.route("user/delete/<string:id_>", methods=['DELETE'])
def delete_user(id_: str) -> dict:
    user = request.get_json()
    url = f'{url_base}/delete/{id_}'
    response = requests.delete(url, headers=HEADERS, json=user)
    return response.json()

