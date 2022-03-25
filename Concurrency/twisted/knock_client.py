from twisted.internet import reactor, protocol

class KnockClient(protocol.Protocol):
    def connectionMade(self):
        message = 'Knock knock'.encode('utf-8')
        self.transport.write(message)
        
    def dataReceived(self, data):
        message = data.decode('utf-8')
        if message.startswith("Who's a there?"):
            response = 'Disappearing client'.encode('utf-8')
            self.transport.write(response)
        else:
            self.transport.loseConnection()
            reactor.stop()
            
class KnockFatory(protocol.ClientFactory):
    protocol = KnockClient
    
    
def main():
    f = KnockFatory()
    reactor.connectTCP('localhost', 8000, f)
    reactor.run()
    
if __name__ == "__main__":
    main()
