from tkinter import *
from MenuBarFunctions import *
#function
def mainMenubar():
   menubar = Menu(root)
   systemmenu = Menu(menubar, tearoff=0)
   systemmenu.add_command(label="Invoice", command=donothing, state = DISABLED)
   systemmenu.add_command(label="Price & Quantity Check", command=donothing, state=DISABLED)
   systemmenu.add_command(label="Refund", command=donothing, state=DISABLED)
   systemmenu.add_separator()
   systemmenu.add_command(label="Logout", command=donothing, state=DISABLED)
   systemmenu.add_command(label="Exit", command=root.quit, accelerator="Cmd+Q")
   menubar.add_cascade(label="System", menu=systemmenu)

   modifymenu = Menu(menubar, tearoff=0)
   modifymenu.add_command(label="Void", command=donothing, state=DISABLED)
   modifymenu.add_command(label="Void All", command=donothing, state=DISABLED)
   modifymenu.add_separator()
   modifymenu.add_command(label="Change Qty", command=donothing, state=DISABLED)
   modifymenu.add_command(label="Markdown", command=donothing, state=DISABLED)
   modifymenu.add_command(label="Reset", command=donothing, state=DISABLED)
   menubar.add_cascade(label="Modify", menu=modifymenu)

   managermenu = Menu(menubar, tearoff=0)
   managermenu.add_command(label="Z-Report", command=donothing, state=DISABLED)
   managermenu.add_command(label="X-Report", command=donothing, state=DISABLED)
   managermenu.add_command(label="Cash In Drawer", command=donothing, state=DISABLED)
   managermenu.add_command(label="Tender Declaration", command=donothing, state=DISABLED)
   managermenu.add_command(label="Employees On Register", command=donothing, state=DISABLED)
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

   root.config(menu=menubar)

def voidmodefunc():
   print(voidmode.get())

def tkWidgets():
   #entryboxes
   entryInput = Entry(root, width=75, font=("Arial", 25))
   entryInput.grid(column=0, row=1, columnspan=9, sticky=NW, padx=5, pady=0)
   entryOutput=Entry(root, width=15, font=("Arial",15))
   entryOutput.grid(column=10, row=3, sticky=E, pady=5, rows=2)

   entry4=Entry(root,width=11, font=("Arial",15))
   entry4.grid(column=0, row=4)
   entry5=Entry(root,width=11, font=("Arial",15))
   entry5.grid(column=1, row=4)
   entry6=Entry(root,width=11, font=("Arial",15))
   entry6.grid(column=2, row=4)
   entry7=Entry(root,width=11, font=("Arial",15))
   entry7.grid(column=3, row=4)
   entry8=Entry(root,width=11, font=("Arial",15))
   entry8.grid(column=4, row=4)
   entry9=Entry(root,width=11, font=("Arial",15))
   entry9.grid(column=5, row=4)
   entry10=Entry(root,width=11, font=("Arial",15))
   entry10.grid(column=6, row=4)
   entry11=Entry(root,width=11, font=("Arial",15))
   entry11.grid(column=7, row=4)
   entry12=Entry(root,width=11, font=("Arial",15))
   entry12.grid(column=8, row=4)

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
   textbox1=Text(root, width=150, height=57)
   textbox1.grid(row=1, column=0, sticky=S, columnspan=9, rows=2)

def startRoot():
   #tkinter window
   global root
   global voidmode
   root = Tk()
   root.geometry("1600x900")
   root.title("PerkinsPOSTest-2.0")
   voidmode=IntVar()
   

   mainMenubar()

   #widgets
   tkWidgets()


      




      

   root.mainloop()