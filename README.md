# ReadWidgetValue
Read Widget value from SmartDisplay RS485/Modbus using Python.

# Note
- You may need a USB to RS485 dongle for Modbus communication.
- Port names are different in Linux/Windows/...
- Since the Modbus Slave cannot actively transmit data to the Master, you should regularly (using timer, for example.) read the data actively. 
