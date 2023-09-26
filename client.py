from twisted.internet import protocol, reactor
from twisted.internet.protocol import ClientFactory as ClFactory
from twisted.internet.endpoints import TCP4ClientEndpoint


class Client(protocol.Protocol):
    def __init__(self):
        super(Client, self).__init__()
        reactor.callInThread(self.send_data)

    def dataReceived(self, data):
        data = data.decode("utf-8")
        print(data)

    def send_data(self):
        while True:
            data = input(":::")
            self.transport.write(data.encode("utf-8"))


class ClientFactory(ClFactory):
    def buildProtocol(self, addr):
        return Client()


if __name__ == "__main__":
    endpoint = TCP4ClientEndpoint(reactor, "127.0.0.1", 12345)
    endpoint.connect(ClientFactory())
    reactor.run()
