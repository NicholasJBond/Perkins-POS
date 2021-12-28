from tkinter import *
import sqlite3
import time as tm
import sys

conn = sqlite3.connect('PerkinPOSDatabase')
c= conn.cursor()
global companyName
global focus
global enterCount
companyName = "POS Test 2.4"
focus = 0
enterCount = 0

class mainWindow:

	class windowSetup:
		def __init__(self, master):

			master.title(companyName)
			master.resizable(height = False, width = False)
			master.geometry("1000x1000")
			

	class menubarSetup:
		def __init__(self, master):
			self.menubar = Menu(master)
			self.systemmenu = Menu(self.menubar, tearoff=0)
			self.systemmenu.add_command(label="Price & Quantity Check", command=mainWindow.donothing, state=DISABLED)
			
			self.systemmenu.add_separator()
			self.systemmenu.add_command(label="Logout", command=mainWindow.logout, state=ACTIVE)
			self.systemmenu.add_command(label="Exit", command=mainWindow.close, accelerator="Cmd+Q")
			self.menubar.add_cascade(label="System", menu=self.systemmenu)

			self.modifymenu = Menu(self.menubar, tearoff=0)
			self.modifymenu.add_command(label="Void Last", command=mainWindow.donothing, state=DISABLED)
			self.modifymenu.add_command(label="Change Qty", command=mainWindow.donothing, state=DISABLED, accelerator='*')
			self.modifymenu.add_command(label="Markdown", command=mainWindow.donothing, state=DISABLED, accelerator='/')
			self.modifymenu.add_command(label="Suspend", command=mainWindow.donothing, state=DISABLED)
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
			Label(master, text = "Amount", font=("Arial", 25)).place(anchor=W, relx=0.74 , rely=0.08)
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
			self.managerEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER, state = DISABLED)
			self.managerEntry.place(anchor=CENTER, relx = 0.93, rely=0.27)
			self.rewardsEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER, state = DISABLED)
			self.rewardsEntry.place(anchor=CENTER, relx = 0.93, rely=0.37)
			self.accountEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER, state = DISABLED)
			self.accountEntry.place(anchor=CENTER, relx = 0.93, rely=0.47)
			self.salesEntry = Entry(master, width=12, font=("Arial", 25), justify=CENTER, state = DISABLED)
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
		self.loginPage = loginWindowClass(master)
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
		self.cartPrice=[]
		self.returnCount = 0

		self.employee = self.loginPage.employeenum


		



		master.bind("<Return>", lambda a:self.bindReturn(master))
		master.bind("<KP_Enter>", lambda a:self.bindReturn(master))
		master.bind("<KP_Divide>", lambda b:self.bindDivide())
		master.bind("<KP_Multiply>", lambda b:self.bindMultiply())
		master.bind("<KP_Add>", lambda b:self.bindAdd())

	def changeState(self, statea):
		global state
		state = statea
		self.widgetsVar.stateEntry.config(state=NORMAL)
		self.widgetsVar.stateEntry.delete(0, END)
		self.widgetsVar.stateEntry.insert(0, state)
		self.widgetsVar.stateEntry.config(state=DISABLED)
		

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

	def close():
		
		quit()

	def donothing(self):
		print("Nothing Has been done")
		return None

	def logout(self, master):
		master.destroy()

	def bindReturn(self, master):
		
		self.priceList = self.widgetsVar.listboxPrice
		self.itemList = self.widgetsVar.listboxDescription
		self.totalPrice2 = "${:,.2f}".format(float(self.totalPrice))	

		if self.widgetsVar.inputEntry.get() == "000":
			self.logout(master)

		elif self.widgetsVar.inputEntry.get() == "000000":
			self.helpWindow = helpWindowClass(self.master)
			

			self.widgetsVar.inputEntry.delete(0, END)
		else:

			if state=="Payment":
				self.printText("Scan Barcode")
				self.changeState("Invoice")
				self.returnCount = 0

			elif self.returnCount == 1 and self.widgetsVar.inputEntry.get()=="":
				self.changeState("Payment")
				self.returnCount = 0
				self.printText("Payment State:\n/ :Cash")

			else:

				self.printText("Scan Barcode\n/: Markdown\n*: Change Qty")
				self.widgetsVar.inputEntry.focus()
				self.conn = sqlite3.connect('PerkinPOSDatabase')
				self.c = self.conn.cursor()

				self.input = self.widgetsVar.inputEntry.get()
				self.widgetsVar.inputEntry.delete(0, END)
				

				self.c.execute("SELECT * from allItemsAndCodes WHERE barcode = ?", [self.input])
				self.dbFetch=self.c.fetchone()

				if self.input== "":
					self.returnCount = self.returnCount + 1

				else:
					if state == "Invoice":
						self.returnCount = 0

						if self.dbFetch == None:
							self.printText("No Barcode Found")

						else:
							
							
							self.i = 0
							self.end = 0
							
							while self.i <= len(self.cartbarcode) and self.end == 0:
								try:
									if self.cartbarcode[self.i] == self.input:
										
										self.end = 1
										self.itemList.delete(self.i)
										self.priceList.delete(self.i)

										if self.cartquantity[self.i] != -1:

											self.tempPrice = self.cartPrice[self.i]/self.cartquantity[self.i]
											self.totalPrice = self.totalPrice - self.cartPrice[self.i]
											self.cartbarcode.append(self.dbFetch[0])
											self.cartquantity.append(self.cartquantity[self.i]+1)
											self.cartPrice.append(self.tempPrice*self.cartquantity[self.cartquantity[self.i]])
											

											self.cartbarcode.pop(self.i)
											self.cartquantity.pop(self.i)
											self.cartPrice.pop(self.i)




											
											self.totalPrice = self.totalPrice + self.tempPrice*self.cartquantity[self.i]
											if self.dbFetch[3] == 1:
												self.outputText = str(self.dbFetch[1]) + " x "+str(self.cartquantity[len(self.cartquantity)-1]) +" @ " + "${:,.2f}".format(float(self.tempPrice)) + " each"
											else:
												self.outputText = str(self.dbFetch[1]) + " x "+str(self.cartquantity[len(self.cartquantity)-1]) +"kg @ " + "${:,.2f}".format(float(self.tempPrice)) + " per kilo"


											self.widgetsVar.listboxDescription.insert(END, self.outputText)
											self.widgetsVar.listboxPrice.insert("end", "${:,.2f}".format(float(self.tempPrice*self.cartquantity[len(self.cartquantity)-1])))

											if self.cartquantity[self.i] < 0:
												self.widgetsVar.listboxDescription.itemconfig(self.widgetsVar.listboxDescription.size()-1, {'fg':'red'})
												self.widgetsVar.listboxPrice.itemconfig(self.widgetsVar.listboxPrice.size()-1, {'fg':'red'})

										else:
											self.cartbarcode.pop(self.i)
											self.cartquantity.pop(self.i)
											self.totalPrice = self.totalPrice + self.dbFetch[2]
											self.cartPrice.append(self.dbFetch[2])

											


									else:
										self.i = self.i + 1

								except IndexError:

									if self.dbFetch[3] == 1:
										self.outputText = str(self.dbFetch[1]) + " x 1"+ " @ " + "${:,.2f}".format(float(self.dbFetch[2])) + " each"
									else:
										self.outputText = str(self.dbFetch[1]) + " x 1"+ "kg @ " + "${:,.2f}".format(float(self.dbFetch[2])) + " per kilo"

									self.end = 1
									self.cartbarcode.append(self.dbFetch[0])
									self.cartquantity.append(1)
									self.totalPrice = self.totalPrice + self.dbFetch[2]

									self.widgetsVar.listboxDescription.insert("end", self.outputText)
									self.widgetsVar.listboxPrice.insert("end", "${:,.2f}".format(float(self.dbFetch[2])))
									self.cartPrice.append(self.dbFetch[2])
									


					

					
			self.widgetsVar.subtotal.delete(0, END)
			self.widgetsVar.subtotal.insert(0, "{:,.2f}".format(float(self.totalPrice)))	

	def bindDivide(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)
		if state == "Payment":
			if self.check_float(self.widgetsVar.inputEntry.get()) == True:
				
				self.printText("Order Proccessed. Price came to " + str(self.totalPrice2) + "\nCash Back: "+ "${:,.2f}".format(float(self.widgetsVar.inputEntry.get())-float(self.totalPrice)))


			else:
				
				if self.totalPrice < 0:
					self.printText("Order Proccessed. Price came to " + str(self.totalPrice2) + "\nCash Back: "+ "${:,.2f}".format(float(float(self.totalPrice)*-1)))
				else:
					self.printText("Order Proccessed. Price came to " + str(self.totalPrice2))
				

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
			print("Cart Items:")
			print(self.cartbarcode)
			print(self.cartquantity)
			print("-------------")
			self.cartbarcode = []
			self.cartquantity = []
			self.totalPrice = 0

			self.widgetsVar.listboxDescription.delete(0, END)
			self.widgetsVar.listboxPrice.delete(0, END)
			self.widgetsVar.subtotal.delete(0, END)
			self.widgetsVar.subtotal.insert(0, 0)
			self.widgetsVar.inputEntry.delete(0, END)

		elif state == "Invoice":
			if self.check_float(self.widgetsVar.inputEntry.get())==True:

				if self.cartbarcode != []:

					if float(self.widgetsVar.inputEntry.get()) > float(self.cartPrice[len(self.cartPrice)-1]):
						self.printText("Scan Barcode\n/: Markdown\n*: Change Qty\nWARNING: Price is higher than before")



					self.totalPrice = self.totalPrice - float(self.cartPrice[len(self.cartPrice)-1])
					self.cartPrice[len(self.cartPrice)-1] = self.widgetsVar.inputEntry.get()
					self.totalPrice = float(self.totalPrice) + float(self.cartPrice[len(self.cartPrice)-1])

					if self.dbFetch[3] == 1:
						self.outputText = str(self.dbFetch[1]) + " x "+str(self.cartquantity[len(self.cartquantity)-1]) +" @ " + "${:,.2f}".format(float(self.widgetsVar.inputEntry.get())) + " each"
					else:
						self.outputText = str(self.dbFetch[1]) + " x "+str(self.cartquantity[len(self.cartquantity)-1]) +"kg @ " + "${:,.2f}".format(float(self.widgetsVar.inputEntry.get())) + " per kilo"

					self.priceList.delete(END)
					self.priceList.insert(END, "${:,.2f}".format(self.cartquantity[len(self.cartquantity)-1]*float(self.widgetsVar.inputEntry.get())))
					self.itemList.delete(END)
					self.itemList.insert(END, self.outputText)


					self.widgetsVar.subtotal.delete(0, END)
					self.widgetsVar.subtotal.insert(0, "{:,.2f}".format(float(self.totalPrice)))	
					self.widgetsVar.inputEntry.delete(0, END)
				
			else:
				print("Invalid amount")

		return None

	def bindMultiply(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)

		if state == "Invoice":
			if self.check_float(self.widgetsVar.inputEntry.get()) == True:
				if self.cartbarcode != []:

					self.newQuantity = self.widgetsVar.inputEntry.get()
					self.widgetsVar.inputEntry.delete(0, END)

					self.c.execute("SELECT * FROM allItemsAndCodes where barcode = ?", [self.cartbarcode[len(self.cartbarcode)-1]])
					self.dbFetch=self.c.fetchone()

					self.tempPrice = float(self.cartPrice[len(self.cartPrice)-1])/float(self.cartquantity[len(self.cartquantity)-1])
					self.totalPrice=float(self.totalPrice)-float(self.cartPrice[len(self.cartPrice)-1])
					self.cartquantity[len(self.cartquantity)-1] = float(self.newQuantity)
					self.cartPrice[len(self.cartPrice)-1] = (self.cartquantity[len(self.cartquantity)-1]*self.tempPrice)
					

					
					


					self.i = 0
					
					self.totalPrice=self.totalPrice+(self.cartquantity[len(self.cartquantity)-1]*self.tempPrice)
					
					self.widgetsVar.subtotal.delete(0, END)
					self.widgetsVar.subtotal.insert(0, self.totalPrice)

					if self.dbFetch[3] == 1:
						self.outputText = str(self.dbFetch[1]) + " x "+str(self.newQuantity) +" @ " + "${:,.2f}".format(float(self.tempPrice)) + " each"
					else:
						self.outputText = str(self.dbFetch[1]) + " x "+str(self.newQuantity) +"kg @ " + "${:,.2f}".format(float(self.tempPrice)) + " per kilo"


					self.widgetsVar.listboxDescription.delete(END)
					self.widgetsVar.listboxPrice.delete(END)

					self.widgetsVar.listboxDescription.insert("end", self.outputText)
					self.widgetsVar.listboxPrice.insert("end", "${:,.2f}".format(self.cartquantity[len(self.cartquantity)-1]*self.tempPrice))
					
					if self.cartquantity[len(self.cartquantity)-1] < 0:
						self.widgetsVar.listboxDescription.itemconfig(self.widgetsVar.listboxDescription.size()-1, {'fg':'red'})
						self.widgetsVar.listboxPrice.itemconfig(self.widgetsVar.listboxPrice.size()-1, {'fg':'red'})

			else:
				print("Enter a valid quantity")
		

		else:
			print("Eftpos Not Implemented Yet")

		self.widgetsVar.subtotal.delete(0, END)
		self.widgetsVar.subtotal.insert(0, "{:,.2f}".format(float(self.totalPrice))	)

	def bindAdd(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)
		return None










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
		self.loginWindow.bind("<KP_Enter>", lambda i=master, j=self.entry1:self.login(i, j))
		self.employeenum=5

		

	def login(self, master, entryInputs):
		if entryInputs.get() == "000":
				self.close(master)
		
		c.execute('SELECT * FROM settings WHERE settingName = ?', ["Default Employee Number"])
		if c.fetchone() == 0:

			c.execute('SELECT * FROM employees WHERE employeeNumber = ?', [entryInputs.get()])
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
				
				self.employeenum=self.dbFetch[0]+" "+self.dbFetch[1][0]
				mainWindowwindow.widgetsVar.employeeEntry.config(state=NORMAL)
				mainWindowwindow.widgetsVar.employeeEntry.delete(0, END)

				mainWindowwindow.widgetsVar.employeeEntry.insert(0, self.employeenum)
				mainWindowwindow.widgetsVar.employeeEntry.config(state=DISABLED)

			
		else:
			
			self.loginWindow.destroy()
			self.master.deiconify()
			self.master.attributes('-fullscreen',True)
			self.entry = mainWindowwindow.widgetsVar.inputEntry
			self.entry.focus()
			
			self.employeenum=000000
			mainWindowwindow.widgetsVar.employeeEntry.config(state=NORMAL)
			mainWindowwindow.widgetsVar.employeeEntry.delete(0, END)

			mainWindowwindow.widgetsVar.employeeEntry.insert(0, self.employeenum)
			mainWindowwindow.widgetsVar.employeeEntry.config(state=DISABLED)
			


		return None

	def close(self, master):
		sys.exit()

class helpWindowClass:
	def __init__(self, master):
		self.helpWindow = Toplevel(master)
		self.master=master
		self.helpWindow.title("Help Page")
		self.helpWindow.geometry("500x500")
		self.helpWindow.resizable(height = False, width = False)


		self.textbox = Text(self.helpWindow, font=("Arial", 30), width=95, height=29, padx = 10, pady = 10)
		self.textbox.place(anchor=CENTER, relx = 0.5, rely=0.5)
		self.textbox.delete(1.0, END)
		self.helpList = open('helpList.txt', 'r')
		self.textbox.insert(1.0, self.helpList.read())
		self.textbox.config(state=DISABLED)

		
		self.helpWindow.bind("<KP_Enter>", lambda i: self.helpWindowDestroy())

	def helpWindowDestroy(self):
		self.helpWindow.destroy()


def start():
	x =1 
	global voidmode
	global mainWindowwindow
	c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL, priceIncrement INT, quantityInStock REAL, itemType INT)')
	c.execute('CREATE TABLE IF NOT EXISTS employees(firstName TEXT, lastName TEXT, employeeNumber TEXT, email TEXT, phone TEXT, address TEXT, dob TEXT, mgr TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS settings(settingName TEXT, value INT)')
	c.execute('SELECT settingName FROM settings WHERE settingName = ?', ["Default Employee Number"])
	dbFetch = c.fetchone()
	conn.commit()
	if dbFetch == None:
		c.execute("INSERT INTO settings(settingName, value) VALUES ( ?, ?)", (["Default Employee Number", "1",]))
		
	root = Tk()
	voidmode = IntVar()
	
	
	root.withdraw()
	mainWindowwindow = mainWindow(root)
	root.mainloop()
	return None


