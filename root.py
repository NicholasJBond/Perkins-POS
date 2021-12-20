from tkinter import *
from login import *
import login

import time as tm
import sqlite3




conn = sqlite3.connect('PerkinPOSDatabase')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS employees(firstName TEXT, lastName TEXT, employeeNumber TEXT, email TEXT, phone TEXT, address TEXT, dob TEXT, prefix TEXT, voidall TEXT, changeqty TEXT, markdown TEXT, reset TEXT, zreport TEXT, xreport TEXT, tenderdeclare TEXT, removetender TEXT, employeesonreg TEXT, cashindrawer TEXT, vendingmachine TEXT, openkey TEXT, epay TEXT, epayrefund TEXT, items TEXT, accounts TEXT, rewards TEXT, employee TEXT, supplier TEXT)')
c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL,  priceincrement INT, quantityInStock REAL, itemType INT)')

#variables
versionName = "PerkinsPOSTest-2.2"
global state
state = 'Invoice'
companyName="Perkins POS"
inputMain = 0

global cartPrice
global cartQuantity

global barcodeHolder
global voidmode
cartPrice=0
cartQuantity=[]

quantity = 1


#function
def startLoginKeybind(self):
   startLogin()
   

def close():
   root.destroy()
   exit()

def logout():
   
   root.destroy()
   

def donothing():
   print("Nothing Done")

   
def InvoiceMode():
   changeState("Invoice")
   voidmode.set(False)

def VoidMode():
   
   changeState("Void")
   voidmode.set(True)

def alternateMode(self):
   entryInput.delete(0, END)
   
   if state == 'Void':
      InvoiceMode()
   else:
      VoidMode()

def mainMenubar():
  
   menubar = Menu(root)
   systemmenu = Menu(menubar, tearoff=0)
   systemmenu.add_command(label="Invoice", command=InvoiceMode, state = ACTIVE, accelerator="\\")
   systemmenu.add_command(label="Price & Quantity Check", command=donothing, state=DISABLED)
   systemmenu.add_command(label="Void", command=VoidMode, state=ACTIVE, accelerator=('\\'))
   systemmenu.add_separator()
   systemmenu.add_command(label="Logout", command=logout, state=ACTIVE)
   systemmenu.add_command(label="Exit", command=close, accelerator="Cmd+Q")
   menubar.add_cascade(label="System", menu=systemmenu)

   modifymenu = Menu(menubar, tearoff=0)
   modifymenu.add_command(label="Void", command=VoidMode, state=ACTIVE, accelerator='\\')
   modifymenu.add_command(label="Void All", command=donothing, state=DISABLED)
   modifymenu.add_separator()
   modifymenu.add_command(label="Change Qty", command=donothing, state=DISABLED)
   modifymenu.add_command(label="Markdown", command=donothing, state=DISABLED)
   modifymenu.add_command(label="Reset", command=donothing, state=DISABLED)
   menubar.add_cascade(label="Modify", menu=modifymenu)

   managermenu = Menu(menubar, tearoff=0)
   managermenu.add_command(label="Z-Report", command=donothing, state=DISABLED)
   managermenu.add_command(label="X-Report", command=donothing, state=DISABLED)
   managermenu.add_command(label="Tender Declaration", command=donothing, state=DISABLED)
   managermenu.add_command(label="Remove Tender", command=donothing, state=DISABLED)
   managermenu.add_separator()
   managermenu.add_command(label="Employees On Register", command=donothing, state=DISABLED)
   managermenu.add_command(label="Cash In Drawer", command=donothing, state=DISABLED)
   managermenu.add_separator()
   managermenu.add_command(label="Training Mode", command=donothing, state=DISABLED)
   managermenu.add_command(label="Vending Machine Sales", command=donothing, state=DISABLED)
   managermenu.add_command(label="Open Key", command=donothing, state=DISABLED)
   managermenu.add_command(label="Epay", command=donothing, state=DISABLED)
   managermenu.add_command(label="Epay Refund", command=donothing, state=DISABLED)
   
   

   menubar.add_cascade(label="Manager Menu", menu=managermenu)

   databasemenu = Menu(menubar, tearoff=0)
   menubar.add_cascade(label="Database", menu=databasemenu)


   itemsmenu = Menu(databasemenu, tearoff = 0)
   databasemenu.add_cascade(label="Items", menu = itemsmenu)
   itemsmenu.add_command(label="Add Item", command =donothing, state = DISABLED)
   itemsmenu.add_command(label="Remove Item", command =donothing, state = DISABLED)
   itemsmenu.add_separator()
   itemsmenu.add_command(label="Change Item PLU", command =donothing, state = DISABLED)
   itemsmenu.add_command(label="Change Item Description", command =donothing, state = DISABLED)
   itemsmenu.add_command(label="Change Item Price", command =donothing, state = DISABLED)
   itemsmenu.add_command(label="Change Item Price Increment", command =donothing, state = DISABLED)
   itemsmenu.add_separator()
   itemsmenu.add_command(label="Set Stock", command =donothing, state = DISABLED)
   itemsmenu.add_command(label="Add Stock", command =donothing, state = DISABLED)


   accountsmenu=Menu(databasemenu, tearoff=0)
   databasemenu.add_cascade(label="Accounts", menu=accountsmenu)
   accountsmenu.add_command(label="Add Account", command=donothing, state=DISABLED)
   accountsmenu.add_command(label="Remove Account", command=donothing, state=DISABLED)
   accountsmenu.add_separator()
   accountsmenu.add_command(label="Change Account Number", command=donothing, state=DISABLED)
   accountsmenu.add_command(label="Change Account Name", command=donothing, state=DISABLED)
   accountsmenu.add_separator()
   accountsmenu.add_command(label="Set Account Balance", command=donothing, state=DISABLED)
   accountsmenu.add_command(label="Add Money to Balance", command=donothing, state=DISABLED)


   rewardsmenu=Menu(databasemenu, tearoff=0)
   databasemenu.add_cascade(label="Rewards", menu=rewardsmenu)
   rewardsmenu.add_command(label="Register Rewards Card", command=donothing, state=DISABLED)
   rewardsmenu.add_command(label="Deregister Rewards Card", command=donothing, state=DISABLED)
   rewardsmenu.add_separator()
   rewardsmenu.add_command(label="Change Rewards Card Number", command=donothing, state=DISABLED)
   rewardsmenu.add_command(label="Change Rewards Card Name", command=donothing, state=DISABLED)
   rewardsmenu.add_separator()
   rewardsmenu.add_command(label="Set Reward Points", command=donothing, state=DISABLED)
   rewardsmenu.add_command(label="Add Reward Points", command=donothing, state=DISABLED)

   databasemenu.add_separator()
   employeemenu=Menu(databasemenu, tearoff=0)
   databasemenu.add_cascade(label="Employee", menu=employeemenu)
   employeemenu.add_command(label="Register Employee", command=donothing, state=DISABLED)
   employeemenu.add_command(label="Deregister Employee", command=donothing, state=DISABLED)
   employeemenu.add_separator()
   employeeinfomenu=Menu(employeemenu, tearoff=0)
   employeemenu.add_cascade(label="Edit Employee Info", menu=employeeinfomenu)
   employeeinfomenu.add_command(label="Employee Number", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Name", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Email", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Phone Number", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Date of Birth", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Address Line 1", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Address Line 2", command=donothing, state=DISABLED)
   employeeinfomenu.add_command(label="Rank Name", command=donothing, state=DISABLED)
   employeeinfomenu.add_separator()
   employeeinfomenu.add_command(label="Edit All", command=donothing, state=DISABLED)
   employeemenu.add_command(label="Edit Employee Permissions", command=donothing, state=DISABLED)

   databasemenu.add_command(label="Settings", command=donothing, state=DISABLED)

   supliermenu=Menu(menubar, tearoff=0)
   menubar.add_cascade(label="Supplier", menu=supliermenu)
   supliermenu.add_command(label="Order Products", command=donothing, state=DISABLED)






   root.config(menu=menubar)

def entryWidgets():
   global entry4
   global entry5
   global entry6
   global entry7
   global entry8
   global entry9
   global entry10
   global entry11
   global entry12
   entry4=Entry(root,width=11, font=("Arial",15), justify='center')
   entry4.grid(column=0, row=4)
   entry5=Entry(root,width=11, font=("Arial",15), justify='center')
   entry5.grid(column=1, row=4)
   entry6=Entry(root,width=11, font=("Arial",15), justify='center')
   entry6.grid(column=2, row=4)
   entry7=Entry(root,width=11, font=("Arial",15), justify='center')
   entry7.grid(column=3, row=4)
   entry8=Entry(root,width=11, font=("Arial",15), justify='center')
   entry8.grid(column=4, row=4)
   entry9=Entry(root,width=11, font=("Arial",15), justify='center')
   entry9.grid(column=5, row=4)
   entry10=Entry(root,width=11, font=("Arial",15), justify='center')
   entry10.grid(column=6, row=4)
   entry11=Entry(root,width=11, font=("Arial",15), justify='center')
   entry11.grid(column=7, row=4)
   entry12=Entry(root,width=11, font=("Arial",15), justify='center')
   entry12.grid(column=8, row=4)

def changeState(value):
   global state
   state = value
   entry4.config(state=NORMAL)
   entry4.delete(0, END)
   entry4.insert(1, state)
   entry4.config(state=DISABLED)

def voidmodefunc():
   if (voidmode.get()==1):

      changeState("Void")

   else:
      changeState("Invoice")

def widgets():
   global textbox1
   global invoiceOutput
   global invoicePriceOutput
   global entryInput
   global entryOutput
   entryInput = Entry(root, width=75, font=("Arial", 25))
   entryInput.grid(column=0, row=1, columnspan=9, sticky=NW, padx=5, pady=0)
   entryInput.focus()
   entryOutput=Entry(root, width=15, font=("Arial",15))
   entryOutput.grid(column=10, row=3, sticky=E, pady=5, rows=2)

   

   #labels
   label1=Label(root, text="Items")
   label1.grid(column=9, row=0, sticky=N, pady=1)
   label2=Label(root, text="Price")
   label2.grid(column=10, row=0, sticky=N, pady=1)
   label3=Label(root, text="Subtotal: $", font=("Arial", 20))
   label3.grid(column=9, row=3, sticky=E, pady=5, rows=2)

   label4=Label(root, text="State", font=("Arial", 15))
   label4.grid(column=0, row=3, pady=5)
   label5=Label(root, text="Employee", font=("Arial", 15))
   label5.grid(column=1, row=3, pady=5)
   label6=Label(root, text="Manager Level", font=("Arial", 15))
   label6.grid(column=2, row=3, pady=5)
   label7=Label(root, text="Rewards Value", font=("Arial", 15))
   label7.grid(column=3, row=3, pady=5)
   label8=Label(root, text="Account Value", font=("Arial", 15))
   label8.grid(column=4, row=3, pady=5)
   label9=Label(root, text="Number of Sales", font=("Arial", 15))
   label9.grid(column=5, row=3, pady=5)
   label10=Label(root, text="Worth of Sales", font=("Arial", 15))
   label10.grid(column=6, row=3, pady=5)
   label11=Label(root, text="Date", font=("Arial", 15))
   label11.grid(column=7, row=3, pady=5)
   label12=Label(root, text="Time", font=("Arial", 15))
   label12.grid(column=8, row=3, pady=5)

   label13=Label(root, text="Subtotal: $", font=("Arial", 20))
   label13.grid(column=9, row=3, sticky=E, pady=5, rows=2)
   
   #Listboxes
   invoiceOutput = Listbox(root, height=47, width=40)
   invoiceOutput.grid(column=9, row=1, rowspan=2, sticky=NW)
   invoicePriceOutput = Listbox(root, height=47, width=17)
   invoicePriceOutput.grid(column=10, row=1, rowspan=2, sticky=NW)

   #Checkboxes
   checkbox1=Checkbutton(root, text="Void Mode", font=('Arial', 20), variable=voidmode, onvalue=1, offvalue=0, command=voidmodefunc)
   checkbox1.grid(column=9, row=3, rowspan=2, sticky=W, padx=50)

   #textbox
   textbox1=Text(root, width=117, height=44, font=("Arial", 15))
   textbox1.grid(row=1, column=0, sticky=S, columnspan=9, rows=2)

def printText(text, value):

   if (value == 1):
      textbox1.config(state=NORMAL)
      
      
      textbox1.insert(1.0, "|->"+companyName+">----------\n")
      textbox1.insert(1.0, text+"\n")

      textbox1.config(state=DISABLED)

   else:
      textbox1.config(state=NORMAL)
      textbox1.delete(1.0, END)


      textbox1.insert(1.0, text+"\n")
      

      textbox1.config(state=DISABLED)  

def displayTimeAndDate():
   currentTime= tm.strftime('%H:%M:%S')
   entry12.config(state=NORMAL)
   entry12.delete(0, END)
   entry12.insert(1, str(currentTime))
   entry12.config(state=DISABLED)
   entry11.config(state=NORMAL)
   entry11.delete(0, END)
   entry11.insert(1, tm.strftime('%x'))
   entry11.config(state=DISABLED)
   root.after(1000, displayTimeAndDate)

def check_float(potential_float):
    try:
        float(potential_float)

        return True
    except ValueError:
        return False

def clearScreen():
   invoiceOutput.delete(0, END)
   invoicePriceOutput.delete(0, END)

def cashPayment(self):
   if (keybaord==0):

      clearScreen()
      entryOutput.config(state=NORMAL)
      entryOutput.delete(0, END)
      entryOutput.insert(1, 0)
      printText("Paid With Cash. Total paid was $" + str(cartPrice), 0)
      


def eftposPayment(self):
   if (keybaord==0):

      changeState("Eftpos")

def accountPayment(self):
   if (keybaord==0):

      changeState("Account")

def memberpointsPayment(self):
   if (keybaord==0):

      changeState("Memberpoint")

def giftcardPayment(self):
   if (keybaord==0):

      changeState("GiftCard")

def reprintLast(self):
   if (keybaord==0):

      changeState("reprintLast")

def updateSubtotal():
   entryOutput.config(state=NORMAL)
   entryOutput.delete(0, END)
   entryOutput.insert(1, cartPrice)

def getInput(self):
   
   global barcodeHolder
   global quantity
   global stateholder
   global cartPrice
   conn = sqlite3.connect('PerkinPOSDatabase')
   c = conn.cursor()
   inputMain = entryInput.get()
   entryInput.delete(0, END)

   
   

   
   
   

   

   if (state=='Invoice' or state == 'Void'):
      

      
      c.execute("SELECT description FROM allItemsAndCodes WHERE barcode =?", [inputMain])
      dbFetch = c.fetchone()
      if (dbFetch == None):
         printText("Barcode not on file; Please try again\nType 'help' and then hit enter to show a list of commands", 0)
         if stateholder=='Void':
            VoidMode()

         else:
            InvoiceMode()

      else:

         c.execute("SELECT * FROM allItemsAndCodes WHERE barcode =?", [inputMain])
         dbFetch = c.fetchone()
         if dbFetch[3]==0:
            priceIncrement = " per kilo"
            printText("Enter weight in kilograms", 0)
            barcodeHolder = inputMain
            stateholder = state
            changeState("Weigh Item")
      
      
            

         else:
            priceIncrement = " each"
            if (state != 'Void'):
               cartPrice = float(cartPrice)+float(dbFetch[2])
               cartQuantity.append(quantity)
               invoiceOutput.insert("end", str(dbFetch[1]) + " x " + str(quantity) + " at $" + str(dbFetch[2]) + priceIncrement)
               invoicePriceOutput.insert("end", "$" + str(dbFetch[2]*float(quantity)))
               quantity=1
               printText("Please Scan Another Barcode to continue", 0)


            else:
               cartPrice = float(cartPrice)+float(dbFetch[2]*-1)
               cartQuantity.append(-1*quantity)
               
               invoiceOutput.insert("end", "-" + str(dbFetch[1]) + " x " + str(quantity) + " at $" + str(dbFetch[2]) + priceIncrement)
               
               invoicePriceOutput.insert("end", "-$" + str(dbFetch[2]*float(quantity)))
               invoicePriceOutput.itemconfig(invoiceOutput.size()-1, {'fg':'red'})
               invoiceOutput.itemconfig(invoiceOutput.size()-1, {'fg':'red'})
               
               quantity=1.0
               printText("Please Scan Another Barcode to continue", 0)

            if state=='Void':
               VoidMode()

            else:
               InvoiceMode()
         
         
   elif (state=='Weigh Item'):
      quantity=inputMain
      
      if (check_float(quantity)==True):

         quantity = float((inputMain))
         if stateholder=='Void':
            VoidMode()

         else:
            InvoiceMode()

         c.execute("SELECT * FROM allItemsAndCodes WHERE barcode =?", [barcodeHolder])
         dbFetch = c.fetchone()
        
         priceIncrement = " per kilo"



         if (stateholder != 'Void'):

            print(dbFetch)
            cartPrice = float(cartPrice)+float(dbFetch[2]*quantity)
            cartQuantity.append(quantity)
            invoiceOutput.insert("end", str(dbFetch[1]) + " x " + str(quantity) + "kg at $" + str(dbFetch[2]) + priceIncrement)
            invoicePriceOutput.insert("end", "$" + str(dbFetch[2]*float(quantity)))

            quantity=1.0
            printText("Please Scan Another Barcode to continue", 0)


         else:
            cartPrice = float(cartPrice)-float(dbFetch[2]*quantity)
            cartQuantity.append(-1*quantity)
            
            invoiceOutput.insert("end", "-" + str(dbFetch[1]) + " x " + str(quantity) + "kg at $" + str(dbFetch[2]) + priceIncrement)
            
            invoicePriceOutput.insert("end", "-$" + str(dbFetch[2]*float(quantity)))
            invoicePriceOutput.itemconfig(invoiceOutput.size()-1, {'fg':'red'})
            invoiceOutput.itemconfig(invoiceOutput.size()-1, {'fg':'red'})
            
            quantity=1.0
            printText("Please Scan Another Barcode to continue", 0)


         

      else:
         printText("Enter a valid weight", 0)

         
      
         
         
   

        
         

   else:
      printText("Not Invoice State",0)
      if stateholder=='Void':
            VoidMode()

      else:
         InvoiceMode()


   updateSubtotal()

def alternateKeyboard(self):
   global keybaord
   if keybaord == 1:
      keybaord = 0
      entryInput.delete(0, END)
      entryInput.config(state=DISABLED)
   else:
      keybaord = 1
      entryInput.delete(0, END)
      entryInput.config(state=NORMAL)

def startRoot():
   #tkinter window
   global keybaord
   global root
   global voidmode
   global stateholder
   global employeeNumber
   keybaord = 1
   stateholder = 'Invoice'
   root = Tk()
   root.geometry("1600x900")
   root.title(versionName)


   #variables
   voidmode=IntVar()
  


   #menubar
   mainMenubar()
   #widgets
   entryWidgets()
   widgets()
   #Display Time
   displayTimeAndDate()
   #set state
   changeState("Invoice")
   #set textbox
   printText("Scan Barcode to Begin", 0)
   #set subtotal to 0
   entryOutput.config(state=NORMAL)
   entryOutput.delete(0, END)
   entryOutput.insert(1, 0)






   

 







   root.bind("<Return>", getInput)
   root.bind("<\\>", alternateMode)
   root.bind("<`>", alternateKeyboard)
   root.bind("<C>", cashPayment)
   root.bind("<E>", eftposPayment)
   root.bind("<A>", accountPayment)
   root.bind("<M>", memberpointsPayment)
   root.bind("<G>", giftcardPayment)
   root.bind("<P>", reprintLast)
   root.bind("<c>", cashPayment)
   root.bind("<e>", eftposPayment)
   root.bind("<a>", accountPayment)
   root.bind("<m>", memberpointsPayment)
   root.bind("<g>", giftcardPayment)
   root.bind("<p>", reprintLast)
   root.bind("<Control_L>", startLoginKeybind)






   root.mainloop()


startRoot()






















