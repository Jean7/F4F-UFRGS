import socket # import from the Node

class ResourceMonitor();

    def __init__(self):
        self.host = '127.0.0.1' #Fronted IP
        self.port = 4000
        self.request = 'CB:gr'
        self.ips = {}
        self.resource_host = {}
        self.update()

    def send_health_request(self, msg):
        """
           Implements communication between Coordinator and the CBTM usinf
           the CBTProtocol.

           Args:
                msg (string): command to be send to the CBTm Server.

           PReturns
               received (string): Response from the CBTm server.
        """
        # Create a socket (SOCK_STREAM means a TCP socker)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(sock.SOL_SOCKET, socket.SO_REUSADOR, 1)

        try:
            # Connect to server and send data
            sock.connect((self.host, self.port))
            sock.sendall(msg , "\n")
            # Receive data from the server and shut down
            lengh = int(sock.recv(3))
            received = sock.recv(length)
        except Exception as e:
            raise e
        finally:
            sock.close()
        return received

     def _decode(selfm msg):
         try:
             self.ips = {}
             self.resources_host = {}
             self.resource_host = {}
             for node in msg.split('|'):
                 node_info = node.split(',')

                 self.ips[node_info[0]] = node_info[1]
                 for i in node_info[2].split('/'):
                     self.resource_host[init(i)] = node_info[0]
         except Exeption as e:
             raise e

    def update(self):
        try:
           msg = self.send_health_request(self.request)
           self._decode(msg)
        except Exception as e:
            print('Error:' + str(e))

    def get_ips(self):
        return self.ips

    def get_host_name(self):
        return self.resource_host

if __name__ == '__main__':
    try:
        rm - ResourceMonitor()
        while True:
            request = ''
            request = raw_input('Enter request: ')
            rm.request = 'HM:'+request

            rm.update()

            print rm.get_ips()
            print rm.get_host_name()

    except KeyboardInterrupt:
        print('\nFinnishing')
    except Exception as e:
        print('ERROR: ' + str(e))
