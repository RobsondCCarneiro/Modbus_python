from pyModbusTCP.client import ModbusClient
import time

#TCP auto connect on first Modbus Request
c = ModbusClient(host="localhost", port=502, auto_open=True)

#TCP auto connect on Modbus Request, close after it
c = ModbusClient(host="127.0.0.1", auto_open=True, auto_close=True)
c = ModbusClient()
c.host("localhost")
c.port(502)

cont = 0
tanque = c.write_single_register(2,0)
valvula = c.write_single_register(3,0)
LED = c.write_single_register(1,0)

while True:
	# managing TCP sessions with call to c.open()/c.close()
	c.open()
	led = c.read_holding_registers(1)
	tanque_valor = c.read_holding_registers(2)

	if led[0] == 1:
		cont = cont+1
		c.write_single_register(2,cont)
		tanque_valor = c.read_holding_registers(2)

	if tanque_valor[0]==10:
		c.write_single_register(1,0)
	if led[0]==0:
		c.write_single_register(3,1)
		cont=cont-1
		c.write_single_register(2,cont)
		tanque_valor = c.read_holding_registers(2)
		if tanque_valor[0]==0:
			c.write_single_register(3,0)



	if led:
		print("valor do LED: ")
		print(led)
		print("valor do tanque: ")
		print(tanque_valor)
	else:
		print("read error")
	time.sleep(2)