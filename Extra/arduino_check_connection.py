import serial.tools.list_ports
import time
import threading

myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
print(myports)

arduino_port = [port for port in myports if 'COM6' in port ][0]

def check_presence(correct_port,interval=0.1):
    while True:
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        if arduino_port not in myports:
            print('Arduino has been disconnected !')
            break
        time.sleep(interval)

port_controller = threading.Thread(target=check_presence, args=(arduino_port, 0.1))
port_controller.setDaemon(True)
port_controller.start()