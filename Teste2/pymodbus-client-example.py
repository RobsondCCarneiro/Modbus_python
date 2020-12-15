# importacao de bibliotecas
import time
from pyModbusTCP.client import ModbusClient

# define o cliente
c = ModbusClient()

# ip/porta do servidor modbus (para se conectar)
c.host("localhost")
c.port(502)

while True:
    # para abrir a conexao TCP com o servidor
    if not c.is_open():
        if not c.open():
            print("Impossivel se conectar")
        else:
            print("conectado")

    # se a conexao estabelecida, prossegue
    if c.is_open():

        # iniciando as "variaveis" do Scada
        c.write_single_register(0,0) #nivel do tanque
        c.write_single_coil(0,0) #abrir_valvula
        c.write_single_coil(1,0) #valvula
        c.write_single_coil(2,0) #alarme
        time.sleep(1)

        # lendo se tem que abrir a valvula
        start = c.read_coils(0)
        i = 0

        # se for para abrir a valvula:
        if start[0]:
            c.write_single_coil(1,1)
            print("valvula aberta")

            while(1):
                print("nivel = {}".format(i))
                c.write_single_register(0,i)

                # aumentando nivel
                i = i + 1
                time.sleep(1)

                # lendo se tem que continuar enchendo
                goahead = c.read_coils(0)
                nivel = c.read_input_registers(0)

                # se o nivel for maior que 9, ativa o alarme mas continua enchendo ate comando esvaziar
                if(nivel[0]>9):
                    c.write_single_coil(2,1)
                    print("ALARME!!!")
                
                # se for pra continuar:
                if goahead[0]:
                    print("enchendo..")
                    continue
                # se for para esvaziar
                else:
                    print("esvazeando")
                    break