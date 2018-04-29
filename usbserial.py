# """
# usb serial python code
# """

import serial

def initsyrus(serial):
    #info = serial.readline()
    serial.write(b'>SRT;CONFIG<\n')
    serial.write(b'>SRFAinternet.comcel.com.co<')
    serial.write(b'>SRFLcomcel<')
    serial.write(b'>SRFLcomcel<')
    #info = serial.readline()
    #if info:
    #    print(info)

def getposition(serial):
    while(True):
        #data = serial.readline()
        serial.write(b'>QPV<')
        data = serial.readline()
        if data:
            print(data)
            decodedata = data.decode('utf-8')
            #print(data)
            return decodedata

def sendmessageposition(serial):
    serial.write(b'>SXADP10103024066703<')
    serial.write(b'>SDA1;P10,P15<')
    serial.write(b'>STD10010<')
    serial.write(b'>SED03NV1;TD1+;ACT=QPV<')

def helloworldmessage(serial):
    serial.write(b'>SXASGN3024066703;Hola<')

def main():
    # Define a serial object
    syrusser = serial.Serial('/dev/ttyUSB0', 115200)
    initsyrus(syrusser)
    
    #position = getposition(syrusser)
    #print(position)
    
    # sendmessageposition(syrusser)
    
    #while(True):
    #    linedata = syrusser.readline()
    #    if (linedata):
    #        print(linedata)
    
    helloworldmessage(syrusser)

if __name__ == '__main__':
    main()
