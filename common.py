import json

from flask import Response


def result(data, code: int, message: str):
    response_body = {
        'code': code,
        'message': message,
        'data': data
    }
    response_json = json.dumps(response_body, ensure_ascii=False)
    return Response(response_json, mimetype='application/json', status=200)


def ok(message: str):
    return {"data": None, "code": 200, "message": message}


def error(code: int, message: str):
    return {"data": None, "code": code, "message": message}
