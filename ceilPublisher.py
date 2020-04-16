import logging, os
from logging.handlers import RotatingFileHandler
from udpSrv.thrSrv import ThrSrv
from Configure import Configuration

def init():
    global exporter_port
    global udpSrv_port
    global kafka_topic
    global kafka_broker
    global kafka_port
    conf = Configuration("/opt/ceilPublisher/publisher.conf")
    udpSrv_port = os.getenv('UDPSRV_PORT', conf.ConfigSectionMap("udp_server")['port'])
    kafka_broker = os.getenv('KAFKA_IP', conf.ConfigSectionMap("kafka")['ip'])
    kafka_port = os.getenv('KAFKA_PORT', conf.ConfigSectionMap("kafka")['port'])
    kafka_topic = os.getenv('KAFKA_TOPIC', conf.ConfigSectionMap("kafka")['topic'])

if __name__ == '__main__':
    logger = logging.getLogger('ceilometerPublisher')
    hdlr = RotatingFileHandler('ceilPublisher.log', maxBytes=1000000, backupCount=1)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)
    logger.setLevel(logging.WARNING)
    logger.setLevel(logging.INFO)
    init()

    logger.info('====================')
    logger.info('Ceilometer Kafka publisher')
    logger.info('UDP server port: ' + udpSrv_port)
    srv = ThrSrv(ip_='0.0.0.0',port_=udpSrv_port,kafka_ip_=kafka_broker, kafka_port_=kafka_port, kafka_topic_=kafka_topic,log_=logger)

