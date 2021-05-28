import pygatt
import csv
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import collections

def my_function(i):
    global timeCount
    global threshold
    callValue()
    ax.cla()
    ax1.cla()
    
    ax.plot(timeCount,tempQ)
    ax.text(timeCount[-1]-10, tempQ[-1]+2, "{}\u2103".format(tempQ[-1]))
    ax.set(xlim = (timeCount[0],timeCount[-1]),ylim=(0,100),xlabel='Time', ylabel='Temperature')


    ax1.plot(timeCount, humidityQ)
    ax1.text(timeCount[-1]-10, humidityQ[-1]+2, "{}%".format(humidityQ[-1]))
    ax1.set(xlim = (timeCount[0],timeCount[-1]), ylim=(0,100),xlabel='Time', ylabel='Humidity')

    threshold += 1
    if threshold > 9:
        timeCount = [i+10 for i in timeCount]
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timeCount[-1],tempQ[-1],humidityQ[-1]])
    else:
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timeCount[threshold],tempQ[-1],humidityQ[-1]])

def callValue():
    value = device.char_read(<UUID of Char>)
    temp = int.from_bytes(value[:2], byteorder='little', signed=False)
    hum = int.from_bytes(value[2:], byteorder='little', signed=False)
    tempQ.popleft()
    tempQ.append(temp)
    humidityQ.popleft()
    humidityQ.append(hum)

adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(<MAC Address of Device>)

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["time","temp", "hum"])

threshold = 0
timeCount = [i*10 for i in range(10)]
    
tempQ = collections.deque(np.zeros(10))
humidityQ = collections.deque(np.zeros(10))

fig = plt.figure(figsize=(12,6), facecolor='#DEDEDE')

ax = plt.subplot(121)
ax1 = plt.subplot(122)

ax.set_facecolor('#DEDEDE')
ax1.set_facecolor('#DEDEDE')

ani = FuncAnimation(fig, my_function, interval = 10000)

plt.show()
