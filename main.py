import serial as sl
import read as r
import sqlite3 as sq
import time
import os
import crypt as cry
import pyautogui as gu

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
        if key=="o":
            print("We couldn't detect your key within 10secs")
            return "Failed"
        ans=cry.deXor(key,crypt)
        if(ans=="Failed"):
            print("A Wrong Key is been in put as it Failed unlocking")
            exit()
        else:
            return ans
    except:
        print("there was a problem fetching your data!")
        return "Failed"


def typein(query=""):
    if query=="":
        print("Hello please input the website you want to unlock?")
        query=input()
    print("Your query is being proccess please tap the key within 10 secs.")
    text=fetch(query)
    if(text=="Failed"):
        print("There was some error that occured while processing")
        print("do you want to retry [y/n]:")
        ans=input()
        if(ans=="y" or ans=="Y" or ans.lower()=="yes"):
            typein(query)
        return False
    else:
        print("Please keep the cursor in place")
        gu.write(text)
        gu.press('enter')
    del text
    print("The password is been succcess recovered")
    print(" If the login failed please update the correct password" )
    return True

if os.path.isfile(os.getcwd()+"/"+dataBase):
    print("Database Found!")
else:
    if newtable():
        print("New Database created")
    else:
        print("There is some problem creating an Database please create a data base manually")


