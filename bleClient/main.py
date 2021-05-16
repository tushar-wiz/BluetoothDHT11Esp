import pygatt
import time
import csv


def byteArrToInt(value):
    temp = int.from_bytes(value[:2], byteorder='little', signed=False)
    hum = int.from_bytes(value[2:], byteorder='little', signed=False)
    return [str(temp), str(hum)]

adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(<MAC Address of Device>)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["time","temp", "hum"])
    timeUnit = 0
    while(True): 
        value = device.char_read(<UUID of Char>)
        tempAndHumL = byteArrToInt(value)
        writer.writerow([timeUnit,tempAndHumL[0],tempAndHumL[1]])
        timeUnit += 10    
        time.sleep(10)
