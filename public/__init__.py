# load Flask
import os

# load Flask
from flask import Flask
from flask_restx import Api

from controllers import Controllers

app = Flask('public')
api = Api()
api.init_app(app)

controllers = Controllers()