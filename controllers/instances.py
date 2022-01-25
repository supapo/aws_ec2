from ast import List
import json
import os
from public import app, api
from flask_restx import Api, Resource, fields
from werkzeug.exceptions import NotFound
from module.instance import Instance
ns = api.namespace('instances', description='TODO instances')

instance_model = api.model('Instace', {
    'ID': fields.String,
    'launch_time': fields.DateTime
})

@ns.route('/<region>')
class Instances(Resource):
    @ns.response(200, 'Success', instance_model, envelope='Instances', as_list=True)
    def get(self, region):
            base_dir = os.path.dirname(app.instance_path)
            try:
                with open(f"{base_dir}/coverage/{region}.txt", encoding="utf8", errors='ignore') as file:
                    return json.load(file)
            except IOError: 
                raise NotFound(f"region '{region}' not found")