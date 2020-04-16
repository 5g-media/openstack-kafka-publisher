#!/bin/bash

su - stack
cd /opt/stack/
mkdir os_images
cd os_images/
wget http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img
wget http://cloud-images.ubuntu.com/xenial/current/xenial-server-cloudimg-amd64-disk1.img

source /opt/stack/devstack/openrc

openstack image create --file="/opt/stack/os_images/cirros-0.3.4-x86_64-disk.img" --container-format=bare --disk-format=qcow2 --public cirros034
openstack image create --file="/opt/stack/os_images/xenial-server-cloudimg-amd64-disk1.img" --container-format=bare --disk-format=qcow2 --public ubuntu16.04