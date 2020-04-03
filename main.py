import serial as sl
import read as r
import sqlite3 as sq
import time
import os
import crypt as cry


port=""
dataBase="myData.db"
 
def connect(portid):
    global port
    port=portid
    return True

def record(name,password):
    global port
    global dataBase
    try:
        mydb=sq.connect(dataBase)
        key=r.read(port)
        if key=="o":
            print("No devices couldn't be read.")
            return False
        crypt=cry.Xor(key,password)
        #crypt = password
        mydb.execute("INSERT INTO USER (NAME,CRYPT) VALUES ("+str(name)+","+str(crypt)+")")
        print("Recorded it successfully!")
        mydb.close()
        return True
    except:
        print("There is been a problem please check the database")
        mydb.close()
        return False
    
def newtable(i=5):
    global dataBase
    try:
        newdb=sq.connect(dataBase)
        newdb.execute("CREATE TABLE USER (NAME TEXT PRIMARY KEY NOT NULL, CRYPT TEXT NOT NULL)")
        newdb.close()
        return True
    except:
        if os.path.isFile(os.getcwd()+"/"+dataBase):
            os.remove(dataBase)
        return newtable(i-1) if i>0 else False

def fetch(name):
    try:
        sq.connect(dataBase)
        cursor=sq.execute("SELECT CRYPT FROM USER WHERE NAME = "+str(name))
        crypt=cursor[0][0]
        sq.close()
        key = r.read()
        ans=cry.deXor(key,crypt)
        if(ans=="Failed"):
            print("A Wrong Key is been in put as it Failed unlocking")
            exit()
        else:
            return ans
    except:
        print("there was a problem fetching your data")
        return "Failed"





if os.path.isFile(os.getcwd()+"/"+dataBase):
    print("Database Found!")
else:
    if newtable():
        print("New Database created")
    else:
        print("There is some problem creating an Database please create a data base manually")


