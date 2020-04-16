#!/usr/bin/python
from kafka_inf import publisher as kfpub
import socketserver, threading, msgpack


class ThreadedUDPRequestHandler(socketserver.BaseRequestHandler):
    collector = None

    def handle(self):
        data = self.request[0].strip()
        port = self.client_address[1]
        socket = self.request[1]
        client_address = (self.client_address[0])
        cur_thread = threading.current_thread()
        if self.kf_ip:
            msg = msgpack.loads(data, encoding="utf-8")
            # print ("received data: %s" % msg)
            p = kfpub.Publisher(self.kf_ip, self.kf_port, '(1 , 10, 1)')
            res = p.pubJson(topic_=self.kf_topic, msg_=msg)
        else:
            print("Kafka broker doesn't exist")


class ThreadedUDPServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    pass


class ThrSrv(object):

    def __init__(self, ip_, port_, kafka_ip_, kafka_port_, kafka_topic_, log_):
        self.logger = log_
        HOST, PORT = ip_, int(port_)

        class ThreadedUDPRequestHandlerCeil(ThreadedUDPRequestHandler):
            kf_ip = kafka_ip_
            kf_port = kafka_port_
            kf_topic = kafka_topic_
            logger = log_

        server = ThreadedUDPServer((HOST, PORT),
                                   ThreadedUDPRequestHandlerCeil)
        ip, port = server.server_address
        server.serve_forever()
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        self.logger.info('UDP server started in port: ' + str(port_))
        server.shutdown()


if __name__ == "__main__":
    ThrSrv("0.0.0.0", 10000)
