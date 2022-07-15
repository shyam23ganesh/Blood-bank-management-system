import sqlite3
from tkinter import *
conn =sqlite3.connect("data.db")
cursor = conn.cursor()
def adddonor(ID,NAME,BLOOD,ADD,PH,AGE,SEX):
    cursor.execute('''INSERT INTO DONOR VALUES(?,?,?,?,?,?,?)''',(ID,NAME,BLOOD,ADD,PH,AGE,SEX))
    conn.commit()
def addhospital(ID,NAME,PHONE,ADD):
    cursor.execute('''INSERT INTO HOSPITAL VALUES(?,?,?,?)''',(ID,NAME,PHONE,ADD))
    conn.commit()
def addbb(ID,NAME,BLOOD,PHONE,QUANTITY):
    cursor.execute('''INSERT INTO BLOODBANK VALUES(?,?,?,?,?)''', (ID, NAME, BLOOD ,PHONE,QUANTITY))
    conn.commit()
def addrec(ID,NAME,PHONE,PASSWORD):
    cursor.execute('''INSERT INTO RECEPTIONIST VALUES(?,?,?,?)''', (ID, NAME,PHONE,PASSWORD))
    conn.commit()
def deldonor(ID):
    cursor.execute('''DELETE FROM DONOR WHERE ID = :id''',{'id':ID})
    conn.commit()
def checkpass():
    name = nameentry.get()
    password = passentry.get()
    data = cursor.execute('''SELECT NAME,PASSWORD FROM RECEPTIONIST''')
    for record in data:
        if((name==record[0])and(password==record[1])):
            print("password verified")
            donorbut = Button(root,text = "Donor",command=donor)
            donorbut.grid(row = 6 , column = 0 , columnspan=2)
            hospibut = Button(root, text="Add Hospital",command=hospi)
            hospibut.grid(row=7, column=0, columnspan=2)
            bbbut = Button(root, text="Add Employee",command=addr)
            bbbut.grid(row=8, column=0, columnspan=2)
            hbut = Button(root,text="Hospital login",command=loghos)
            hbut.grid(row=9,column=0,columnspan=2)
        else:
            continue
def printhospital(dt1):
    data1 = cursor.execute('''SELECT NAME FROM HOSPITAL''')
    for rec in data1:
        dt1.insert(0.0, "\n\nHospital name : " + rec[0])
def printdonor(dt):
    data = cursor.execute('''SELECT ID,NAME,BLOODGROUP,AGE FROM DONOR''')
    for rec in data:
        dt.insert(0.0 ,"\n\nDonor ID : "+rec[0]+"\nDonor name : "+rec[1]+"\nBlood group :"+rec[2]+"\nDonor's age : "+rec[3])

def seldonor(b,dt):
    print(type(b))
    data = cursor.execute('''SELECT ID,NAME,BLOODGROUP FROM DONOR WHERE BLOODGROUP= :bl''',{'bl':b})
    for rec in data:
        dt.insert(0.0,"\n\nDonor ID : "+rec[0]+"\nDonor name : "+rec[1]+"\nBlood group :"+rec[2])

def loghos():
    log = Toplevel()
    l = Label(log,text="Donor list :")
    l.grid(row=0,column=0)
    mf = Frame(log)
    scrolly = Scrollbar(mf, orient=VERTICAL)
    t = Text(mf, height=10,yscrollcommand=scrolly)
    scrolly.config(command=t.yview)
    scrolly.pack(side=RIGHT,fill=Y)
    t.pack()
    mf.grid(row=2,column=0)
    b = Button(log,text="View donor list",command=lambda : printdonor(t))
    b.grid(row=0,column=1)

    l2 = Label(log,text="Enter the bloodgroup to be searched ")
    l2e = Entry(log)
    l2.grid(row=4,column=0)
    l2e.grid(row=4,column=1)
    lb = Button(log,text="Search",command = lambda : seldonor(l2e.get(),t1))
    lb.grid(row=5,column=0)
    mf2 = Frame(log)
    scroy = Scrollbar(mf2,orient=VERTICAL)
    t1 = Text(mf2,height=10,yscrollcommand=scroy)
    scroy.config(command=t1.yview)
    scroy.pack(side=RIGHT,fill=Y)
    t1.pack()
    mf2.grid(row=7,column=0)

def donor():
    don = Toplevel()
    did = Label(don,text="Donor ID ")

    dname = Label(don,text="Donor's name ")
    dblood = Label(don,text="Donor's bloodgroup ")
    dadd = Label(don,text="Address")
    dph = Label(don,text="Phone number ")
    dage = Label(don , text="Donor's age ")
    dsex = Label(don,text="Donor's sex ")
    did.grid(row=0,column=0)
    dname.grid(row=1,column=0)
    dblood.grid(row=2,column=0)
    dadd.grid(row=3,column=0)
    dph.grid(row=4,column=0)
    dage.grid(row=5,column=0)
    dsex.grid(row=6,column=0)
    ide = Entry(don)
    namee = Entry(don)
    bloode = Entry(don)
    adde = Entry(don)
    phe = Entry(don)
    agee = Entry(don)
    sexe = Entry(don)
    ide.grid(row=0,column=1,columnspan=3)
    namee.grid(row=1, column=1, columnspan=3)
    bloode.grid(row=2, column=1, columnspan=3)
    adde.grid(row=3, column=1, columnspan=3)
    phe.grid(row=4, column=1, columnspan=3)
    agee.grid(row=5, column=1, columnspan=3)
    sexe.grid(row=6, column=1, columnspan=3)
    donaddbut = Button(don,text = "Add Entry",command= lambda : adddonor(ide.get(),namee.get(),bloode.get(),adde.get(),phe.get(),agee.get(),sexe.get()))
    donaddbut.grid(row=7,column=3,columnspan=2)
    bbaddbut = Button(don,text="Add Blood bank entry",command = lambda : addbb(ide.get(),namee.get(),bloode.get(),phe.get(),'1'))
    bbaddbut.grid(row=8,column=3,columnspan=2)
    fr = Frame(don)
    scrolly = Scrollbar(fr,orient=VERTICAL)

    dt = Text(fr,height=10,yscrollcommand =scrolly.set)
    scrolly.config(command=dt.yview)
    scrolly.pack(side=RIGHT,fill=Y)
    dt.pack()
    fr.grid(row=11,column=0,columnspan=3)
    viewd = Button(don,text="View donor list",command= lambda : printdonor(dt))
    viewd.grid(row=10,column=3,columnspan=3)
    dell = Label(don,text="Enter ID to be deleted ")
    dele = Entry(don)
    dell.grid(row=14,column=0)
    dele.grid(row=14,column=1)
    delb = Button(don,text="Delete entry",command= lambda : deldonor(str(dele.get())))
    delb.grid(row=15,column=0)

def hospi():
    hos = Toplevel()
    hid = Label(hos, text="Enter hospital ID ")
    hname = Label(hos, text="Enter hospital name ")
    hph = Label(hos, text="Phone number ")
    had = Label(hos, text="Address")
    hie = Entry(hos)
    hne = Entry(hos)
    hpe = Entry(hos)
    hae = Entry(hos)
    hid.grid(row=0, column=0)
    hname.grid(row=1, column=0)
    hph.grid(row=2, column=0)
    had.grid(row=3, column=0)
    hie.grid(row=0, column=1, columnspan=3)
    hne.grid(row=1, column=1, columnspan=3)
    hpe.grid(row=2, column=1, columnspan=3)
    hae.grid(row=3, column=1, columnspan=3)
    hosaddbut = Button(hos, text="Add hospital",
                       command=lambda: addhospital(hie.get(), hne.get(), hpe.get(), hae.get()))
    hosaddbut.grid(row=4, column=4)
    viewh = Button(hos, text="View Hospital list", command=lambda: printhospital(dt1))
    viewh.grid(row=5, column=4, columnspan=3)

    frh = Frame(hos)
    scrollyh = Scrollbar(frh, orient=VERTICAL)
    dt1 = Text(frh, height=20, yscrollcommand=scrollyh.set)
    scrollyh.config(command=dt1.yview)
    scrollyh.pack(side=RIGHT, fill=Y)
    dt1.pack()
    frh.grid(row=11, column=0, columnspan=3)
def addr():
    r = Toplevel()
    nl = Label(r,text="Enter emplyee name ")
    il = Label(r,text="Enter employee ID")
    pl = Label(r,text="Enter Phone number")
    pal= Label(r,text="Enter password")
    ie = Entry(r)
    ne = Entry(r)
    pe = Entry(r)
    pae = Entry(r)
    il.grid(row = 0,column=0)
    nl.grid(row=1, column=0)
    pl.grid(row=2, column=0)
    pal.grid(row=3, column=0)
    ie.grid(row=0,column=1,columnspan=2)
    ne.grid(row=1, column=1, columnspan=2)
    pe.grid(row=2, column=1, columnspan=2)
    pae.grid(row=3, column=1, columnspan=2)
    addebut = Button(r,text="Add Employee",command=lambda : addrec(ie.get(),ne.get(),pe.get(),pae.get()))
    addebut.grid(row=4,column=3,columnspan=2)
cursor.execute('''CREATE TABLE IF NOT EXISTS DONOR(ID TEXT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, BLOODGROUP TEXT NOT NULL, ADDRESS TEXT , PHONE TEXT NOT NULL, AGE TEXT NOT NULL, SEX TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS HOSPITAL(ID TEXT PRIMARY KEY , NAME TEXT NOT NULL , PHONE TEXT NOT NULL , ADDRESS TEXT NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS BLOODBANK(ID TEXT PRIMARY KEY , NAME TEXT NOT NULL ,BLOODGROUP TEXT NOT NULL, PHONE TEXT NOT NULL , QUANTITY INTEGER NOT NULL)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS RECEPTIONIST(ID TEXT PRIMARY KEY , NAME TEXT NOT NULL , PHONE TEXT NOT NULL , PASSWORD INTEGER NOT NULL)''')
#tkinter
root = Tk()
root.title("Blood bank management system")
root.geometry('400x400')
print("hi")
welcome = Label(root,text="Welcome")
welcome.grid(row=0,columnspan=3)
namelabel = Label(root,text="Enter your name")
namelabel.grid(row=1,column=0)
nameentry = Entry(root)
nameentry.grid(row=1,column=1,columnspan=2)
passlabel = Label(root,text="Enter your password")
passlabel.grid(row=3,column=0)
passentry = Entry(root)
passentry.grid(row=3,column=1,columnspan=2)
verify = Button(root,text="submit",command=checkpass)
verify.grid(row=4,column=3)
root.mainloop()
conn.close()
