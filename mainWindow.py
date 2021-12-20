from tkinter import *
import sqlite3
import time as tm

conn = sqlite3.connect('PerkinPOSDatabase')
c= conn.cursor()
global companyName
global focus
global enterCount
companyName = "POS Test 2.2"
focus = 0
enterCount = 0


	


	



class mainWindow:

	class windowSetup:
		def __init__(self, master):

			master.title(companyName)
			master.attributes('-fullscreen',False)
			master.resizable(height = False, width = False)
			master.geometry("0x0")

	class menubarSetup:
		def __init__(self, master):
			self.menubar = Menu(master)
			self.systemmenu = Menu(self.menubar, tearoff=0)
			self.systemmenu.add_command(label="Invoice", command=mainWindow.bindMinus, state = ACTIVE, accelerator="-")
			self.systemmenu.add_command(label="Void", command=mainWindow.bindMinus, state=ACTIVE, accelerator=('-'))
			self.systemmenu.add_command(label="Price & Quantity Check", command=mainWindow.donothing, state=DISABLED)
			
			self.systemmenu.add_separator()
			self.systemmenu.add_command(label="Logout", command=mainWindow.logout, state=ACTIVE)
			self.systemmenu.add_command(label="Exit", command=mainWindow.close, accelerator="Cmd+Q")
			self.menubar.add_cascade(label="System", menu=self.systemmenu)

			self.modifymenu = Menu(self.menubar, tearoff=0)
			self.modifymenu.add_command(label="Void", command=mainWindow.bindMinus, state=ACTIVE, accelerator='-')
			self.modifymenu.add_command(label="Void All", command=mainWindow.donothing, state=DISABLED, accelerator='+')
			self.modifymenu.add_separator()
			self.modifymenu.add_command(label="Change Qty", command=mainWindow.donothing, state=DISABLED, accelerator='*')
			self.modifymenu.add_command(label="Markdown", command=mainWindow.donothing, state=DISABLED, accelerator='/')
			self.modifymenu.add_command(label="Reset", command=mainWindow.donothing, state=DISABLED)
			self.menubar.add_cascade(label="Modify", menu=self.modifymenu)

			self.managermenu = Menu(self.menubar, tearoff=0)
			self.managermenu.add_command(label="Z-Report", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="X-Report", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Tender Declaration", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Remove Tender", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_separator()
			self.managermenu.add_command(label="Employees On Register", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Cash In Drawer", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_separator()
			self.managermenu.add_command(label="Training Mode", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Vending Machine Sales", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Open Key", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Epay", command=mainWindow.donothing, state=DISABLED)
			self.managermenu.add_command(label="Epay Refund", command=mainWindow.donothing, state=DISABLED)



			self.menubar.add_cascade(label="Manager Menu", menu=self.managermenu)

			self.databasemenu = Menu(self.menubar, tearoff=0)
			self.menubar.add_cascade(label="Database", menu=self.databasemenu)


			self.itemsmenu = Menu(self.databasemenu, tearoff = 0)
			self.databasemenu.add_cascade(label="Items", menu = self.itemsmenu)
			self.itemsmenu.add_command(label="Add Item", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_command(label="Remove Item", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_separator()
			self.itemsmenu.add_command(label="Change Item PLU", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_command(label="Change Item Description", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_command(label="Change Item Price", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_command(label="Change Item Price Increment", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_separator()
			self.itemsmenu.add_command(label="Set Stock", command =mainWindow.donothing, state = DISABLED)
			self.itemsmenu.add_command(label="Add Stock", command =mainWindow.donothing, state = DISABLED)


			self.accountsmenu=Menu(self.databasemenu, tearoff=0)
			self.databasemenu.add_cascade(label="Accounts", menu=self.accountsmenu)
			self.accountsmenu.add_command(label="Add Account", command=mainWindow.donothing, state=DISABLED)
			self.accountsmenu.add_command(label="Remove Account", command=mainWindow.donothing, state=DISABLED)
			self.accountsmenu.add_separator()
			self.accountsmenu.add_command(label="Change Account Number", command=mainWindow.donothing, state=DISABLED)
			self.accountsmenu.add_command(label="Change Account Name", command=mainWindow.donothing, state=DISABLED)
			self.accountsmenu.add_separator()
			self.accountsmenu.add_command(label="Set Account Balance", command=mainWindow.donothing, state=DISABLED)
			self.accountsmenu.add_command(label="Add Money to Balance", command=mainWindow.donothing, state=DISABLED)


			self.rewardsmenu=Menu(self.databasemenu, tearoff=0)
			self.databasemenu.add_cascade(label="Rewards", menu=self.rewardsmenu)
			self.rewardsmenu.add_command(label="Register Rewards Card", command=mainWindow.donothing, state=DISABLED)
			self.rewardsmenu.add_command(label="Deregister Rewards Card", command=mainWindow.donothing, state=DISABLED)
			self.rewardsmenu.add_separator()
			self.rewardsmenu.add_command(label="Change Rewards Card Number", command=mainWindow.donothing, state=DISABLED)
			self.rewardsmenu.add_command(label="Change Rewards Card Name", command=mainWindow.donothing, state=DISABLED)
			self.rewardsmenu.add_separator()
			self.rewardsmenu.add_command(label="Set Reward Points", command=mainWindow.donothing, state=DISABLED)
			self.rewardsmenu.add_command(label="Add Reward Points", command=mainWindow.donothing, state=DISABLED)

			self.databasemenu.add_separator()
			self.employeemenu=Menu(self.databasemenu, tearoff=0)
			self.databasemenu.add_cascade(label="Employee", menu=self.employeemenu)
			self.employeemenu.add_command(label="Register Employee", command=mainWindow.donothing, state=DISABLED)
			self.employeemenu.add_command(label="Deregister Employee", command=mainWindow.donothing, state=DISABLED)
			self.employeemenu.add_separator()
			self.employeeinfomenu=Menu(self.employeemenu, tearoff=0)
			self.employeemenu.add_cascade(label="Edit Employee Info", menu=self.employeeinfomenu)
			self.employeeinfomenu.add_command(label="Employee Number", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Name", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Email", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Phone Number", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Date of Birth", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Address Line 1", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Address Line 2", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_command(label="Rank Name", command=mainWindow.donothing, state=DISABLED)
			self.employeeinfomenu.add_separator()
			self.employeeinfomenu.add_command(label="Edit All", command=mainWindow.donothing, state=DISABLED)
			self.employeemenu.add_command(label="Edit Employee Permissions", command=mainWindow.donothing, state=DISABLED)

			self.databasemenu.add_command(label="Settings", command=mainWindow.donothing, state=DISABLED)

			self.supliermenu=Menu(self.menubar, tearoff=0)
			self.menubar.add_cascade(label="Supplier", menu=self.supliermenu)
			self.supliermenu.add_command(label="Order Products", command=mainWindow.donothing, state=DISABLED)
			master.config(menu=self.menubar)
	class widgets:
		def __init__(self, master):
			self.master=master
			Label(master, text = companyName, font=("Arial", 50)).place(anchor=W, relx=0.01, rely=0.03)
			
			Label(master, text = "Description", font=("Arial", 25)).place(anchor=W, relx=0.01, rely=0.08)
			Label(master, text = "Price", font=("Arial", 25)).place(anchor=W, relx=0.74 , rely=0.08)
			Label(master, text = "Total: $", font=("Arial", 30)).place(anchor=W, relx=0.675 , rely=0.88)

			Label(master, text = "State", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.03)
			Label(master, text = "Employee", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.13)
			Label(master, text = "Manager", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.23)
			Label(master, text = "Rewards Value", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.33)
			Label(master, text = "Account Value", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.43)
			Label(master, text = "Date", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.63)
			Label(master, text = "Time", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.73)
			Label(master, text = "Sales Count", font=("Arial", 25)).place(anchor=CENTER, relx=0.93, rely=0.53)

			self.stateEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.stateEntry.place(anchor=CENTER, relx = 0.93, rely=0.07)
			self.employeeEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.employeeEntry.place(anchor=CENTER, relx = 0.93, rely=0.17)
			self.managerEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.managerEntry.place(anchor=CENTER, relx = 0.93, rely=0.27)
			self.rewardsEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.rewardsEntry.place(anchor=CENTER, relx = 0.93, rely=0.37)
			self.accountEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.accountEntry.place(anchor=CENTER, relx = 0.93, rely=0.47)
			self.salesEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.salesEntry.place(anchor=CENTER, relx = 0.93, rely=0.57)
			self.dateEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.dateEntry.place(anchor=CENTER, relx = 0.93, rely=0.67)
			self.timeEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER)
			self.timeEntry.place(anchor=CENTER, relx = 0.93, rely=0.77)

			self.displayTimeAndDate()

			self.logoutButton = Button(text="Logout", font=("Arial", 45), height = 3, width =6, command=lambda i =self, j=master:mainWindow.logout(i, j))
			self.logoutButton.place(anchor=SW, relx = 0.875, rely = 0.99)

			self.subtotal=Entry(master, font=("Arial", 30), width=11)
			self.subtotal.place(anchor=W, relx=0.7425, rely=0.88)

			self.listboxDescription = Listbox(master, width = 101, height=32, font=("Arial", 20))
			self.listboxDescription.place(anchor=NW, relx=0.01, rely=0.1)
			self.listboxPrice = Listbox(master, width = 17, height=32, font=("Arial", 20))
			self.listboxPrice.place(anchor=NW, relx=0.74, rely=0.1)

			self.textbox1 = Text(master, width = 90, height = 4, font = ("Arial", 20))
			self.textbox1.place(anchor=W, relx = 0.01, rely=0.885)



			self.inputEntry = Entry(master, width=62, font=("Arial", 40))
			self.inputEntry.place(anchor=SW, relx=0.01, rely = 0.99)

		def displayTimeAndDate(self):
			currentTime= tm.strftime('%H:%M:%S')
			self.timeEntry.config(state=NORMAL, justify = CENTER)
			self.timeEntry.delete(0, END)
			self.timeEntry.insert(1, str(currentTime))
			self.timeEntry.config(state=DISABLED)
			self.dateEntry.config(state=NORMAL, justify = CENTER)
			self.dateEntry.delete(0, END)
			self.dateEntry.insert(1, tm.strftime('%x'))
			self.dateEntry.config(state=DISABLED)
			self.master.after(1000, self.displayTimeAndDate)
	def __init__(self, master):
		self.master = master
		self.windowSetupVar = self.windowSetup(master)
		self.menubarSrtupVar = self.menubarSetup(master)
		self.widgetsVar = self.widgets(master)
		self.changeState('Invoice')

		self.totalPrice = 0
		self.widgetsVar.subtotal.insert(0, self.totalPrice)
		self.printText("Scan Barcode To Begin")

		self.cartbarcode = []
		self.cartquantity = []
		self.returnCount = 0




		master.bind("<Return>", lambda a:self.bindReturn())
		master.bind("</>", lambda b:self.bindDivide())
		master.bind("<*>", lambda c:self.bindMultiply())
		master.bind("<minus>", lambda e: self.bindMinus())
		master.bind("<+>", lambda d:self.bindAdd())


	  

	def changeState(self, statea):
		global state
		state = statea
		self.widgetsVar.stateEntry.config(state=NORMAL)
		self.widgetsVar.stateEntry.delete(0, END)
		self.widgetsVar.stateEntry.insert(0, state)
		self.widgetsVar.stateEntry.config(state=DISABLED)
		print(state)

	def check_float(self, potential_float):
	    try:
	        float(potential_float)

	        return True
	    except ValueError:
	        return False


	def printText(self, text):

		self.widgetsVar.textbox1.config(state=NORMAL)
		self.widgetsVar.textbox1.delete(1.0, END)


		self.widgetsVar.textbox1.insert(1.0, text+"\n")


		self.widgetsVar.textbox1.config(state=DISABLED)  

	def close(self):
		quit()

	def donothing(self):
		print("Nothing Has been done")
		return None

	def logout(self, master):
		master.destroy()	

	def bindReturn(self):
		if self.returnCount == 1:
			self.changeState("Payment")
			self.returnCount = 0
			self.printText("Payment State - Enter number and then hit any of the following keys:\n/ :Cash\n* :Eftpos\n- :Customer Accounts \n+ :Rewards Points")

		else:

		
			self.widgetsVar.inputEntry.focus()
			self.conn = sqlite3.connect('PerkinPOSDatabase')
			self.c = self.conn.cursor()

			self.input = self.widgetsVar.inputEntry.get()
			self.widgetsVar.inputEntry.delete(0, END)
			print(self.input)

			self.c.execute("SELECT * from allItemsAndCodes WHERE barcode = ?", [self.input])
			self.dbFetch=self.c.fetchone()

			if state == "Invoice":

				if self.dbFetch == None:
					print("No Barcode Found")
					self.returnCount = self.returnCount + 1

				else:
					if self.dbFetch[3] == 1:
						self.priceIncrement = " each"
					else:
						self.priceIncrement = " per kilo"

					self.cartbarcode.append(self.dbFetch[0])
					self.cartquantity.append(1)
					self.totalPrice = self.totalPrice + self.dbFetch[2]
					self.widgetsVar.listboxDescription.insert("end", str(self.dbFetch[1]) + " x 1 @ $" + str(self.dbFetch[2]) + str(self.priceIncrement))
					self.widgetsVar.listboxPrice.insert("end", "$"+str(self.dbFetch[2]))
					self.widgetsVar.subtotal.delete(0, END)
					self.widgetsVar.subtotal.insert(0, self.totalPrice)
					print(state)

			elif state == "Void":
				if self.dbFetch == None:
					print("No Barcode Found")
					self.returnCount = self.returnCount + 1

				else:
					if self.dbFetch[3] == 1:
						self.priceIncrement = " each"
					else:
						self.priceIncrement = " per kilo"


					self.cartbarcode.append(self.dbFetch[0])
					self.cartquantity.append(-1)
					self.totalPrice = self.totalPrice - self.dbFetch[2]
					self.widgetsVar.listboxDescription.insert("end", str(self.dbFetch[1]) + " x -1 @ $" + str(self.dbFetch[2]) + str(self.priceIncrement))
					self.widgetsVar.listboxPrice.insert("end", "-$"+str(self.dbFetch[2]))
					self.widgetsVar.listboxDescription.itemconfig(self.widgetsVar.listboxDescription.size()-1, {'fg':'red'})
					self.widgetsVar.listboxPrice.itemconfig(self.widgetsVar.listboxPrice.size()-1, {'fg':'red'})
					self.widgetsVar.subtotal.delete(0, END)
					self.widgetsVar.subtotal.insert(0, self.totalPrice)
			elif state=="Payment":
				self.printText("Scan Barcode")
				self.changeState("Invoice")
			
			

		return None


	def bindMinus(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)
		if state == "Invoice":

			self.changeState("Void")
		elif state == "Void":
			self.changeState("Invoice")
		return None

	def bindDivide(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)
		if state == "Payment":
			if self.check_float(self.widgetsVar.inputEntry.get()) == True:
				
				self.printText("Order Proccessed. Price came to $" + str(self.widgetsVar.subtotal.get()) + "\nCash Back: $"+ str(float(self.widgetsVar.inputEntry.get())-float(self.widgetsVar.subtotal.get())))


			else:
			
				self.printText("Order Proccessed. Price came to $" + str(self.widgetsVar.subtotal.get()))
				

			self.conn = sqlite3.connect('PerkinPOSDatabase')
			self.c= self.conn.cursor()

			self.i = 0
			self.changeState("Invoice")
			while self.i < len(self.cartbarcode):
				
				self.c.execute('SELECT * from allItemsAndCodes where barcode = ?', [str(self.cartbarcode[self.i])])
				
				self.quantity = self.c.fetchone()
				self.c.execute('UPDATE allItemsAndCodes SET quantityInStock = ? WHERE barcode = ?', [self.quantity[4] - self.cartquantity[self.i], self.cartbarcode[self.i]])
				
				self.i = self.i+1
				self.conn.commit()


			self.widgetsVar.listboxDescription.delete(0, END)
			self.widgetsVar.listboxPrice.delete(0, END)
			self.widgetsVar.subtotal.delete(0, END)
			self.widgetsVar.subtotal.insert(0, 0)
			self.widgetsVar.inputEntry.delete(0, END)



		return None

	def binkMultiply(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)
		return None



	
		


class loginWindowClass:
	def __init__(self, master):
		self.loginWindow = Toplevel(master)
		self.master=master
		self.loginWindow.title("Login")
		self.loginWindow.geometry("500x500")
		self.loginWindow.resizable(height = False, width = False)

		self.label1=Label(self.loginWindow, text="Enter Employee Number", font=("Arial", 20))
		self.label1.place(anchor=CENTER, relx = 0.5, rely=0.3)

		self.entry1 = Entry(self.loginWindow, width=45, font=("{Times New Roman}", 15))
		self.entry1.place(anchor=CENTER, relx=0.5, rely = 0.38)
		self.entry1.focus()


		self.loginButton = Button(self.loginWindow, text="Login",font=("Arial", 15), command=lambda: self.login(master, self.entry1))
		self.loginButton.place(anchor=CENTER, relx=0.5, rely=0.45)

		self.destroyLogin = Button(self.loginWindow, text="EXIT",font=("Arial, 25"), command=lambda i=master: self.close(i))
		self.destroyLogin.place(anchor=CENTER, relx=0.5, rely=0.9)

		self.loginWindow.bind("<Return>", lambda i=master, j=self.entry1:self.login(i, j))
		

	def login(self, master, entryInputs):
		


		c.execute('SELECT employeeNumber FROM employees WHERE employeeNumber = ?', [entryInputs.get()])
		self.dbFetch = c.fetchone()

		if self.dbFetch ==None:
			print("No Such Employee")
			entryInputs.delete(0, END)



		else:
			
			self.loginWindow.destroy()
			self.master.deiconify()
			self.master.attributes('-fullscreen',True)
			self.entry = mainWindowwindow.widgetsVar.inputEntry
			self.entry.focus()
			


		return None

	def close(self, master):
		quit()

def start():
	x =1 
	global voidmode
	global mainWindowwindow
	root = Tk()
	voidmode = IntVar()
	initialLogin=loginWindowClass(root)
	
	root.withdraw()
	mainWindowwindow = mainWindow(root)
	root.mainloop()
	return None























