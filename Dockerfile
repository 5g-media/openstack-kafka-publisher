FROM python:3.5.5-slim

RUN apt-get update && apt-get -y upgrade && \
apt-get -y install apache2 python3 default-libmysqlclient-dev python3-dev python3-setuptools nano && \
mkdir -p /opt/ceilPublisher

COPY ./ /opt/ceilPublisher
RUN pip3 install -r /opt/ceilPublisher/requirements.txt

ADD ./run.sh /opt/ceilPublisher/run.sh
RUN chmod 0755 /opt/ceilPublisher/run.sh
RUN ls -la /opt/ceilPublisher/*

CMD ["/opt/ceilPublisher/run.sh"]
