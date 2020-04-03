if __name__=="__main__":
    exit()
else:
    import serial as sl
    import time
    
    def read(port):
        ini=time.time()
        a="blank"
        with serial.Serial(port, 9600, timeout=10) as ser:
            a=ser.read()
        if(a.find('!')+1):
            j=(a.split('!')[-1].split('\\')[0])
            return j
        else:
            return "o"
