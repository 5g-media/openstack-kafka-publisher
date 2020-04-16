#!/bin/bash

#mv /opt/ceilPublisher/ceilo-pub.service  /etc/systemd/system/ceilo-pub.service & \
#systemctl deamon-reload  & \
#systemctl enable ceilo-pub.service & \
#systemctl start ceilo-pub.service

python3 /opt/ceilPublisher/ceilPublisher.py & \
tail -f /dev/null
