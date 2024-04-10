
def result(data, code: int, message: str):
    return {"data": data, "code": code, "message": message}


def ok(message: str):
    return {"data": None, "code": 200, "message": message}


def error(code: int, message: str):
    return {"data": None, "code": code, "message": message}
