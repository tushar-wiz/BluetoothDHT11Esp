# Python Script
This Script needs to run on a computer which has a bluetooth module

## What it Does
It periodically reads From the Bluetooth Server which in this case is the ESP32 and appends values to the CSV
* NOTE - Replace (MAC Address of Device) and (UUID of Char) before using

### Includes
* pygatt [link](https://github.com/peplin/pygatt)
* time
* csv

## STILL UNDER CONSTRUCTION
This method is not the best as we can subscribe to a notification service it will be added in the coming days
