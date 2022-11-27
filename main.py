from datetime import timedelta

import requests as rq
from flask import Flask, request
from flask_cors import CORS
from flask_jwt_extended import (JWTManager, create_access_token, get_jwt_identity, verify_jwt_in_request)
from waitress import serve

import utils

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "mision_tic"
cors = CORS(app)
jwt = JWTManager(app)


@app.before_request
def before_request_callback():
    endpoint = utils.clear_url(request.path)
    exclude_routes = ['/', '/login']
    if exclude_routes.__contains__(request.path):
        pass
    elif verify_jwt_in_request():
        user = get_jwt_identity()
        if user.get('rol'):
            has_grant = utils.validate_grant((endpoint, request.method, user['rol'].get('idRol')))
            if not has_grant:
                return {"message": "Acceso denegado por permiso"}, 401
        else:
            return {"message": "Permisos denegados por rol"}, 401


@app.route("/", methods=["GET"])
def home() -> dict:
    response = {"message": "Bienvenido al API Gateway de ciclo IV..."}
    return response


@app.route("/login", methods=["POST"])
def login() -> dict[str, str]:
    user = request.get_json()
    url = data_config.get("url-backend-security") + "/user/login"
    response = rq.post(url, headers=utils.HEADERS, json=user)
    if response.status_code == 200:
        user_logged = response.json()
        del user_logged['rol']['permisos']
        expires = timedelta(days=1)
        access_token = create_access_token(identity=user_logged, expires_delta=expires)
        return {"token": access_token, "user_id": user_logged.get('idUser')}, 200
    else:
        return {"message": 'Acceso denegado'}, 401


if __name__ == "__main__":
    data_config = utils.load_file_config()
    print(f'API Gateway Server corriendo... http://{data_config.get("url-api-gateway")}' +
          f':{data_config.get("port")}')

    serve(app, host=data_config.get("url-api-gateway"), port=data_config.get("port"))
