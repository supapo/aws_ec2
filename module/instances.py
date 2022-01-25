from __future__ import annotations

from typing import List
import boto3.ec2
import json
from module.instance import Instance
class Instances:
    @staticmethod
    def get_instaces() -> List[Instance]:
        instances: List[Instance] = {}
        return instances

    @staticmethod
    def get_ec2_region_client(region: str): #TODO what is the return type?
        return boto3.resource(region_name=region, service_name='ec2', endpoint_url='http://localhost:4000', aws_access_key_id='aaa',aws_secret_access_key = 'SecertKey')
    
    @staticmethod
    def get_instaces_from_aws(region: str) -> List[Instance]:
        instances: List[Instance] = []
        ec2 = Instances.get_ec2_region_client(region)
        #TODO try & catch
        for i in ec2.instances.all():
            instance = Instance.ec2_to_instance(i)
            instances.append(instance)
        return instances


    @staticmethod
    def load_instaces() :
       # TODO take file name from config
        regions : List[str]
        with open("regions.txt", encoding="utf8", errors='ignore') as file:
            file_content = file.read()  
            regions = file_content.split(",")
            # TODO get from config
        for region in regions:
            region = region.strip()
            instances: List[Instance] = Instances.get_instaces_from_aws(region)
            instances.sort(key=Instance.launch_time_sort)
            with open(f"coverage/{region}.txt", "w") as region_file:
                region_file.write(json.dumps([ob.__dict__ for ob in instances],default=str))
