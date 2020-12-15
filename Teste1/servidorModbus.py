from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep	
from random import uniform

#Create an instance of ModbusServer
server = ModbusServer ("127.0.0.1", 502, no_block=True)

try:
	print("STAR SERVER...")
	server.start()
	print("SERVER ONLINE")
	while True:
		DataBank.set_words(0, [int(uniform(0,100))])
		sleep(0.5)

except:
	print("SHUTDOWN SERVER")
	server.stop()
	print("SERVER IS OFFLINE")

