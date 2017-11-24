#!/usr/bin/env python3

import connexion
#from .encoder import JSONEncoder
from swagger_server.__init__ import db, CustomJSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = CustomJSONEncoder #JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Talk.Domo interactions'})
    app.run(port=8080)
