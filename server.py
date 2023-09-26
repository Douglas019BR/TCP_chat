from twisted.internet import protocol, reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import ServerFactory as ServFactory


class Server(protocol.Protocol):
    def __init__(self, clients):
        super(Server, self).__init__()
        self.clients = clients
        print(self.clients)

    def dataReceived(self, data):
        for client in self.clients:
            client.transport.write(data)


class ServerFactory(ServFactory):
    def __init__(self):
        super(ServerFactory, self).__init__()
        self.clients = set()

    def buildProtocol(self, addr):
        server = Server(self.clients)
        self.clients.add(server)
        return server


if __name__ == '__main__':
    endpoint = TCP4ServerEndpoint(
        reactor=reactor, port=12345)
    endpoint.listen(ServerFactory())
    reactor.run()
