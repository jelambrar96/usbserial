import serial 
import time 

def init_syrus_serial(syrus_serial):
    syrus_serial.write(b'>SRT;CONFIG<\n')
    data = syrus_serial.readline()
    print(data)
    syrus_serial.write(b'>SRFAinternet.comcel.com.co<\n')
    data = syrus_serial.readline()
    print(data)
    syrus_serial.write(b'>SRFLcomcel<\n')
    data = syrus_serial.readline()
    print(data)
    syrus_serial.write(b'>SRFLcomcel<\n')
    data = syrus_serial.readline()
    print(data)

def get_qpv_data(syrus_serial):
    syrus_serial.write(b'>QPV<\n')
    info = syrus_serial.readline()
    #remove the semicolon
    info.replace(';','')
    #time.sleep(0.1)
    return info

def send_message_cosole(sytus_serial, data): 
    #mesg = 
    #syrus_serial.write(b'>SXASGN3127477304;HABLA<')
    pass

def send_message_phone(syrus_serial, phone, data):
    mesg = '>SXASGN3'+ phone + ';' + data + '<' 
    syrus_serial.write(mesg)
    

def send_message_ip_port(syrus_serial, ipaddress, port):

    pass 

def is_valid(data):

    return True     

def main():
     
    syrus_serial = serial.Serial('/dev/ttyUSB0', 115200)

    init_syrus_serial(syrus_serial)

    if syrus_serial.isOpen:
        print('Syrus connected...')
        while True: 
            # wait a second
            time.sleep(10)
            
            qpv_data = get_qpv_data(syrus_serial)    
            print(type(qpv_data))
            
            # restar the loop if data is not the correct format 
            if (not is_valid(qpv_data)):
                print('invalid QPV')
                continue
            
            send_message_phone(syrus_serial, '3045653650', qpv_data)

            if (not syrus_serial.isOpen):
                print('Syrus connection closed...')
                break


if __name__ == '__main__':
    main()    