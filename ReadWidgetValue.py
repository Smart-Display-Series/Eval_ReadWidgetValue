"""
Hardware testing of MinimalModbus using the SmartDisplay RS485/Modbus.

Ref: https://minimalmodbus.readthedocs.io/en/stable/index.html

Usage
-------------
::
    python3 scriptname [-rtu] [-ascii] [-b115200] [-D/dev/ttyUSB0]

Arguments:
 * -b : baud rate
 * -D : port name

NOTE: There should be no space between the option switch and its argument.

Defaults to RTU mode.

SmartDisplay Specifications:
-------------------------------
 * SlaveID
    0x7B

 * Registers
    Base idx for widget n: n * 100          for n in [0 ~ 9]
                           n * 100 + 10000  for n in [10 ~ 63]
    Offset (16-bit value each)
        0 Type
        2 PosX              
        3 PosY
        4 Style
        6 Set Value (Value1)
        7 Get Value (Value2)
        8 - 57 String/Time

 * Value2 Mapping Address (16-bit)
    2000 - 2063 
"""
import os
import statistics
import sys
import time
from typing import Any, Dict, List, Optional, Tuple, Type, Union

sys.path.insert(0, "..")
import minimalmodbus

SLAVE_ADDRESS = 0x7B            # SmartDisplay ID
TIMEOUT = 0.3                   # seconds. At least 0.3 seconds required for 2400 bits/s ASCII mode.
VALUE_MAPPING_ADDRESS = 2000

DEFAULT_PORT_NAME = "/dev/ttyUSB0"     # Linux
#DEFAULT_PORT_NAME = "COM22"           # Windows
DEFAULT_BAUDRATE = 115200              # SmartDisplay baudrate

def _box(description: Optional[str] = None, value: Any = None) -> None:
    """Print a single line in a box"""
    MAX_WIDTH = 85
    DESCR_WIDTH = 30
    if description is None:
        print("#" * MAX_WIDTH)
    else:
        if value is None:
            line = "## {}".format(description)
        else:
            line = "## {}:".format(description).ljust(DESCR_WIDTH) + str(value)
        line = line.ljust(MAX_WIDTH - 2) + "##"
        print(line)


def show_test_settings(mode: str, baudrate: int, portname: str) -> None:
    _box()
    _box("Test with SmartDisplay")
    _box("Minimalmodbus version", minimalmodbus.__version__)
    _box(" ")
    _box("Platform", sys.platform)
    _box(
        "Python version",
        "{}.{}.{}".format(
            sys.version_info[0], sys.version_info[1], sys.version_info[2]
        ),
    )
    _box("Modbus mode", mode)
    _box("Baudrate (-b)", baudrate)
    _box("Port name (-D)", portname)
    _box("Slave address", SLAVE_ADDRESS)
    _box("Timeout", TIMEOUT)
    _box("Full file path", os.path.abspath(__file__))
    _box()
    print("")

def show_current_values(instr: minimalmodbus.Instrument) -> None:
    """Read current values via Modbus"""

    values = instr.read_registers(VALUE_MAPPING_ADDRESS, 10)

    _box()
    _box("Current values")
    _box(" ")
    _box("Widget 0 Value", values[0])
    _box("Widget 1 Value", values[1])
    _box("Widget 2 Value", values[2])
    _box("Widget 3 Value", values[3])
    _box("Widget 4 Value", values[4])
    _box("Widget 5 Value", values[5])
    _box("Widget 6 Value", values[6])
    _box("Widget 7 Value", values[7])
    _box("Widget 8 Value", values[8])
    _box("Widget 9 Value", values[9])
    _box()
    print(" ")

def parse_commandline(argv: List[str]) -> Tuple[str, str, int]:
    # TODO Use standard parsing of command line (now that we have dropped Python 2.6)

    mode = minimalmodbus.MODE_RTU
    baudrate = DEFAULT_BAUDRATE
    portname = DEFAULT_PORT_NAME

    for arg in argv:
        if arg.startswith("-ascii"):
            mode = minimalmodbus.MODE_ASCII

        elif arg.startswith("-rtu"):
            mode = minimalmodbus.MODE_RTU

        elif arg.startswith("-b"):
            if len(arg) < 3:
                print("Wrong usage of the -b option. Use -b9600")
                sys.exit()
            baudrate = int(arg[2:])

        elif arg.startswith("-D"):
            if len(arg) < 3:
                print("Wrong usage of the -D option. Use -D/dev/ttyUSB0 or -DCOM4")
                sys.exit()
            portname = arg[2:]

    return portname, mode, baudrate


def main() -> None:
    portname, mode, baudrate = parse_commandline(sys.argv)
    show_test_settings(mode, baudrate, portname)

    inst = minimalmodbus.Instrument(portname, SLAVE_ADDRESS, mode=mode)
    if inst.serial is None:
        print("Instrument.serial is None")
        return
    inst.serial.timeout = TIMEOUT
    inst.serial.baudrate = baudrate

    show_current_values(inst)

if __name__ == "__main__":
    main()
