from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep

#Criando uma instancia de ModbusServer
server = ModbusServer("localHost", 502, no_block=True)

try:
    print("Start server ...")
    server.start()
    print("Server is online")
    state = [0]
    while True:
        if state != DataBank.get_words(1):
            state = DataBank.get_words(1)
            print("Value has changed to " +str(state))
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offiline")