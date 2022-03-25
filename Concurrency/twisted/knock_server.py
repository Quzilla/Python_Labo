from twisted.internet import protocol, reactor

class Knock(protocol.Protocol):
    def dataReceived(self, data):
        print('Client', data)
        message = data.decode('utf-8')
        if message.startswith("Knock knock"):
            response = "Who's a there?".encode('utf-8')
        else: 
            response = "{} Who?".format(message).encode('utf-8')
        print('Server', response)
        self.transport.write(response)
        
class KnockFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Knock()
    
reactor.listenTCP(8000, KnockFactory())
reactor.run()