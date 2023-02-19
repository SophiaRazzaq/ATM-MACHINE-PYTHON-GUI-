
ID_dic={
        "ibrahim":[7898,50000],
        "hazik":[1234,100000],
        "aun":[5678,20000],
        "talha":[7654,75000],
        "abubakar":[4321,55000],
        "ghulam":[3479,40000],
        "naqash":[5909,30000],
        "taha":[6969,45000],
        "adil":[6000,25000],
        "mujtaba":[8989,23000],
        "ahmed":[0000,80000],
        "tayab":[6666,85000]
        }




#####################################################################

from tkinter import *
import time
# Designing a window
screen=Tk()
screen.geometry("500x700")
screen.title("(ATM)")
screen.iconbitmap('ATMicon.ico')
screen.configure(background='#8b9dc3')


# Updating amount

def update(current,name1):
    f6=Frame()
    f6.place(x=0,y=0,width=500,height=700)
    am3list=[]
    am3list=ID_dic[name1]
    am3list[1]=current
    ID_dic[name1]=am3list
    print(am3list[1])
    Label(f6,text=f"Your new balance is {am3list[1]}").pack()
    Label(f6,text="Do you want to do further transaction:").pack()
    Button(f6,text="YES",command=transaction).place(relx=0.43,rely=0.3)
    Button(f6,text="NO",command=destroy).place(relx=0.54,rely=0.3)


# login function

def login1():
    name1=""
    name1=name.get()
    print(name1)
   
    for x in ID_dic:
        if x==name1:
            check=True
            break
        else:
            check=False
    return name1

#updating amount 2

def update1(current,name1):
       f8=Frame()
       f8.place(x=0,y=0,width=500,height=700)
       am3list=[]
       am3list=ID_dic[name1]
       am3list[1]=current
       ID_dic[name1]=am3list
       print(am3list[1])
       Label(f8,text=f"Your new balance is {am3list[1]}").pack()
       Label(f8,text="Do you want to do further transaction:").pack()
       Button(f8,text="YES",command=transaction).place(relx=0.43,rely=0.3)
       Button(f8,text="NO",command=destroy).place(relx=0.54,rely=0.3)
# Balance Counter
def BALANCE(name1):
    print(name1)
    amountL=[]
    amountL=ID_dic[name1]
    balance1=amountL[1]
    print(balance1)
    return balance1

def calculate_500():
            print(name1)
            current=BALANCE(name1)
            current=current-500
            update(current,name1)
def calculate_1000():
            print(name1)
            current=BALANCE(name1)
            current=current-1000
            update(current,name1)
def calculate_5000():
            print(name1)
            current=BALANCE(name1)
            current=current-5000
            update(current,name1)
def calculate_10000():
            print(name1)
            current=BALANCE(name1)
            current=current-10000
            update(current,name1)
def calculate_15000():
            print(name1)
            current=BALANCE(name1)
            current=current-15000
            update(current,name1)
def calculate_20000():
            print(name1)
            current=BALANCE(name1)
            current=current-20000
            update(current,name1)
# second call

def cAlculate_500():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current-500
            update1(current,name1)
def cAlculate_1000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current-1000
            update1(current,name1)
def cAlculate_5000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current-5000
            update1(current,name1)
def cAlculate_10000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current-10000
            update1(current,name1)
def cAlculate_15000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current-15000
            update1(current,name1)
def cAlculate_20000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current-20000
            update1(current,name1)

# deposti 1

def deposit1():
              f10=Frame()
              f10.place(x=0,y=0,width=500,height=700)
              Button(f10,text="500",padx=70,pady=50,bg='#8b9dc3',command=CAlculate_500).place(relx=0,rely=0)
              Button(f10,text="1000",padx=70,pady=50,bg='#8b9dc3',command=CAlculate_1000).place(relx=0,rely=0.2)
              Button(f10,text="5000",padx=70,pady=50,bg='#8b9dc3',command=CAlculate_5000).place(relx=0,rely=0.5)
              Button(f10,text="10,000",padx=70,pady=50,bg='#8b9dc3',command=CAlculate_10000).place(relx=0.5,rely=0)
              Button(f10,text="20,000",padx=70,pady=50,bg='#8b9dc3',command=CAlculate_15000).place(relx=0.5,rely=0.2)
              Button(f10,text="other",padx=70,pady=50,bg='#8b9dc3',command=CAlculate_20000).place(relx=0.5,rely=0.5)

def CAlculate_500():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current+500
            update1(current,name1)
def CAlculate_1000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current+1000
            update1(current,name1)
def CAlculate_5000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current+5000
            update1(current,name1)
def CAlculate_10000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current+10000
            update1(current,name1)
def CAlculate_15000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current+15000
            update1(current,name1)
def CAlculate_20000():
            name1=login1()
            print(name1)
            current=BALANCE(name1)
            current=current+20000
            update1(current,name1)
#Fuction to destroy window


def destroy():
    screen.destroy()

def withdraw():
            f7=Frame()
            f7.place(x=0,y=0,width=500,height=700)
            Button(f7,text="500",padx=70,pady=50,bg='#8b9dc3',command=cAlculate_500).place(relx=0,rely=0)
            Button(f7,text="1000",padx=70,pady=50,bg='#8b9dc3',command=cAlculate_1000).place(relx=0,rely=0.2)
            Button(f7,text="5000",padx=70,pady=50,bg='#8b9dc3',command=cAlculate_5000).place(relx=0,rely=0.5)
            Button(f7,text="10,000",padx=70,pady=50,bg='#8b9dc3',command=cAlculate_10000).place(relx=0.5,rely=0)
            Button(f7,text="15,000",padx=70,pady=50,bg='#8b9dc3',command=cAlculate_15000).place(relx=0.5,rely=0.2)
            Button(f7,text="20,000",padx=70,pady=50,bg='#8b9dc3',command=cAlculate_20000).place(relx=0.5,rely=0.5)

# balance inquiry1

def balance1():
          name1=login1()
          f9=Frame()
          f9.place(x=0,y=0,width=500,height=700) 
          print("Hello")

          amBalance=BALANCE(name1)
          Label(f9,text=f"{amBalance}").pack()
          Label(f9,text="Do you want to do further transaction:").pack()
          Button(f9,text="YES",command=transaction).place(relx=0.43,rely=0.3)
          Button(f9,text="NO",command=destroy).place(relx=0.54,rely=0.3)


# Transaction
def transaction():
                print("Hello")
                f5=Frame()
                f5.place(x=0,y=0,width=500,height=700)
                Label(f5,text="Select Options",font='comicsansms 20 bold').pack()
                Button(f5,text="WithDraw",command=withdraw).pack()
                Button(f5,text="Balance Inquiry",command=balance1).pack()
                Button(f5,text="Deposit",command=deposit1).pack()






# login function

def login():
    name1=""
    name1=name.get()
    print(name1)
   
    for x in ID_dic:
        if x==name1:
            check2=True
            break
        else:
            check2=False
    print(check2)

# check function to check password
    def check():
     print(code.get())
     code1=int(code.get())
     print(type(code1))
     amlist=(ID_dic[name1])
     amlist1=int(amlist[0])
     balance=int(amlist[1])
     print(balance)
     print(type(balance))
     print(type(amlist1))
     if code1==amlist[0]:
            print("matched")
            check1=True
     else:
            print("not")
            print("incorrect")
            Label(f2,text="Incorrect password").pack()

            def withdraw():
              Button(f6,text="500",padx=70,pady=50,bg='#8b9dc3',command=calculate_500).place(relx=0,rely=0)
              Button(f6,text="1000",padx=70,pady=50,bg='#8b9dc3',command=calculate_1000).place(relx=0,rely=0.2)
              Button(f6,text="5000",padx=70,pady=50,bg='#8b9dc3',command=calculate_5000).place(relx=0,rely=0.5)
              Button(f6,text="10,000",padx=70,pady=50,bg='#8b9dc3',command=calculate_10000).place(relx=0.5,rely=0)
              Button(f6,text="15,000",padx=70,pady=50,bg='#8b9dc3',command=calculate_15000).place(relx=0.5,rely=0.2)
              Button(f6,text="20,000",padx=70,pady=50,bg='#8b9dc3',command=calculate_20000).place(relx=0.5,rely=0.5)
              def transaction():
                print("Hello")
                f5=Frame()
                f5.place(x=0,y=0,width=500,height=700)
                Label(f5,text="Select Options",font='comicsansms 20 bold').pack()
                Button(f5,text="WithDraw",command=withdraw).pack()
                Button(f5,text="Balance Inquiry",command=balance).pack()
                Button(f5,text="Deposit",command=deposit).pack()
     if check1:
        f3=Frame()
        f3.place(x=0,y=0,width=500,height=700)


# Calculater

# For withdraw


        def calculate_500():
            print(name1)
            current=BALANCE(name1)
            current=current-500
            update(current,name1)
        def calculate_1000():
            print(name1)
            current=BALANCE(name1)
            current=current-1000
            update(current,name1)
        def calculate_5000():
            print(name1)
            current=BALANCE(name1)
            current=current-5000
            update(current,name1)
        def calculate_10000():
            print(name1)
            current=BALANCE(name1)
            current=current-10000
            update(current,name1)
        def calculate_15000():
            print(name1)
            current=BALANCE(name1)
            current=current-15000
            update(current,name1)
        def calculate_20000():
            print(name1)
            current=BALANCE(name1)
            current=current-20000
            update(current,name1)


# for deposit

        def Calculate_500():
            print(name1)
            current=BALANCE(name1)
            current=current+500
            update(current,name1)
        def Calculate_1000():
            print(name1)
            current=BALANCE(name1)
            current=current+1000
            update(current,name1)
        def Calculate_5000():
            print(name1)
            current=BALANCE(name1)
            current=current+5000
            update(current,name1)
        def Calculate_10000():
            print(name1)
            current=BALANCE(name1)
            current=current+10000
            update(current,name1)
        def Calculate_15000():
            print(name1)
            current=BALANCE(name1)
            current=current+15000
            update(current,name1)
        def Calculate_20000():
            print(name1)
            current=BALANCE(name1)
            current=current+20000
            update(current,name1)
            
        def display():
            print("HEllo")
        def deposit():
              f7=Frame()
              f7.place(x=0,y=0,width=500,height=700)
              Button(f7,text="500",padx=70,pady=50,bg='#8b9dc3',command=Calculate_500).place(relx=0,rely=0)
              Button(f7,text="1000",padx=70,pady=50,bg='#8b9dc3',command=Calculate_1000).place(relx=0,rely=0.2)
              Button(f7,text="5000",padx=70,pady=50,bg='#8b9dc3',command=Calculate_5000).place(relx=0,rely=0.5)
              Button(f7,text="10,000",padx=70,pady=50,bg='#8b9dc3',command=Calculate_10000).place(relx=0.5,rely=0)
              Button(f7,text="20,000",padx=70,pady=50,bg='#8b9dc3',command=Calculate_15000).place(relx=0.5,rely=0.2)
              Button(f7,text="other",padx=70,pady=50,bg='#8b9dc3',command=Calculate_20000).place(relx=0.5,rely=0.5)


        
        def balance():
          f4=Frame()
          f4.place(x=0,y=0,width=500,height=700) 
          print("Hello")
          amBalance=BALANCE(name1)
          Label(f4,text=f"{amBalance}").pack()
          Label(f4,text="Do you want to do further transaction:").pack()
          def transaction():
                print("Hello")
                f5=Frame()
                f5.place(x=0,y=0,width=500,height=700)
                Label(f5,text="Select Options",font='comicsansms 20 bold').pack()
                Button(f5,text="WithDraw",command=withdraw).pack()
                Button(f5,text="Balance Inquiry",command=balance).pack()
                Button(f5,text="Deposit",command=deposit).pack()
          Button(f4,text="YES",command=transaction).place(relx=0.43,rely=0.3)
          Button(f4,text="NO",command=destroy).place(relx=0.54,rely=0.3)
        print("HEllo") 
        def withdraw():
            f6=Frame()
            f6.place(x=0,y=0,width=500,height=700)
            Button(f6,text="500",padx=70,pady=50,bg='#8b9dc3',command=calculate_500).place(relx=0,rely=0)
            Button(f6,text="1000",padx=70,pady=50,bg='#8b9dc3',command=calculate_1000).place(relx=0,rely=0.2)
            Button(f6,text="5000",padx=70,pady=50,bg='#8b9dc3',command=calculate_5000).place(relx=0,rely=0.5)
            Button(f6,text="10,000",padx=70,pady=50,bg='#8b9dc3',command=calculate_10000).place(relx=0.5,rely=0)
            Button(f6,text="20,000",padx=70,pady=50,bg='#8b9dc3',command=calculate_15000).place(relx=0.5,rely=0.2)
            Button(f6,text="other",padx=70,pady=50,bg='#8b9dc3',command=calculate_20000).place(relx=0.5,rely=0.5)
        Label(f3,text="Select Options",font='comicsansms 20 bold').pack()
        Button(f3,text="WithDraw",command=withdraw).pack()
        Button(f3,text="Balance Inquiry",command=balance).pack()
        Button(f3,text="Deposit",command=deposit).pack()

    if check2:
        print("why")
        f2=Frame()
        f2.place(x=0,y=0,width=500,height=700)
        Label(f2,text="Enter your Password:",font='comicsansms 20 bold',fg='#8b9dc3').pack()
        code=StringVar()
        e2=Entry(f2,textvariable=code)
        e2.place(relx=0.4,rely=0.4)
        b2=Button(f2,text="Login",command=check)
        b2.place(relx=0.4,rely=0.5)
    else:
        print("kya")
        Label(text="Account not found",bg='#8b9dc3').place(relx=0.4,rely=0.17)
       
    




    
   
    

my_label=Label(screen,text="Welcome To ATM",font="comicsansms 20 bold",fg='#3b5998',bg='#8b9dc3')
my_label.pack()
Label(screen,text="Enter your name:",bg='#8b9dc3').pack()
name=StringVar()
e3=Entry(textvariable=name)
e3.pack()
b3=Button(text="Enter",command=login)
b3.place(relx=0.46,rely=0.12)
screen.mainloop()