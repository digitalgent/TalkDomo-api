import connexion


def options(id):
    return True, 200, {'Access-Control-Allow-Origin': '*'}
