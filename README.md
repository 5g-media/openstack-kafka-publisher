# `Openstack-kafka-publisher` service

## Introduction

The role of the `Openstack-kafka-publisher` service is to receive monitoring data of the running network services (and the running VNFs) deployed in OpenStack NFVI through the Ceilometer service (OpenStack) over UDP protocol and forward them in the publish/subscribe broker of 5G-MEDIA Service Virtualization Platform.

Actually, this service feeds the [MAPE](https://github.com/5g-media/mape) with monitoring data.

Apart from the instructions relevent to deployment of this publisher, indicative configuration of the Ceilometer service is provided under the `ceilometer` folder.


## Requirements
- The docker engine has been installed
- The Ceilometer can access this service (check firewall)


## Configuration

Inspect the `publisher.conf` file and modify it before the build of the image. 
The default settings are the following:
- udp_server
   + port: 10000 
- kafka
   + ip: 192.168.1.107
   + port: 9092
   + topic: nfvi.example.openstack
   
You need to configure the ceilometer properly in order to push the data over UDP in this service.

Modify the ceilometer.conf and pipeline.conf in the `/etc/ceilometer` path. 
Take a look in the files that are included in the ceilometer folder.


## Installation/Deployment

Before the duild of the docker image, take a look in the configuration section.

**1. Build teh docker image**
```bash
# clone code from  repository
cd Openstack-kafka-publisher
docker build -t ceilometer_kafka_publisher .
```

**2. Instaintiate the service as docker container**
```bash
docker run -d --name ceilometer_kafka_publisher -p 10000:10000/udp ceilometer_kafka_publisher
```

## Usage

 **Check the logs**
```bash
docker exec -it ceilometer_kafka_publisher bash 
# inside container
cd /opt/ceilPublisher
tail -f /ceilPublisher.log  
```

The expected response should look like:
```txt
2018-05-14 11:57:39,326 INFO ====================
2018-05-14 11:57:39,326 INFO Ceilometer Kafka publisher
2018-05-14 11:57:39,326 INFO UDP server port: 10000
...
```


## Authors
- Singular Logic

## Contributors
 - Contact with Authors
 
## Acknowledgements
This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 761699. The dissemination of results herein reflects only the author’s view and the European Commission is not responsible for any use that may be made of the information it contains.

## License
[Apache 2.0](LICENSE.md)
