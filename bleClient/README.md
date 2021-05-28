# Python Script
This Script needs to run on a computer which has a bluetooth module

## What it Does
It periodically reads From the Bluetooth Server which in this case is the ESP32 and appends values to the CSV. Also it plots a live graph using matplotlib.
* NOTE - Replace (MAC Address of Device) and (UUID of Char) before using

### Includes
* pygatt [link](https://github.com/peplin/pygatt)
* time
* csv
* matplotlib
