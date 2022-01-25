from __future__ import annotations
from datetime import datetime

class Instance:
    ID: str
    launch_time: datetime
    
    def __init__(self, id: str, date : datetime):
        self.ID = id
        self.launch_time = date
    @staticmethod
    def ec2_to_instance(ec2_instance  ) -> Instance:
        return Instance(ec2_instance.instance_id, ec2_instance.launch_time)
    
    def launch_time_sort(i):
        return i.launch_time
    