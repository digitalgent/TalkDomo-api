#!/usr/bin/env python3
import os, sys
#from daemonize import Daemonize
import connexion
from flask_cors import CORS
#from .encoder import JSONEncoder
from swagger_server.__init__ import db, CustomJSONEncoder

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = CustomJSONEncoder #JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Talk.Domo interactions'})
    # add CORS support
    CORS(app.app)
    app.run(port=8080)
    print("App running")

if __name__ == '__main__':
    # name='swagger_server'
    # pidfile='/tmp/%s' % name
    # daemon = Daemonize(app=name,pid=pidfile, action=main)
    # print("Daemon starting as %s" % name)
    # daemon.start()
    main()
