#!/usr/bin/env python
import threading, logging, time
from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

data = {
    'source': 'openstack',
    'counter_type': 'gauge',
    'project_id': '9f89d937198543e6b38a89d8503142d5',
    'timestamp': '2018-03-21T16:27:45.273549',
    'resource_id': '50a3a175-42a4-42d4-8a10-e0f0cf16c1a0',
    'message_id': 'c97bb281-2d24-11e8-9c8a-150e18cb77dc',
    'user_id': 'cf180fadfb214e12aa90a5ccafe10383',
    'message_signature': 'dd6c21aa535dbc188e9991ea24a889203ca3eb52c5297a04e1bdef09c9905c7b',
    'resource_metadata': {
        'os_type': 'hvm',
        'display_name': 'test',
        'image_ref': '6fadef71-6608-4ba2-9cee-671a1aa5edba',
        'task_state': '',
        'instance_host': 'pike2',
        'root_gb': 1,
        'state': 'running',
        'name': 'instance-00000006',
        'memory_mb': 512,
        'flavor': {
            'swap': 0,
            'disk': 1,
            'ram': 512,
            'vcpus': 1,
            'ephemeral': 0,
            'name': 'm1.tiny',
            'id': '76949218-7a4f-4e7e-8269-f4e24c2832ab'
        },
        'architecture': 'x86_64',
        'vcpus': 1,
        'instance_id': '50a3a175-42a4-42d4-8a10-e0f0cf16c1a0',
        'disk_gb': 1,
        'instance_type': 'm1.tiny',
        'ephemeral_gb': 0,
        'status': 'active',
        'image_ref_url': None,
        'cpu_number': 1,
        'image': {
            'id': '6fadef71-6608-4ba2-9cee-671a1aa5edba'
        },
        'host': '30b3a202bf71d8651cf49f4aa9232f79e029f87d47c081163fca9d12'
    },
    'counter_name': 'cpu_util',
    'counter_unit': '%',
    'monotonic_time': None,
    'counter_volume': 2.0722654293387963
}


class Publisher(object):
    def __init__(self, borker_ip_, port_, api_ver_):
        self.borker_url = borker_ip_ + ':' + port_
        self.api_verision = api_ver_

    def pubJson(self, msg_, topic_):
        producer = KafkaProducer(bootstrap_servers=self.borker_url, api_version=(1, 1, 0),
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        record_metadata = None
        t = producer.send(topic_, msg_)
        # Set as timeout10 sec for 'synchronous' sends
        try:
            record_metadata = t.get(timeout=10)
        except KafkaError as ex:
            # Decide what to do if produce request failed...
            pass


if __name__ == "__main__":

    while (1):
        print(time.time())
        p = Publisher('192.168.1.107', '9092', '(1 , 10, 1)')
        p.pubJson(topic_='monitoring1', msg_=data)
        time.sleep(0.05)
