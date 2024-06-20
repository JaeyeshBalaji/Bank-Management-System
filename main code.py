def input():
    while True:
        global cur,con
        uu=[]
        con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
        cur=con.cursor()
        cur.execute("use computerproject")
        a1=e1.get()
        a2=e2.get()
        cur.execute("select aadhar from bp")
        for x in cur:
            for y in x:
                uu.append(int(y))
        try:
            a3=int(e3.get())
        except:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID AADHAR NUMBER !!!")
            break
        try:
            a4=int(e4.get())
        except:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID MOBILE NUMBER !!!")
            break
        try:    
            a6=int(e6.get())
        except:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID AGE !!!")
            break
        if(a3 in uu):
            messagebox.showinfo(title="ERROR !!!",message="THIS AADHAR NUMBER ALREADY EXISTS !!!")
            break
        a9=e9.get()
        a9=str(a9).split("/")
        a9=a9[0]+a9[1]+a9[2]
        a5=e5.get()
        a7=e7.get()
        a8=e8.get()
        if(len(str(a3))!=12):
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID AADHAR NUMBER !!!")
            break
        if(len(str(a6))>3):
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID AGE !!!")
            break
        if(len(str(a4))!=10):
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID MOBILE NUMBER !!!")
            break
        if(re.fullmatch(regex, a5)):
            pass
        else:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID EMAIL !!!")
            break
        a9=str(a9)
        cur.execute("insert ignore into bp values({},'{}','{}','{}',{},'{}',{},'{}','{}',{})".format(a3,a1,a2,a9,a6,a7,a4,a5,a8,1000))
        con.commit()    
        messagebox.showinfo(title="DONE !!!",message="ACCOUNT SUCCESSFULLY CREATED ")
        break
def create():
    n=Toplevel()
    n.geometry("810x450")
    n.config(background="pink")
    Label(n,text="Enter your Details",font=("Helvetica",20,"bold","underline"),bg="pink").grid(row=0,column=0,columnspan=2)
    Label(n,text="Enter your First name",font=("Helvetica",20),bg="pink",padx=15).grid(row=1,column=0,sticky="W")
    Label(n,text="Enter your last name",font=("Helvetica",20),bg="pink",padx=15).grid(row=2,column=0,sticky="W")
    Label(n,text="Enter your Aadhar number",font=("Helvetica",20),bg="pink",padx=15).grid(row=3,column=0,sticky="W")
    Label(n,text="Enter your Mobile number",font=("Helvetica",20),bg="pink",padx=15).grid(row=4,column=0,sticky="W")
    Label(n,text="Enter your Email",font=("Helvetica",20),bg="pink",padx=15).grid(row=5,column=0,sticky="W")
    Label(n,text="Enter your Age",font=("Helvetica",20),bg="pink",padx=15).grid(row=6,column=0,sticky="W")
    Label(n,text="Enter your Gender",font=("Helvetica",20),bg="pink",padx=15).grid(row=7,column=0,sticky="W")
    Label(n,text="Enter your Address",font=("Helvetica",20),bg="pink",padx=15).grid(row=8,column=0,sticky="W")
    Label(n,text="Enter your Date of birth[YYYYMMDD]",font=("Helvetica",20),bg="pink",padx=15).grid(row=9,column=0,sticky="W")
    global e1,e2,e3,e4,e5,e6,e7,e8,e9
    listf=["MALE","FEMALE"," OTHER"]
    e7=StringVar(n)
    e7.set(listf[0])
    e1=StringVar()
    e2=StringVar()
    e3=StringVar()
    e4=StringVar()
    e5=StringVar()
    e6=StringVar()
    e8=StringVar()
    e9=StringVar()
    Entry(n,font=("Helvetica",20),textvariable=e1).grid(row=1,column=1,sticky="W")
    Entry(n,font=("Helvetica",20),textvariable=e2).grid(row=2,column=1,sticky="W")
    Entry(n,font=("Helvetica",20),textvariable=e3).grid(row=3,column=1,sticky="W")
    Entry(n,font=("Helvetica",20),textvariable=e4).grid(row=4,column=1,sticky="W")
    Entry(n,font=("Helvetica",20),textvariable=e5).grid(row=5,column=1,sticky="W")
    Entry(n,font=("Helvetica",20),textvariable=e6).grid(row=6,column=1,sticky="W")
    OptionMenu(n,e7,*listf).grid(row=7,column=1)
    Entry(n,font=("Helvetica",20),textvariable=e8).grid(row=8,column=1,sticky="W")
    DateEntry(n,locale="en_us",date_pattern="yyyy/mm/dd",textvariable=e9).grid(row=9,column=1)   
    Button(n,text="Submit",font=("Helvetica",20),bg="violet",command=input).grid(row=12,column=0,columnspan=2)
def rb():
    global v,o
    o=Toplevel()
    v=IntVar()
    o.config(background="pink")
    Label(o,text="How would you like to view the account details ?",font=("Helvetica",20),bg="pink",padx=15).grid(row=0,column=0)
    Radiobutton(o,variable=v,value=1,text="UNSORTED ",font=("Helvetica",20),bg="pink",padx=15,underline=-1).grid(row=1,column=0)
    Radiobutton(o,variable=v,value=2,text="SORTED",font=("Helvetica",20),bg="pink",padx=15).grid(row=2,column=0)
    Button(o,text="Submit",font=("Helvetica",20),bg="violet",command=view).grid(row=3,column=0)   
def view():
    global cur,con,p,w
    o.destroy()
    p=Toplevel()
    p.config(background="pink")
    
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    if(v.get()==1):
        cur.execute("select * from bp")
        l=list(cur)
        Label(p,text="AADHAR NUMBER",font=("Helvetica",18,"bold"),bg="pink",padx=5,pady=2).grid(row=0,column=0)
        Label(p,text="FIRST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=1)
        Label(p,text="LAST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=2)
        Label(p,text="DATE OF BIRTH",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=3)
        Label(p,text="AGE",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=4)
        Label(p,text="GENDER",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=5)
        Label(p,text="MOBILE NUMBER",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=6)
        Label(p,text="EMAIL",font=("Helvetica",18,"bold"),bg="pink",padx=6,pady=2).grid(row=0,column=7)
        Label(p,text="ADDRESS",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=8)
        j=1
        for x in l:
            x=list(x)
            for op in range(9):
                Label(p,text=str(x[op]),font=("Helvetica",18),bg="pink",padx=3,pady=2).grid(row=j,column=op)
            j+=1
    if(v.get()==2):
        Label(p,text="How would you like to sort ?",font=("Helvetica",25),bg="pink",padx=15).grid(row=0,column=0)
        w=IntVar()
        Radiobutton(p,variable=w,value=1,text="BASED ON AADHAR NUMBER ",font=("Helvetica",20),bg="pink",padx=15).grid(row=1,column=0,sticky="E")
        Radiobutton(p,variable=w,value=2,text="BASED ON FIRSTNAME",font=("Helvetica",20),bg="pink",padx=15).grid(row=2,column=0,sticky="E")
        Radiobutton(p,variable=w,value=3,text="BASED ON MOBILIE NUMBER",font=("Helvetica",20),bg="pink",padx=15).grid(row=3,column=0,sticky="E")
        Radiobutton(p,variable=w,value=4,text="BASED ON AGE",font=("Helvetica",20),bg="pink",padx=15).grid(row=4,column=0,sticky="E")
        Radiobutton(p,variable=w,value=5,text="BASED ON GENDER",font=("Helvetica",20),bg="pink",padx=15).grid(row=5,column=0,sticky="E")
        Button(p,text="Submit",font=("Helvetica",20),bg="violet",command=f2).grid(row=6,column=0)
def f2():
    p.destroy()
    global cur,con
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    q=Toplevel()
    q.config(background="pink")
    if(w.get()==1):
        cur.execute("select * from bp order by aadhar")
    elif(w.get()==2):
        cur.execute("select * from bp order by firstname")
    elif(w.get()==3):
        cur.execute("select * from bp order by mobile")
    elif(w.get()==4):
        cur.execute("select * from bp order by age")
    elif(w.get()==5):
        cur.execute("select * from bp order by gender")
    l=list(cur)
    Label(q,text="AADHAR NUMBER",font=("Helvetica",18,"bold"),bg="pink",padx=5,pady=2).grid(row=0,column=0)
    Label(q,text="FIRST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=1)
    Label(q,text="LAST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=2)
    Label(q,text="DATE OF BIRTH",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=3)
    Label(q,text="AGE",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=4)
    Label(q,text="GENDER",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=5)
    Label(q,text="MOBILE NUMBER",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=6)
    Label(q,text="EMAIL",font=("Helvetica",18,"bold"),bg="pink",padx=6,pady=2).grid(row=0,column=7)
    Label(q,text="ADDRESS",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=8)
    j=1
    for x in l:
        x=list(x)
        for op in range(9):
            Label(q,text=str(x[op]),font=("Helvetica",18),bg="pink",padx=3,pady=2).grid(row=j,column=op)
        j+=1
def dele():
    messagebox.showinfo(title="INFO !!!",message="To delete all accounts enter 100 !!!")
    de()
def de():
    
    global cur,con,ac
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    ab=Toplevel()
    ab.geometry("950x120")
    ab.config(background="pink")
    ac=StringVar()
    Label(ab,text="Enter aadhar number of account to be deleted",font=("Helvetica",20),bg="pink",padx=12).grid(row=0,column=0)
    Entry(ab,font=("Helvetica",20),textvariable=ac).grid(row=0,column=1,sticky="W")
    Button(ab,text="Submit",font=("Helvetica",20),bg="violet",command=process,padx=5).grid(row=2,column=0,columnspan=2)
def process():
    az=0
    while True:
        try:
            ad=int(ac.get())
        except:
            messagebox.showinfo(title="ERROR !!!", message="ENTER VALID AADHAR NUMBER !!!")
            break
        cur.execute("select aadhar from bp")
        ae=list(cur)
        for x in ae:
            for af in x:
                if ad==af:
                    cur.execute("delete from bp where aadhar={}".format(ad))
                    con.commit()
                    az=1
                    break
                elif(ad==100):
                    cur.execute("delete from bp ".format(ad))
                    con.commit()
                    az=2
                    break
                    
                    
            
        if(az==1):
            messagebox.showinfo(title="DONE !!!",message="ACCOUNT SUCCESSFULLY DELETED !!!")
            break            
        elif(az==2):
            messagebox.showinfo(title="DONE !!!",message="ALL ACCOUNTS SUCCESSFULLY DELETED !!!")
            break
        else:
            messagebox.showinfo(title="ERROR !!!",message="ACCOUNT DOES NOT EXIST !!!")
            break
def updat():
    global cur,con,wc
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    ww=Toplevel()
    ww.config(background="pink")
    ww.geometry("950x100")
    wc=StringVar()
    Label(ww,text="Enter aadhar number of account to be updated",font=("Helvetica",20),bg="pink",padx=12).grid(row=0,column=0)
    Entry(ww,font=("Helvetica",20),textvariable=wc).grid(row=0,column=1,sticky="W")
    Button(ww,text="Submit",font=("Helvetica",20),bg="violet",command=pro,padx=5).grid(row=2,column=0,columnspan=2)
def pro():
    az=0
    global wd
    while True:
        try:
            wd=int(wc.get())
        except:
            messagebox.showinfo(title="ERROR !!!", message="ENTER VALID AADHAR NUMBER !!!")
            break
        cur.execute("select aadhar from bp")
        ae=list(cur)
        for x in ae:
            for af in x:
                if wd==af:
                    az=1
                    br()
        if(az==1):
            break            
        else:
            messagebox.showinfo(title="ERROR !!!",message="ACCOUNT DOES NOT EXIST !!!")
            break   
def br():
    global cur,con
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    cur.execute("select * from bp where aadhar={}".format(wd))
    k=cur
    k=list(k)
    v=Toplevel()
    v.geometry("810x450")
    v.config(background="pink")
    Label(v,text="Enter your Details",font=("Helvetica",20,"bold","underline"),bg="pink").grid(row=0,column=0,columnspan=2)
    Label(v,text="Enter your First name",font=("Helvetica",20),bg="pink",padx=15).grid(row=1,column=0,sticky="W")
    Label(v,text="Enter your last name",font=("Helvetica",20),bg="pink",padx=15).grid(row=2,column=0,sticky="W")
    Label(v,text="Enter your Mobile number",font=("Helvetica",20),bg="pink",padx=15).grid(row=3,column=0,sticky="W")
    Label(v,text="Enter your Email",font=("Helvetica",20),bg="pink",padx=15).grid(row=4,column=0,sticky="W")
    Label(v,text="Enter your Age",font=("Helvetica",20),bg="pink",padx=15).grid(row=5,column=0,sticky="W")
    Label(v,text="Enter your Gender",font=("Helvetica",20),bg="pink",padx=15).grid(row=6,column=0,sticky="W")
    Label(v,text="Enter your Address",font=("Helvetica",20),bg="pink",padx=15).grid(row=7,column=0,sticky="W")
    Label(v,text="Enter your Date of birth[YYYYMMDD]",font=("Helvetica",20),bg="pink",padx=15).grid(row=8,column=0,sticky="W")
    global v1,v2,v3,v4,v5,v6,v7,v8,v9
    listf=["MALE","FEMALE"," OTHER"]
    v1=StringVar()
    v1.set(k[0][1])
    v2=StringVar()
    v2.set(k[0][2])
    v4=StringVar()    
    v4.set(k[0][6])
    v5=StringVar()
    v5.set(k[0][7])
    v6=StringVar()
    v6.set(k[0][4])
    v7=StringVar()
    v7.set(k[0][5])
    v8=StringVar()
    v8.set(k[0][8])
    v9=StringVar()
    v9.set((str(k[0][3]).split("-"))[0]+(str(k[0][3]).split("-"))[1]+(str(k[0][3]).split("-"))[2])
    Entry(v,font=("Helvetica",20),textvariable=v1).grid(row=1,column=1,sticky="W")
    Entry(v,font=("Helvetica",20),textvariable=v2).grid(row=2,column=1,sticky="W")
    Entry(v,font=("Helvetica",20),textvariable=v4).grid(row=3,column=1,sticky="W")
    Entry(v,font=("Helvetica",20),textvariable=v5).grid(row=4,column=1,sticky="W")
    Entry(v,font=("Helvetica",20),textvariable=v6).grid(row=5,column=1,sticky="W")
    OptionMenu(v,v7,*listf).grid(row=6,column=1)
    Entry(v,font=("Helvetica",20),textvariable=v8).grid(row=7,column=1,sticky="W")
    DateEntry(v,locale="en_us",date_pattern="yyyy/mm/dd",textvariable=v9).grid(row=8,column=1)   
    Button(v,text="Submit",font=("Helvetica",20),bg="violet",command=inp).grid(row=9,column=0,columnspan=2)
def inp():
    while True:
        w1=v1.get()
        w2=v2.get()
        try:
            w4=int(v4.get())
        except:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID MOBILE NUMBER !!!")
            break
        try:    
            w6=int(v6.get())
        except:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID AGE !!!")
            break
        w9=v9.get()
        w9=str(w9).split("/")
        w9=w9[0]+w9[1]+w9[2]
        w5=v5.get()
        w7=v7.get()
        w8=v8.get()
        if(len(str(w4))!=10):
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID MOBILE NUMBER !!!")
            break
        if(re.fullmatch(regex, w5)):
            pass
        else:
            messagebox.showinfo(title="ERROR !!!",message="PLEASE ENTER VALID EMAIL !!!")
            break
        w9=str(w9)
        global cur,con
        con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
        cur=con.cursor()
        cur.execute("use computerproject")
        cur.execute("update bp set firstname='{}',lastname='{}',mobile={},email='{}',age={},gender='{}',adress='{}',Dateofbirth='{}' where aadhar={}".format(w1,w2,w4,w5,w6,w7,w8,w9,wd))
        con.commit()
        messagebox.showinfo(title="DONE !!!",message="ACCOUNT SUCCESSFULLY UPDATED !!!")
        break
def mn():
    messagebox.showinfo(title="!!!",message="THANK YOU !!! SEE YOU AGAIN SOON !!!")
def exits():
    mn()
    m.destroy()
def dp():
    global cur,con,ai,ak
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    ah=Toplevel()
    ah.geometry("800x120")
    ah.config(background="pink")
    ai=StringVar()
    ak=StringVar()
    Label(ah,text="Enter aadhar number of account :",font=("Helvetica",20),bg="pink",padx=12).grid(row=0,column=0)
    Label(ah,text="Enter amount of money to be deposited :",font=("Helvetica",20),bg="pink",padx=12).grid(row=1,column=0)
    Entry(ah,font=("Helvetica",20),textvariable=ai).grid(row=0,column=1,sticky="W")
    Entry(ah,font=("Helvetica",20),textvariable=ak).grid(row=1,column=1,sticky="W")
    Button(ah,text="Submit",font=("Helvetica",20),bg="violet",padx=5,command=dq).grid(row=3,column=0,columnspan=2)
def dq():
    am=0
    while True:
        try:
            aj=int(ai.get())
        except:
            messagebox.showinfo(title="ERROR !!!", message="ENTER VALID AADHAR NUMBER !!!")
            break
        try:
            al=int(ak.get())
        except:
            messagebox.showinfo(title="ERROR !!!", message="ENTER VALID AMOUNT !!!")
            break
        cur.execute("select aadhar from bp")
        ae=list(cur)
        for x in ae:
            for af in x:
                if aj==af:
                    cur.execute("update bp set amount=amount + {} where aadhar={}".format(al,aj))
                    con.commit()
                    am=1
                    break
        if(am==1):
            messagebox.showinfo(title="DONE !!!",message="MONEY SUCCESSFULLY DEPOSITED !!!")
            break            
        else:
            messagebox.showinfo(title="ERROR !!!",message="ACCOUNT DOES NOT EXIST !!!")
            break
def vo():
    global yy,zz
    yy=Toplevel()
    zz=IntVar()
    yy.config(background="pink")
    Label(yy,text="How would you like to view the account details ?",font=("Helvetica",20),bg="pink",padx=15).grid(row=0,column=0)
    Radiobutton(yy,variable=zz,value=1,text="UNSORTED ",font=("Helvetica",20),bg="pink",padx=15,underline=-1).grid(row=1,column=0)
    Radiobutton(yy,variable=zz,value=2,text="SORTED",font=("Helvetica",20),bg="pink",padx=15).grid(row=2,column=0)
    Button(yy,text="Submit",font=("Helvetica",20),bg="violet",command=vie).grid(row=3,column=0)   
def vie():
    global cur,con,pp,ww
    yy.destroy()
    pp=Toplevel()
    pp.config(background="pink")
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    if(zz.get()==1):
        cur.execute("select aadhar,firstname,lastname,amount from bp")
        l=list(cur)
        Label(pp,text="AADHAR NUMBER",font=("Helvetica",18,"bold"),bg="pink",padx=5,pady=2).grid(row=0,column=0)
        Label(pp,text="FIRST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=1)
        Label(pp,text="LAST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=2)
        Label(pp,text="ACCOUNT BALANCE",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=3)
        j=1
        for x in l:
            x=list(x)
            for op in range(4):
                Label(pp,text=str(x[op]),font=("Helvetica",18),bg="pink",padx=3,pady=2).grid(row=j,column=op)
            j+=1
    if(zz.get()==2):
        Label(pp,text="How would you like to sort ?",font=("Helvetica",25),bg="pink",padx=15).grid(row=0,column=0)
        ww=IntVar()
        Radiobutton(pp,variable=ww,value=1,text="BASED ON AADHAR NUMBER ",font=("Helvetica",20),bg="pink",padx=15).grid(row=1,column=0,sticky="E")
        Radiobutton(pp,variable=ww,value=2,text="BASED ON FIRSTNAME",font=("Helvetica",20),bg="pink",padx=15).grid(row=2,column=0,sticky="E")
        Button(pp,text="Submit",font=("Helvetica",20),bg="violet",command=f10).grid(row=6,column=0)
def f10():
    pp.destroy()
    global cur,con
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    q=Toplevel()
    q.config(background="pink")
    if(ww.get()==1):
        cur.execute("select aadhar,firstname,lastname,amount from bp order by aadhar")
    elif(ww.get()==2):
        cur.execute("select aadhar,firstname,lastname,amount from bp order by firstname")
    l=list(cur)
    Label(q,text="AADHAR NUMBER",font=("Helvetica",18,"bold"),bg="pink",padx=5,pady=2).grid(row=0,column=0)
    Label(q,text="FIRST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=1)
    Label(q,text="LAST NAME",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=2)
    Label(q,text="AMOUNT",font=("Helvetica",18,"bold"),bg="pink",padx=3,pady=2).grid(row=0,column=3)
    j=1
    for x in l:
        x=list(x)
        for op in range(4):
            Label(q,text=str(x[op]),font=("Helvetica",18),bg="pink",padx=3,pady=2).grid(row=j,column=op)
        j+=1
def wm():
    global cur,con,bs,bt
    con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
    cur=con.cursor()
    cur.execute("use computerproject")
    ah=Toplevel()
    ah.geometry("800x120")
    ah.config(background="pink")
    bs=StringVar()
    bt=StringVar()
    Label(ah,text="Enter aadhar number of account :",font=("Helvetica",20),bg="pink",padx=12).grid(row=0,column=0)
    Label(ah,text="Enter amount of money to withdraw :",font=("Helvetica",20),bg="pink",padx=12).grid(row=1,column=0)
    Entry(ah,font=("Helvetica",20),textvariable=bs).grid(row=0,column=1,sticky="W")
    Entry(ah,font=("Helvetica",20),textvariable=bt).grid(row=1,column=1,sticky="W")
    Button(ah,text="Submit",font=("Helvetica",20),bg="violet",padx=5,command=mw).grid(row=3,column=0,columnspan=2)  
def mw():
    am=0
    while True:
        try:
            aj=int(bs.get())
        except:
            messagebox.showinfo(title="ERROR !!!", message="ENTER VALID AADHAR NUMBER !!!")
            break
        try:
            al=int(bt.get())
        except:
            messagebox.showinfo(title="ERROR !!!", message="ENTER VALID AMOUNT !!!")
            break
        cur.execute("select aadhar from bp")
        ae=list(cur)
        for x in ae:
            for af in x:
                if aj==af:
                    cur.execute("select amount from bp where aadhar = {}".format(aj))
                    for x in cur :
                        for y in x:
                            ggg=y
                    if ggg-al>=1000:
                        cur.execute("update bp set amount=amount - {} where aadhar = {}".format(al,aj))
                        con.commit()
                        am=1
                        break
                    else:
                        messagebox.showinfo(title="ERROR !!!",message="ACCOUNT DOES NOT HAVE ENOUGH MONEY !!!")
                        am=1000
                        break
        if(am==1):
            messagebox.showinfo(title="DONE !!!",message="MONEY SUCCESSFULLY WITHDRAWN !!!")
            break
        elif(am==1000):
            break            
        else:
            messagebox.showinfo(title="ERROR !!!",message="ACCOUNT DOES NOT EXIST !!!")
            break
global regex,m
from tkinter import *
from tkinter import messagebox
import re
import mysql.connector as my
from tkcalendar import *
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
m=Tk()
m.geometry("1200x900")
m.config(background="lightblue")
con=my.connect(host="localhost",user="root",password="tree",charset="utf8")
cur=con.cursor()
cur.execute("create database if not exists computerproject")
cur.execute("use computerproject")
cur.execute("Create table if not exists bp(aadhar numeric(12) primary key,Firstname char(100),Lastname char(100),Dateofbirth date,Age numeric(3),Gender char(100),Mobile numeric(10),Email char(50),Adress char(200),amount int)")
m.title("ABC BANK")
canvas=Canvas(m,height=95,width=1200)
canvas.create_rectangle(0,0,1200,95,outline="black",width=5,fill="blue")
canvas.create_text(600,50,text="ABC BANK",font=("Helvetica",50,"bold"))
canvas.pack()
Label(m,text="Welcome to the World of Net Banking!!! How can we help you ?",font=("Helvetica",25)).place(x=290,y=130)
Button(m,text="Create a new account",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=create,width=25).place(x=200,y=250)
Button(m,text="View existing account details",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=rb,width=25).place(x=200,y=340)
Button(m,text="Update existing account details",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=updat,width=25).place(x=200,y=430)
Button(m,text="Delete existing account",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=dele,width=25).place(x=200,y=520)
Button(m,text="Exit",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=exits,width=25).place(x=800,y=520)
Button(m,text="Deposit Money",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=dp,width=25).place(x=800,y=250)
Button(m,text="Withdraw Money",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",width=25,command=wm).place(x=800,y=340)
Button(m,text="View account balance",font=('helvetica',25),bg="orange",relief="raised",bd=5,activebackground="yellow",command=vo,width=25).place(x=800,y=430)
cur.close()
con.close()
m.mainloop()
