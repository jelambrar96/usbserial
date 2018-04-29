import serial

def main():

    baudios = [
        300,
        600,
        1200,
        2400,
        4800,
        9600,
        19200,
        38400,
        57600,
        112500,
        115200
        ]

    for item in baudios:
        syrus_serial = serial.Serial('/dev/ttyUSB0', item)
        syrus_serial.write(b'>SMTN<')
        syrus_serial.write(b'>SXABR115200<')
        



if __name__ == '__main__':
    main()