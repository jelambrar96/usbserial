import serial
import time 

class Syrus(serial): 

    # atributos 
    self destination_port = {} 
    self destination_address = {}


    # metodos 
    
    def get_qpv_data(self):
        self.write(b'>QPV<\n')
        info = self.readline()
        time.sleep(0.1)
        return info

    def init_syrus_serial(self):
        self.write(b'>SRT;CONFIG<\n')
        data = self.readline()
        print(data)
        self.write(b'>SRFAinternet.comcel.com.co<\n')
        data = self.readline()
        print(data)
        self.write(b'>SRFLcomcel<\n')
        data = self.readline()
        print(data)
        self.write(b'>SRFLcomcel<\n')
        data = self.readline()
        print(data)

    pass 
