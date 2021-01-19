import rpyc
from constRPYC import * #-

class Client:
  conn_serverDirectory = rpyc.connect(SERVER, PORT)
  nameServerDirectory = conn_directory.root.exposed_lookup("DBList")
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  conn.root.exposed_append(2)       # Call an exposed operation,
  conn.root.exposed_append(4)       # and append two elements
  print conn.root.exposed_value()   # Print the result
