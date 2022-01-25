from datetime import date, datetime
from boto3.session import Session

import boto3.ec2
from botocore.config import Config

ec2= boto3.resource(region_name='eu-west-1', service_name='ec2', endpoint_url='http://localhost:4000', aws_access_key_id='aaa',aws_secret_access_key = 'SecertKey')
# ec2 = boto3.resource('ec2', config=my_config)
for i in ec2.instances.all():
    print(i)


# Helper to translate AWS datatime to ISO format
def datetime_converter(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type {} is not serializable".format(type(obj)))
