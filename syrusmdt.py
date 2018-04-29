# """
# usb serial python code
# """

import serial

def initsyrus(serial):
    serial.write(b'>SRT;CONFIG<\n')
    serial.write(b'>SRFAinternet.comcel.com.co<')
    serial.write(b'>SRFLcomcel<')
    serial.write(b'>SRFLcomcel<')

def main():
    syrusser = serial.Serial('/dev/ttyUSB0', 115200)
    initsyrus(syrusser)

if __name__ == '__main__':
    main()
