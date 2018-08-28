import socket
import time

class ClientError(Exception):
    pass

class Client:

    def __init__(self, host, port, timeout = None):
        self.host = host
        self.port = port
        self.timeout = timeout if not None else 0


    def put(self, metric_name, metric_value, timestamp = str(int(time.time()))):
        prepared_metric = "put {} {} {}\n".format(metric_name, metric_value, timestamp)
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(prepared_metric.encode("utf8"))
                data = sock.recv(1024)
                if data != b'ok\n\n':
                    raise ClientError
            except:
                raise ClientError

    def get(self, metric):
        message = ("get {}\n".format(metric)).encode("utf8")
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(message)
                while True:
                    try:
                        data = sock.recv(1024*1024).decode("utf8")
                        if data == 'ok\n\n':
                            return {}
                        b = {}
                        for i in data.split('\n')[1:-2]:
                            c = i.split()
                            temp = b.get(c[0], [])
                            temp.append((int(c[2]), float(c[1])))
                            b[c[0]] = temp
                        return b
                    except:
                        raise ClientError

            except:
                raise ClientError

