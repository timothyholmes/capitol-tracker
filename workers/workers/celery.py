from __future__ import absolute_import
from celery import Celery

app = Celery('capitol_tracker_workers',
    broker='amqp://capitol:ct123@localhost/capitol_vhost',
    backend='rpc://',
    include=['workers.tasks']
)