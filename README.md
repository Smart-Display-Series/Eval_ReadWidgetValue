# ReadWidgetValue
Show how to read value from RS485/Modbus SmartDisplay using Python.

## Feature
- Use the library [minimalmodbus](https://minimalmodbus.readthedocs.io/en/stable/index.html "minimalmodbus") and refer to its sample programs.
- Tested on Windows and Raspberry Pi.

## Note
- You may need a USB to RS485 dongle for Modbus communication.
- The com port name is different in different operating systems.
- Since the Modbus Slave cannot actively transmit data to the Master, you should regularly (using timer, for example.) read the data actively. 

## Result
### Windows
```console
D:\Git\PythonProject\ReadWidgetValue>python ReadWidgetValue.py -DCOM22
#####################################################################################
## Test with SmartDisplay                                                          ##
## Minimalmodbus version:     2.0.1                                                ##
##                                                                                 ##
## Platform:                  win32                                                ##
## Python version:            3.8.10                                               ##
## Modbus mode:               rtu                                                  ##
## Baudrate (-b):             115200                                               ##
## Port name (-D):            COM22                                                ##
## Slave address:             123                                                  ##
## Timeout:                   0.3                                                  ##
## Full file path:            D:\Git\PythonProject\ReadWidgetValue\ReadWidgetValue.py##
#####################################################################################

#####################################################################################
## Current values                                                                  ##
##                                                                                 ##
## Widget 0 Value:            1                                                    ##
## Widget 1 Value:            0                                                    ##
## Widget 2 Value:            0                                                    ##
## Widget 3 Value:            28                                                   ##
## Widget 4 Value:            0                                                    ##
## Widget 5 Value:            0                                                    ##
## Widget 6 Value:            0                                                    ##
## Widget 7 Value:            0                                                    ##
## Widget 8 Value:            0                                                    ##
## Widget 9 Value:            0                                                    ##
#####################################################################################

D:\Git\PythonProject\ReadWidgetValue>
```
### Raspberry Pi / Linux
```
pi@raspberrypi:~/PythonProject/ReadWidgetValue $ python3 ReadWidgetValue.py
#####################################################################################
## Test with SmartDisplay                                                          ##
## Minimalmodbus version:     2.0.1                                                ##
##                                                                                 ##
## Platform:                  linux                                                ##
## Python version:            3.7.3                                                ##
## Modbus mode:               rtu                                                  ##
## Baudrate (-b):             115200                                               ##
## Port name (-D):            /dev/ttyUSB0                                         ##
## Slave address:             123                                                  ##
## Timeout:                   0.3                                                  ##
## Full file path:            /home/pi/PythonProject/ReadWidgetValue/ReadWidgetValue.py##
#####################################################################################

#####################################################################################
## Current values                                                                  ##
##                                                                                 ##
## Widget 0 Value:            1                                                    ##
## Widget 1 Value:            0                                                    ##
## Widget 2 Value:            0                                                    ##
## Widget 3 Value:            28                                                   ##
## Widget 4 Value:            0                                                    ##
## Widget 5 Value:            0                                                    ##
## Widget 6 Value:            0                                                    ##
## Widget 7 Value:            0                                                    ##
## Widget 8 Value:            0                                                    ##
## Widget 9 Value:            0                                                    ##
#####################################################################################

pi@raspberrypi:~/PythonProject/ReadWidgetValue $
```
