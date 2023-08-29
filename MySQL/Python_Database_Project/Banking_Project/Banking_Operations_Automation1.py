import sqlite3
from tkinter import *
from tkinter.ttk import Combobox
from datetime import datetime
from tkinter import messagebox
try:
    conobj=sqlite3.connect(database="banking.sqlite")
    curobj=conobj.cursor()
    curobj.execute("create table accounts(acn_no integer primary key autoincrement,acn_name text,acn_pass text,acn_email text,acn_mob text,acn_bal float,acn_type text,acn_opendate text)")
    curobj.execute("create table txn(txn_acn_no int,txn_amt float,txn_update_bal float,txn_date text,txn_type text)")
    conobj.commit()
    print("tables created")
except:
    print("tables already exists,no need to create..")
conobj.close()

win=Tk()
win.state("zoomed")
win.configure(bg="pink")

lbl_title=Label(win,text="Bank Operations Automation",font=('arial',50,'bold','underline'),bg='pink',fg='blue')
lbl_title.pack()


def main_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def login_check():
        acn=e_acn.get()
        pwd=e_pass.get()
        if(len(acn)==0 or len(pwd)==0):
            messagebox.showerror("login","empty fields are not allowed")
            return
        else:
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from accounts where acn_no=? and acn_pass=?",(acn,pwd))
            global tup_user
            tup_user=curobj.fetchone()
            if(tup_user==None):
                messagebox.showerror("login","Invalid ACN/Pass")
            else:
                login_screen()
            
    lbl_acn=Label(frm,text="ACN",font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)
    e_acn.focus()
    
    lbl_pass=Label(frm,text="Pass",font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)
    
    login_btn=Button(frm,command=login_check,text="login",font=('arial',20,'bold'),bd=5)
    login_btn.place(relx=.45,rely=.3)
    
    reset_btn=Button(frm,text="reset",font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.55,rely=.3)
    
    fp_btn=Button(frm,command=fp_screen,text="forgot password",width=14,font=('arial',20,'bold'),bd=5)
    fp_btn.place(relx=.43,rely=.43)
    
    new_btn=Button(frm,command=newacc_screen,text="open new account",width=17,font=('arial',20,'bold'),bd=5)
    new_btn.place(relx=.41,rely=.55)
    
def newacc_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def open_acn():
        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        mob=e_mob.get()
        typ=cb_type.get()
        bal=1000.0
        open_date=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("insert into accounts(acn_name,acn_pass,acn_email,acn_mob,acn_type,acn_bal,acn_opendate) values(?,?,?,?,?,?,?)",(name,pwd,email,mob,typ,bal,open_date))
        conobj.commit()
        curobj.close()
        
        curobj=conobj.cursor()
        curobj.execute("select max(acn_no) from accounts")
        acn_no=curobj.fetchone()[0]
        conobj.close()
        
        reslbl=Label(frm,bg='powder blue',font=('arial',20,'bold'),fg='green',text=f"Your account is opened successfully with ACN:{acn_no}")
        reslbl.place(relx=.3,rely=.8)
        
    back_btn=Button(frm,command=main_screen,text="back",font=('arial',20,'bold'),bd=5)
    back_btn.place(relx=0,rely=0)
    
    frm_title=Label(frm,text="This is open new account screen",font=('arial',20,'bold'),bg='powder blue',fg='brown')
    frm_title.pack()
    
    lbl_name=Label(frm,text="Name",font=('arial',20,'bold'),bg='powder blue')
    lbl_name.place(relx=.3,rely=.1)

    e_name=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_name.place(relx=.4,rely=.1)
    
    lbl_pass=Label(frm,text="Pass",font=('arial',20,'bold'),bg='powder blue')
    lbl_pass.place(relx=.3,rely=.2)

    e_pass=Entry(frm,font=('arial',20,'bold'),bd=5,show='*')
    e_pass.place(relx=.4,rely=.2)
    
    lbl_email=Label(frm,text="Email",font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.3)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.3)

    lbl_mob=Label(frm,text="Mob",font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.3,rely=.4)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.4)
    
    lbl_type=Label(frm,text="Type",font=('arial',20,'bold'),bg='powder blue')
    lbl_type.place(relx=.3,rely=.5)
    
    cb_type=Combobox(frm,values=['Saving','Current'],font=('arial',20,'bold'))
    cb_type.current(0)
    cb_type.place(relx=.4,rely=.5)
    
    open_btn=Button(frm,command=open_acn,text="open",font=('arial',20,'bold'),bd=5)
    open_btn.place(relx=.45,rely=.6)
    
    reset_btn=Button(frm,text="reset",font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.55,rely=.6)
    
def fp_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def get_pass():
        acn=e_acn.get()
        email=e_email.get()
        mob=e_mob.get()
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select acn_pass from accounts where acn_no=? and acn_email=? and acn_mob=?",(acn,email,mob))
        tup=curobj.fetchone()
        if(tup==None):
            reslbl=Label(frm,bg='powder blue',font=('arial',20,'bold'),fg='red',text=f"wrong details")
            reslbl.place(relx=.3,rely=.6)
        else:
            reslbl=Label(frm,bg='powder blue',font=('arial',20,'bold'),fg='green',text=f"Your Pass is:{tup[0]}")
            reslbl.place(relx=.3,rely=.6)
    back_btn=Button(frm,command=main_screen,text="back",font=('arial',20,'bold'),bd=5)
    back_btn.place(relx=0,rely=0)
    
    frm_title=Label(frm,text="This is forgot password screen",font=('arial',20,'bold'),bg='powder blue',fg='brown')
    frm_title.pack()

    lbl_acn=Label(frm,text="ACN",font=('arial',20,'bold'),bg='powder blue')
    lbl_acn.place(relx=.3,rely=.1)

    e_acn=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_acn.place(relx=.4,rely=.1)

    lbl_email=Label(frm,text="Email",font=('arial',20,'bold'),bg='powder blue')
    lbl_email.place(relx=.3,rely=.2)

    e_email=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_email.place(relx=.4,rely=.2)

    lbl_mob=Label(frm,text="Mob",font=('arial',20,'bold'),bg='powder blue')
    lbl_mob.place(relx=.3,rely=.3)

    e_mob=Entry(frm,font=('arial',20,'bold'),bd=5)
    e_mob.place(relx=.4,rely=.3)
    
    get_btn=Button(frm,command=get_pass,text="get",font=('arial',20,'bold'),bd=5)
    get_btn.place(relx=.45,rely=.4)
    
    reset_btn=Button(frm,text="reset",font=('arial',20,'bold'),bd=5)
    reset_btn.place(relx=.55,rely=.4)
    
    
def login_screen():
    frm=Frame(win)
    frm.configure(bg='powder blue')
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.85)
    
    def show_details():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg="white")
        ifrm.place(relx=.25,rely=.1,relwidth=.6,relheight=.6)
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn_no=?",(tup_user[0],))
        tup=curobj.fetchone()
        conobj.close()
        
        reslbl_1=Label(ifrm,text=f"ACN No.  :\t{tup[0]}",bg='white',font=('arial',15))
        reslbl_1.place(relx=.2,rely=.2)
        
        reslbl_2=Label(ifrm,text=f"Balance  :\t{tup[5]}",bg='white',font=('arial',15))
        reslbl_2.place(relx=.2,rely=.3)
                       
        reslbl_3=Label(ifrm,text=f"Open Date:\t{tup[7]}",bg='white',font=('arial',15))
        reslbl_3.place(relx=.2,rely=.4)
        
        reslbl_4=Label(ifrm,text=f"Acn Type :\t{tup[6]}",bg='white',font=('arial',15))
        reslbl_4.place(relx=.2,rely=.5)
     
    def dep_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg="white")
        ifrm.place(relx=.25,rely=.1,relwidth=.6,relheight=.6)
        
        def add_bal():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(tup_user[0],))
            bal=curobj.fetchone()[0]
            curobj.close()
            
            bal=bal+amt
            curobj=conobj.cursor()
            curobj.execute("update accounts set acn_bal=? where acn_no=?",(bal,tup_user[0]))
            curobj.execute("insert into txn values(?,?,?,?,?)",(tup_user[0],amt,bal,datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"Cr"))
            conobj.commit()
            conobj.close()
            
            messagebox.showinfo("Deposit",f"Amount:{amt} deposited and updated bal is:{bal}")
            e_amt.delete(0,"end")
            
        lbl_amt=Label(ifrm,text="Amount",font=('arial',15,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.2)
        
        e_amt=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_amt.place(relx=.4,rely=.2)
        
        sub_btn=Button(ifrm,command=add_bal,text="submit",font=('arial',15,'bold'),bd=5)
        sub_btn.place(relx=.3,rely=.4)
    
    def withdraw_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg="white")
        ifrm.place(relx=.25,rely=.1,relwidth=.6,relheight=.6)
        
        def withdraw_bal():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select acn_bal from accounts where acn_no=?",(tup_user[0],))
            bal=curobj.fetchone()[0]
            curobj.close()
            if(bal>=amt):
                bal=bal-amt
                curobj=conobj.cursor()
                curobj.execute("update accounts set acn_bal=? where acn_no=?",(bal,tup_user[0]))
                curobj.execute("insert into txn values(?,?,?,?,?)",(tup_user[0],amt,bal,datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"Db"))
                conobj.commit()
                conobj.close()

                messagebox.showinfo("Withdraw",f"Amount:{amt} withdrawn and updated bal is:{bal}")
                e_amt.delete(0,"end")
            else:
                messagebox.showwarning("Withdraw","Insufficient Bal")
                
        lbl_amt=Label(ifrm,text="Amount",font=('arial',15,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.2)
        
        e_amt=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_amt.place(relx=.4,rely=.2)
        
        sub_btn=Button(ifrm,command=withdraw_bal,text="submit",font=('arial',15,'bold'),bd=5)
        sub_btn.place(relx=.3,rely=.4)
    
    def update_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg="white")
        ifrm.place(relx=.25,rely=.1,relwidth=.6,relheight=.6)
        
        def update():
            name=e_name.get()
            pwd=e_pass.get()
            mob=e_mob.get()
            email=e_email.get()
            
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("update accounts set acn_name=?,acn_pass=?,acn_email=?,acn_mob=? where acn_no=?",(name,pwd,email,mob,tup_user[0]))
            conobj.commit()
            conobj.close()
            
            messagebox.showinfo("Update","Profile updated")
            
            e_name.delete(0,"end")
            e_pass.delete(0,"end")
            e_email.delete(0,"end")
            e_mob.delete(0,"end")
            
        
        lbl_name=Label(ifrm,text="Name",font=('arial',15,'bold'),bg='white')
        lbl_name.place(relx=.1,rely=.1)
        
        e_name=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_name.place(relx=.1,rely=.2)
    
        lbl_pass=Label(ifrm,text="Pass",font=('arial',15,'bold'),bg='white')
        lbl_pass.place(relx=.5,rely=.1)
        
        e_pass=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_pass.place(relx=.5,rely=.2)
    
        lbl_mob=Label(ifrm,text="Mob",font=('arial',15,'bold'),bg='white')
        lbl_mob.place(relx=.1,rely=.4)
        
        e_mob=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_mob.place(relx=.1,rely=.5)
    
        lbl_email=Label(ifrm,text="Email",font=('arial',15,'bold'),bg='white')
        lbl_email.place(relx=.5,rely=.4)
        
        e_email=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_email.place(relx=.5,rely=.5)
    
        update_btn=Button(ifrm,command=update,text="update",font=('arial',15,'bold'),bd=5)
        update_btn.place(relx=.4,rely=.7)
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from accounts where acn_no=?",(tup_user[0],))
        tup=curobj.fetchone()
        conobj.close()
        
        e_name.insert(0,tup[1])
        e_pass.insert(0,tup[2])
        e_email.insert(0,tup[3])
        e_mob.insert(0,tup[4])
        
     
    def transfer_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg="white")
        ifrm.place(relx=.25,rely=.1,relwidth=.6,relheight=.6)
        
        def transfer():
            to=e_to.get()
            
            conobj=sqlite3.connect(database="banking.sqlite")
            curobj=conobj.cursor()
            curobj.execute("select * from accounts where acn_no=?",(to,))
            tup=curobj.fetchone()
            curobj.close()
            if(tup==None):
                messagebox.showerror("Transfer","To ACN does not exist")
                return
            else:
                amt=float(e_amt.get())
                curobj=conobj.cursor()
                curobj.execute("select acn_bal from accounts where acn_no=?",(tup_user[0],))
                from_bal=curobj.fetchone()[0]
                curobj.close()
                
                curobj=conobj.cursor()
                curobj.execute("select acn_bal from accounts where acn_no=?",(to,))
                to_bal=curobj.fetchone()[0]
                curobj.close()
                
                if(from_bal>=amt):
                    from_bal=from_bal-amt
                    to_bal=to_bal+amt
                    curobj=conobj.cursor()
                    curobj.execute("update accounts set acn_bal=? where acn_no=?",(from_bal,tup_user[0]))
                    curobj.execute("update accounts set acn_bal=? where acn_no=?",(to_bal,to))
                    
                    curobj.execute("insert into txn values(?,?,?,?,?)",(tup_user[0],amt,from_bal,datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"Db"))
                    curobj.execute("insert into txn values(?,?,?,?,?)",(to,amt,to_bal,datetime.now().strftime("%d-%m-%Y %H:%M:%S"),"Cr"))
                    
                    conobj.commit()
                    conobj.close()

                    messagebox.showinfo("Transfer",f"Amount:{amt} Transfered to ACN:{to} and updated bal is:{from_bal}")
                    e_amt.delete(0,"end")
                else:
                    messagebox.showwarning("Transfer","Insufficient Bal")
            
        
        lbl_to=Label(ifrm,text="To ACN",font=('arial',15,'bold'),bg='white')
        lbl_to.place(relx=.2,rely=.2)
        
        e_to=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_to.place(relx=.4,rely=.2)
        
        
        lbl_amt=Label(ifrm,text="Amount",font=('arial',15,'bold'),bg='white')
        lbl_amt.place(relx=.2,rely=.4)
        
        e_amt=Entry(ifrm,font=('arial',15,'bold'),bd=5)
        e_amt.place(relx=.4,rely=.4)
        
        sub_btn=Button(ifrm,command=transfer,text="transfer",font=('arial',15,'bold'),bd=5)
        sub_btn.place(relx=.3,rely=.6)
    
    def mini_screen():
        ifrm=Frame(frm,highlightthickness=2,highlightbackground='black')
        ifrm.configure(bg="white")
        ifrm.place(relx=.25,rely=.1,relwidth=.6,relheight=.6)
        
        conobj=sqlite3.connect(database="banking.sqlite")
        curobj=conobj.cursor()
        curobj.execute("select * from txn where txn_acn_no=?",(tup_user[0],))
        tups=curobj.fetchall()[-3:]
        
        y=0
        for tup in tups:
            lbl_date=Label(ifrm,font=('arial',15,'bold'),bg='white',text=f"Txn Date: {tup[3]}")
            lbl_date.place(relx=.1,rely=.05+y)
            
            lbl_amt=Label(ifrm,font=('arial',12),bg='white',text=f"Txn Amt:\t{tup[1]}")
            lbl_amt.place(relx=.2,rely=.13+y)
            
            lbl_bal=Label(ifrm,font=('arial',12),bg='white',text=f"Balance:\t{tup[2]}")
            lbl_bal.place(relx=.2,rely=.21+y)
            
            lbl_type=Label(ifrm,font=('arial',12),bg='white',text=f"Txn Type:\t{tup[4]}")
            lbl_type.place(relx=.2,rely=.29+y)
            
            
            y+=.3
        
        
    logout_btn=Button(frm,command=main_screen,text="logout",font=('arial',20,'bold'),bd=5)
    logout_btn.place(relx=.9,rely=0)
    
    frm_title=Label(frm,text=f"This is home screen of user:{tup_user[1]}",font=('arial',20,'bold'),bg='powder blue',fg='brown')
    frm_title.pack()
    
    details_btn=Button(frm,command=show_details,width=12,text="account details",font=('arial',20,'bold'),bd=5)
    details_btn.place(relx=0,rely=.1)
    
    dep_btn=Button(frm,command=dep_screen,width=12,text="deposit",font=('arial',20,'bold'),bd=5)
    dep_btn.place(relx=0,rely=.2)
    
    withdraw_btn=Button(frm,command=withdraw_screen,width=12,text="withdraw",font=('arial',20,'bold'),bd=5)
    withdraw_btn.place(relx=0,rely=.3)
    
    update_btn=Button(frm,command=update_screen,width=12,text="update details",font=('arial',20,'bold'),bd=5)
    update_btn.place(relx=0,rely=.4)
    
    transfer_btn=Button(frm,command=transfer_screen,width=12,text="transfer",font=('arial',20,'bold'),bd=5)
    transfer_btn.place(relx=0,rely=.5)
    
    mini_btn=Button(frm,command=mini_screen,width=12,text="mini stmt",font=('arial',20,'bold'),bd=5)
    mini_btn.place(relx=0,rely=.6)

    
main_screen()
win.mainloop()


# In[ ]:




