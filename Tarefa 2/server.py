import rpyc
from constRPYC import * #-
from rpyc.utils.server import ForkingServer

class DBList(rpyc.Service):
  value = []

  def exposed_append(self, data):
    self.value = self.value + [data]
    return self.value

  def exposed_value(self):
    return self.value

if __name__ == "__main__":
    server = ForkingServer(DBList, port = 8765)
    conn_serverDirectory = rpyc.connect(SERVER, PORT)
    
    my_ip_address = socket.gethostbyname(socket.gethostname())
    conn_serverDirectory.root.exposed_register("DBList", my_ip_address, 8765)
    server.start()

