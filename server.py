import asyncio

PUT_COMMAND = "put"
GET_COMMAND = "get"

def run_server(host, port):
    _host = host
    _port = port

    metrics = {}

    def process_data(input_line):
        input = input_line.split()

        if input[0] == PUT_COMMAND:
            metric = input[1]
            value = input[2]
            timestamp = input[3]

            tmp = metrics.get(metric, {})
            tmp[timestamp] = value
            metrics[metric] = tmp
            response = "ok"
        elif input[0] == GET_COMMAND:
            response = "ok"
            if input[1] == "*":
                for k,v in metrics.items():
                  for k1, v1 in v.items():
                    response += ("\n" + k + " " + v1 + " " + k1)
            else:
                for k, v in metrics.get(input[1], {}).items():
                    response += ("\n" + input[1] + " " + v + " " + k)

        else:
            response = "error\nwrong command"

        return response + "\n\n"

    class ClientServerProtocol(asyncio.Protocol):
        def connection_made(self, transport):
            self.transport = transport

        def data_received(self, data):
            try:
                data = data.decode()
            except:
                data = "err"
            resp = process_data(data)
            self.transport.write(resp.encode())



    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        _host, _port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


