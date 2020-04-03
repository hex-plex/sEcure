if __name__=="__main__":
    exit()
else:
    import serial as sl
    
    def read(port):
        ser=sl.Serial(port,9600)
        a=ser.read()
        if(a.find('!')+1):
            j=(a.split('!')[-1].split('\')[0])
        return j
