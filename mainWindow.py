from tkinter import *
import sqlite3
import time as tm
import sys
from PIL import Image, ImageTk

conn = sqlite3.connect('PerkinPOSDatabase')
c= conn.cursor()
global companyName
global focus
global enterCount
companyName = "POS Test 2.7"
focus = 0
enterCount = 0
amount_of_settings = 4

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

			self.databasemenu.add_command(label="Settings", command=lambda: mainWindow.openSettings(self, master), state=ACTIVE)

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

			self.logoutButton = Button(text="Logout:\nEnter\n000", font=("Arial", 45), height = 3, width =6, command=lambda i =self, j=master:mainWindow.logout(i, j))
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

		c.execute("SELECT value FROM settings WHERE settingName = 'Sales Count'")
		self.sales_count = c.fetchone()
		self.sales_count = self.sales_count[0]

		self.widgetsVar.salesEntry.config(state = NORMAL)
		self.widgetsVar.salesEntry.delete(0, END)
		self.widgetsVar.salesEntry.insert(0, self.sales_count)
		self.widgetsVar.salesEntry.config(state = DISABLED)

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
		return False

	def bindReturn(self, master):

		
		self.priceList = self.widgetsVar.listboxPrice
		self.itemList = self.widgetsVar.listboxDescription
		self.totalPrice2 = "${:,.2f}".format(float(self.totalPrice))	

		if self.widgetsVar.inputEntry.get() == "000":
			self.logout(master)

		elif self.widgetsVar.inputEntry.get() == "000000":
			self.helpWindow = helpWindowClass(self.master)
			

			self.widgetsVar.inputEntry.delete(0, END)

		elif self.widgetsVar.inputEntry.get() == "000000000":
			self.Settings = settingsWindowClass(self.master)
			

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

				self.printText("Scan Barcode\n/: Change Price\n*: Change Qty")
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

											try:
												self.tempPrice = float(self.cartPrice[self.i])/float(self.cartquantity[self.i])
											except ZeroDivisionError:
												self.tempPrice = self.dbFetch[2]
											self.totalPrice = self.totalPrice - float(self.cartPrice[self.i])
											self.cartbarcode.append(self.dbFetch[0])
											self.cartquantity.append(self.cartquantity[self.i]+1)
											print(f'temp price is {self.tempPrice}, total price is {self.totalPrice}, the last item of cart quantity is {self.cartquantity[len(self.cartquantity)-1]}')
											self.cartPrice.append(self.tempPrice*self.cartquantity[len(self.cartquantity)-1])

											

											self.cartbarcode.pop(self.i)
											self.cartquantity.pop(self.i)
											self.cartPrice.pop(self.i)

											self.totalPrice = self.totalPrice + self.tempPrice*self.cartquantity[len(self.cartquantity)-1]
											print(f'appending total price: {self.totalPrice}')
											if self.dbFetch[3] == 1:
												self.outputText = str(self.dbFetch[1]) + " x "+str(self.cartquantity[len(self.cartquantity)-1]) +" @ " + "${:,.2f}".format(float(self.tempPrice)) + " each"
											else:
												self.outputText = str(self.dbFetch[1]) + " x "+str(self.cartquantity[len(self.cartquantity)-1]) +"kg @ " + "${:,.2f}".format(float(self.tempPrice)) + " per kilo"


											self.widgetsVar.listboxDescription.insert(END, self.outputText)
											self.widgetsVar.listboxPrice.insert("end", "${:,.2f}".format(float(self.tempPrice*self.cartquantity[len(self.cartquantity)-1])))

											if self.cartPrice[len(self.cartPrice)-1] < 0:
												self.widgetsVar.listboxDescription.itemconfig(self.widgetsVar.listboxDescription.size()-1, {'fg':'red'})
												self.widgetsVar.listboxPrice.itemconfig(self.widgetsVar.listboxPrice.size()-1, {'fg':'red'})



										else:
											self.cartbarcode.pop(self.i)
											self.cartquantity.pop(self.i)
											self.totalPrice = self.totalPrice - self.cartPrice[self.i]
											self.cartPrice.pop(self.i)

											


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
				
				c.execute('SELECT * from allItemsAndCodes where barcode = ?', [str(self.cartbarcode[self.i])])
				
				self.quantity = c.fetchone()
				print(self.quantity)
				c.execute('UPDATE allItemsAndCodes SET quantityInStock = ? WHERE barcode = ?', [self.quantity[4] - self.cartquantity[self.i], self.cartbarcode[self.i]])
				
				self.i = self.i+1
				conn.commit()
			print("Cart Items:")
			print(self.cartbarcode)
			print(self.cartquantity)
			print("-------------")

			self.rewardsNumber = 0
			self.accountsNumber = 0
			self.transType = "cash"
			self.transDate = self.widgetsVar.dateEntry.get()

			c.execute("INSERT INTO transactionPointer (transID, employeeNumber, totalcost, transdate, transtype, rewardsnum, accountnum) VALUES (?, ?, ?, ?, ?, ?, ?)", ([self.widgetsVar.salesEntry.get(), self.employee, self.totalPrice, self.transDate, self.transType, self.rewardsNumber,self.accountsNumber]))

			self.i =0
			while self.i <len(self.cartbarcode):
				c.execute("INSERT INTO transactionList (transID, barcode, quantity, price) VALUES (?, ?, ?, ?)", ([self.widgetsVar.salesEntry.get(), self.cartbarcode[self.i], self.cartquantity[self.i], self.cartPrice[self.i]]))

				self.i = self.i +1

			conn.commit()

			self.cartbarcode = []
			self.cartquantity = []
			self.totalPrice = 0

			self.widgetsVar.listboxDescription.delete(0, END)
			self.widgetsVar.listboxPrice.delete(0, END)
			self.widgetsVar.subtotal.delete(0, END)
			self.widgetsVar.subtotal.insert(0, 0)
			self.widgetsVar.inputEntry.delete(0, END)
			c.execute("SELECT value FROM settings WHERE settingName = 'Sales Count'")
			self.sales_count = c.fetchone()
			self.sales_count = self.sales_count[0]+1

			c.execute("UPDATE settings SET value = ? WHERE settingName = 'Sales Count'", [self.sales_count])
			self.widgetsVar.salesEntry.config(state = NORMAL)
			self.widgetsVar.salesEntry.delete(0, END)
			self.widgetsVar.salesEntry.insert(0, self.sales_count)
			self.widgetsVar.salesEntry.config(state = DISABLED)
			conn.commit()

		elif state == "Invoice":
			if self.check_float(self.widgetsVar.inputEntry.get())==True:

				if self.cartbarcode != []:

					if float(self.widgetsVar.inputEntry.get()) > float(self.cartPrice[len(self.cartPrice)-1]):
						self.printText("Scan Barcode\n/: Change Price\n*: Change Qty\nWARNING: Price is higher than before")



					self.totalPrice = self.totalPrice - float(self.cartPrice[len(self.cartPrice)-1])
					print(self.totalPrice)
					self.cartPrice[len(self.cartPrice)-1] = (float(self.widgetsVar.inputEntry.get())*self.cartquantity[len(self.cartquantity)-1])
					print(self.cartPrice[len(self.cartPrice)-1])

					self.totalPrice = float(self.totalPrice) + self.cartPrice[len(self.cartquantity)-1]
					print(self.totalPrice)
				



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


			if self.cartPrice[len(self.cartPrice)-1] < 0:
				self.widgetsVar.listboxDescription.itemconfig(self.widgetsVar.listboxDescription.size()-1, {'fg':'red'})
				self.widgetsVar.listboxPrice.itemconfig(self.widgetsVar.listboxPrice.size()-1, {'fg':'red'})

		return None

	def bindMultiply(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)

		if state == "Invoice":
			if self.check_float(self.widgetsVar.inputEntry.get()) == True:
				if self.cartbarcode != []:


					if self.widgetsVar.inputEntry.get() != '0':

						self.newQuantity = self.widgetsVar.inputEntry.get()
						self.widgetsVar.inputEntry.delete(0, END)

						self.c.execute("SELECT * FROM allItemsAndCodes where barcode = ?", [self.cartbarcode[len(self.cartbarcode)-1]])
						self.dbFetch=self.c.fetchone()

						try:
							self.tempPrice = float(self.cartPrice[len(self.cartPrice)-1])/float(self.cartquantity[len(self.cartquantity)-1])
						except ZeroDivisionError:
							self.tempPrice = self.dbFetch[2]
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
						
						if self.cartPrice[len(self.cartPrice)-1] < 0:
							self.widgetsVar.listboxDescription.itemconfig(self.widgetsVar.listboxDescription.size()-1, {'fg':'red'})
							self.widgetsVar.listboxPrice.itemconfig(self.widgetsVar.listboxPrice.size()-1, {'fg':'red'})

					else:
						self.i = 0
						self.end = 0
						while self.i <= len(self.cartbarcode) and self.end == 0:
							try:
								if self.cartbarcode[self.i] == self.cartbarcode[len(self.cartbarcode)-1]:
									self.itemList.delete(self.i)
									self.priceList.delete(self.i)
									self.cartbarcode.pop(self.i)
									self.cartquantity.pop(self.i)
									self.totalPrice = self.totalPrice - self.cartPrice[self.i]
									self.cartPrice.pop(self.i)
									self.widgetsVar.inputEntry.delete(0, END)
									self.widgetsVar.subtotal.delete(0, END)
									self.widgetsVar.subtotal.insert(0, self.totalPrice)
									self.end = 1

								else:
									self.i = self.i +1

							except IndexError:
								print("Nothing to Void")


						



			else:
				print("Enter a valid quantity")
		

		else:
			print("Eftpos Not Implemented Yet")

		self.widgetsVar.subtotal.delete(0, END)
		self.widgetsVar.subtotal.insert(0, "{:,.2f}".format(float(self.totalPrice))	)

	def bindAdd(self):
		self.widgetsVar.inputEntry.delete(len(self.widgetsVar.inputEntry.get())-1)

		self.input = self.widgetsVar.inputEntry.get() 

		if self.getSettingsState("Enable Lookup") == True:



			conn.commit()
			c.execute("SELECT * FROM allItemsAndCodes WHERE barcode = ?", [self.input])
			self.dbFetch = c.fetchone()
			
		
			if self.dbFetch == None:
				print("No Such Barcode")

			else:
				

				self.printText("Quantity in stock for " + str(self.dbFetch[1]) + " is: " + str(self.dbFetch[4]) + str(isWeighed(self.input)))
				self.printText(f'Item: {self.dbFetch[1]}\nPrice: ${self.dbFetch[2]}\nQuantity In Stock: {self.dbFetch[4]} {isWeighed(self.input)}')

		else:
			print("Feature DISABLED")

	def getSettingsState(self, settingName):
		c.execute("SELECT value FROM settings WHERE settingName = ?", [settingName])
		self.settingState = c.fetchone()
		self.settingState = self.settingState[0]

		if self.settingState == 0:
			return False

		elif self.settingState == 1:
			return True

		else:
			return self.settingState

	def openSettings(self, master):
		settingsWindow = settingsWindowClass(master)


class loginWindowClass:
	def __init__(self, master):
		self.loginWindow = Toplevel(master)
		self.master=master
		self.loginWindow.title("Login")
		self.loginWindow.geometry("500x500")
		self.loginWindow.resizable(height = True, width = True)

		self.canvas=Canvas(self.loginWindow, width=350, height =100)
		self.canvas.place(anchor=CENTER, relx = 0.5, rely = 0.15)
		self.img = (Image.open("logo.png"))
		self.resized_image= self.img.resize((350,100))
		self.img = ImageTk.PhotoImage(self.resized_image)

		self.canvas.create_image(0, 0, anchor=NW, image =self.img)

		self.label1=Label(self.loginWindow, text="Enter Employee Number", font=("Arial", 20))
		self.label1.place(anchor=CENTER, relx = 0.5, rely=0.3)

		self.entry1 = Entry(self.loginWindow, width=45, font=("{Times New Roman}", 15))
		self.entry1.place(anchor=CENTER, relx=0.5, rely = 0.38)
		self.entry1.focus()


		self.loginButton = Button(self.loginWindow, text="Login",font=("Arial", 15), command=lambda: self.login(master, self.entry1))
		self.loginButton.place(anchor=CENTER, relx=0.5, rely=0.45)

		self.destroyLogin = Button(self.loginWindow, text="EXIT",font=("Arial, 25"), command=lambda i=master: self.close(i))
		self.destroyLogin.place(anchor=CENTER, relx=0.5, rely=0.9)

		self.noEmployee = Label(self.loginWindow, text = "", fg='red', font=("Arial", 25))
		self.noEmployee.place(anchor=CENTER, relx=0.5, rely=0.6)

		self.loginWindow.bind("<Return>", lambda i=master, j=self.entry1:self.login(i, j))
		self.loginWindow.bind("<KP_Enter>", lambda i=master, j=self.entry1:self.login(i, j))
		self.employeenum=5




		

	def login(self, master, entryInputs):
		if self.entry1.get() == "000":
				self.close(master)
		
		c.execute('SELECT * FROM settings WHERE settingName = ?', ["Default Employee Number"])
		self.a = c.fetchone()
		print(self.a[1])
		if self.a[1] == 1:

			c.execute('SELECT * FROM employees WHERE employeeNumber = ?', [self.entry1.get()])
			self.dbFetch = c.fetchone()
			

			if self.dbFetch == None:
				print("No Such Employee")
				self.noEmployee.config(text = "No Such Employee")
				self.entry1.delete(0, END)



			else:
				
				self.loginWindow.destroy()
				self.master.deiconify()
				self.master.attributes('-fullscreen',True)
				self.entry = mainWindowwindow.widgetsVar.inputEntry
				self.entry.focus()
				
				self.employeenum=self.dbFetch[0]+" "+self.dbFetch[1][0]
				self.mgr = self.dbFetch[7]
				mainWindowwindow.widgetsVar.employeeEntry.config(state=NORMAL)
				mainWindowwindow.widgetsVar.employeeEntry.delete(0, END)

				mainWindowwindow.widgetsVar.employeeEntry.insert(0, self.employeenum)
				mainWindowwindow.widgetsVar.employeeEntry.config(state=DISABLED)

				mainWindowwindow.widgetsVar.managerEntry.config(state=NORMAL)
				mainWindowwindow.widgetsVar.managerEntry.delete(0, END)

				mainWindowwindow.widgetsVar.managerEntry.insert(0, self.isManger(self.dbFetch[7]))
				mainWindowwindow.widgetsVar.managerEntry.config(state=DISABLED)



			
		else:

			c.execute('SELECT employeeNumber FROM employees WHERE mgr = 1')
			self.dbFetch = c.fetchone()
			if self.dbFetch == None:
				print("Non-Error: No employee with manager permissions set up")
			
				self.loginWindow.destroy()
				self.master.deiconify()
				self.master.attributes('-fullscreen',True)
				self.entry = mainWindowwindow.widgetsVar.inputEntry
				self.entry.focus()
				
				self.employeenum="None"
				self.mgr = "Yes"
				mainWindowwindow.widgetsVar.employeeEntry.config(state=NORMAL)
				mainWindowwindow.widgetsVar.employeeEntry.delete(0, END)

				mainWindowwindow.widgetsVar.employeeEntry.insert(0, self.employeenum)
				mainWindowwindow.widgetsVar.employeeEntry.config(state=DISABLED)

				mainWindowwindow.widgetsVar.managerEntry.config(state=NORMAL)
				mainWindowwindow.widgetsVar.managerEntry.delete(0, END)

				mainWindowwindow.widgetsVar.managerEntry.insert(0, self.mgr)
				mainWindowwindow.widgetsVar.managerEntry.config(state=DISABLED)

			else:
				self.dbFetch = self.dbFetch[0]
				if self.entry1.get() == self.dbFetch:

					self.loginWindow.destroy()
					self.master.deiconify()
					self.master.attributes('-fullscreen',True)
					self.entry = mainWindowwindow.widgetsVar.inputEntry
					self.entry.focus()
					
					self.employeenum="None"
					self.mgr = "Yes"
					mainWindowwindow.widgetsVar.employeeEntry.config(state=NORMAL)
					mainWindowwindow.widgetsVar.employeeEntry.delete(0, END)

					mainWindowwindow.widgetsVar.employeeEntry.insert(0, self.employeenum)
					mainWindowwindow.widgetsVar.employeeEntry.config(state=DISABLED)

					mainWindowwindow.widgetsVar.managerEntry.config(state=NORMAL)
					mainWindowwindow.widgetsVar.managerEntry.delete(0, END)

					mainWindowwindow.widgetsVar.managerEntry.insert(0, self.mgr)
					mainWindowwindow.widgetsVar.managerEntry.config(state=DISABLED)

				else:
					self.loginWindow.destroy()
					self.master.deiconify()
					self.master.attributes('-fullscreen',True)
					self.entry = mainWindowwindow.widgetsVar.inputEntry
					self.entry.focus()
					
					self.employeenum="None"
					self.mgr = "No"
					mainWindowwindow.widgetsVar.employeeEntry.config(state=NORMAL)
					mainWindowwindow.widgetsVar.employeeEntry.delete(0, END)

					mainWindowwindow.widgetsVar.employeeEntry.insert(0, self.employeenum)
					mainWindowwindow.widgetsVar.employeeEntry.config(state=DISABLED)

					mainWindowwindow.widgetsVar.managerEntry.config(state=NORMAL)
					mainWindowwindow.widgetsVar.managerEntry.delete(0, END)

					mainWindowwindow.widgetsVar.managerEntry.insert(0, self.mgr)
					mainWindowwindow.widgetsVar.managerEntry.config(state=DISABLED)



			


		return None

	def close(self, master):
		sys.exit()

	def isManger(self, inputa):
		
		if inputa == "1":
			
			return "Yes"

		else:
			
			return "No"

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

class settingsWindowClass:
	def __init__(self, master):
		if mainWindowwindow.widgetsVar.managerEntry.get() == "Yes":

			self.SettingsWindow = Toplevel(master)
			self.master=master
			self.SettingsWindow.title("Settings")
			self.SettingsWindow.geometry("500x500")
			self.SettingsWindow.resizable(height = False, width = False)

			self.title = Label(self.SettingsWindow, text = "Settings", font = ("Arial", 75))
			self.title.place(anchor=CENTER, relx=0.5, rely = 0.05)
			self.search = Entry(self.SettingsWindow, width = 45, font=("Arial", 25))
			self.search.place(anchor=NW, relx=0.01, rely=0.15)
			self.search.focus()

			self.frame = LabelFrame(self.SettingsWindow, text = "Type setting number to modify", font=("Arial", 30))
			self.frame.place(anchor=NW, relx = 0.01, rely = 0.22)

			self.info = Label(self.frame, text="Actions Appear Here", font=("Arial", 25))
			self.info.pack(anchor = W)


			Label(self.SettingsWindow, text="#", font = ('Arial', 15)).place(anchor=NW, relx = 0.59975, rely = 0.1275)
			Label(self.SettingsWindow, text="Setting Name", font = ('Arial', 15)).place(anchor=NW, relx = 0.61225, rely = 0.1275)
			Label(self.SettingsWindow, text="Value", font = ('Arial', 15)).place(anchor=NW, relx = 0.786, rely = 0.1275)
			Label(self.SettingsWindow, text="/", font = ('Arial', 15)).place(anchor=NW, relx = 0.8145, rely = 0.1275)
			Label(self.SettingsWindow, text="*", font = ('Arial', 15)).place(anchor=NW, relx = 0.843, rely = 0.1275)
			Label(self.SettingsWindow, text="-", font = ('Arial', 15)).place(anchor=NW, relx = 0.8715, rely = 0.1275)
			Label(self.SettingsWindow, text='+', font = ('Arial', 15)).place(anchor=NW, relx = 0.9, rely = 0.1275)


			Label(self.SettingsWindow, text='Press Enter to Exit the Settings', font = ('Arial', 30)).place(anchor=CENTER, relx = 0.5, rely = 0.85)

			self.settingsName = Listbox(self.SettingsWindow, width=32, font=("Arial", 15), height = amount_of_settings)
			self.settingsName.place(anchor=NW, relx = 0.61225, rely=0.15)
			self.settingsValue = Listbox(self.SettingsWindow, width=5, font=("Arial", 15), height = amount_of_settings)
			self.settingsValue.place(anchor=NW, relx = 0.786, rely=0.15)
			self.settingsNumber = Listbox(self.SettingsWindow, width=2, font=("Arial", 15), height = amount_of_settings)
			self.settingsNumber.place(anchor=NW, relx = 0.59975, rely=0.15)
			self.settingsDivide= Listbox(self.SettingsWindow, width=5, font=("Arial", 15), height = amount_of_settings)
			self.settingsDivide.place(anchor=NW, relx = 0.8145, rely=0.15)
			self.settingsMultiply = Listbox(self.SettingsWindow, width=5, font=("Arial", 15), height = amount_of_settings)
			self.settingsMultiply.place(anchor=NW, relx = 0.843, rely=0.15)
			self.settingsMinus = Listbox(self.SettingsWindow, width=5, font=("Arial", 15), height = amount_of_settings)
			self.settingsMinus.place(anchor=NW, relx = 0.8715, rely=0.15)
			self.settingsAdd = Listbox(self.SettingsWindow, width=5, font=("Arial", 15), height = amount_of_settings)
			self.settingsAdd.place(anchor=NW, relx = 0.9, rely=0.15)
			
			c.execute("SELECT value FROM settings")
			self.dbFetch = c.fetchall()
			

			self.pass_in_colours("1", "Require Employee Number", self.valtobool(self.dbFetch[0][0])[0], "", "", "", "", self.valtobool(self.dbFetch[0][0])[1], 'blue', 'blue', 'blue', 'blue')
			self.pass_in_colours("2", "Reset Sales Count", self.dbFetch[1][0], "", "", "", "", 'orange', 'blue', 'blue', 'blue', 'blue')
			self.pass_in_colours("3", "Enable Lookup",self.valtobool(self.dbFetch[2][0])[0], "", "", "", "", self.valtobool(self.dbFetch[2][0])[1], 'blue', 'blue', 'blue', 'blue')
			self.pass_in_colours("4", "Destroy Trans On Logout", self.valtobool(self.dbFetch[3][0])[0], "", "", "", "", self.valtobool(self.dbFetch[3][0])[1], 'blue', 'blue', 'blue', 'blue')

			self.SettingsWindow.bind("<KeyRelease>", lambda i : self.releaseKey())
			self.SettingsWindow.bind("<KP_Enter>", lambda i: self.helpWindowDestroy())



		else:
			pass

	def valtobool(self, val):
		if val == 1:
			return ['True', 'green']

		elif val == 0:
			return ['False', 'red']

		else:
			return ['', 'blue']

	def pass_in_colours(self, num, name, val, div, mult, minus, add, valcol, divcol, multcol, mincol, addcol):
		self.settingsName.insert(END, name)
		self.settingsValue.insert(END, val)
		self.settingsValue.itemconfig(0, fg = 'white')
		self.settingsNumber.insert(END, num)
		self.settingsDivide.insert(END, div)
		self.settingsMultiply.insert(END, mult)
		self.settingsMinus.insert(END, minus)
		self.settingsAdd.insert(END, add)
		self.settingsValue.itemconfig(END, bg=valcol)
		self.settingsAdd.itemconfig(END, bg=addcol)
		self.settingsMinus.itemconfig(END, bg=mincol)
		self.settingsDivide.itemconfig(END, bg=divcol)
		self.settingsMultiply.itemconfig(END, bg=multcol)
		self.settingsValue.itemconfig(END, fg = 'white')




	def helpWindowDestroy(self):
		c.execute("SELECT value FROM settings WHERE settingName = 'Sales Count'")
		self.sales_count = c.fetchone()
		self.sales_count = self.sales_count[0]

		mainWindowwindow.widgetsVar.salesEntry.config(state = NORMAL)
		mainWindowwindow.widgetsVar.salesEntry.delete(0, END)
		mainWindowwindow.widgetsVar.salesEntry.insert(0, self.sales_count)
		mainWindowwindow.widgetsVar.salesEntry.config(state = DISABLED)
		self.SettingsWindow.destroy()

	def check_int(self, check_int):
		try:

			a = int(check_int)

			return True

		except:
			return False

	def releaseKey(self):
		
		

		self.input = str(self.search.get())


		#Setting one
		
		if self.input == "1":
			self.frame.config(text="Options for setting: Require Employee Number")
			self.info.config(anchor = W, text="When set to true an employee number is required to open POS\nWhen set to false no employee number is required\n/ :sets to true\n* :sets to false")

		elif self.input == "1/":
			
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")


			c.execute('SELECT employeeNumber FROM employees WHERE mgr = 1')
			self.dbFetch = c.fetchone()
			if self.dbFetch == None:

				print("Non-Error: No employee with manager permissions set up. Manager attribute is required to set 'Require Employee Number' to true.")
			else:


				c.execute("UPDATE settings SET value = 1 WHERE settingName = 'Default Employee Number'")
				conn.commit()


				
				self.settingsValue.delete(0)
				self.settingsValue.insert(0, "True")
				self.settingsValue.itemconfig(0, bg = 'green')
				self.settingsValue.itemconfig(0, fg = 'white')



			self.search.delete(0, END)

			
		elif self.input == "1*":
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")

			c.execute("UPDATE settings SET value = 0 WHERE settingName = 'Default Employee Number'")
			conn.commit()
			
			self.settingsValue.delete(0)
			self.settingsValue.insert(0, "False")
			self.settingsValue.itemconfig(0, bg = 'red')
			self.settingsValue.itemconfig(0, fg = 'white')
			self.search.delete(0, END)

		# Setting two
		elif self.input == "2":
			self.frame.config(text="Options for setting: Reset Sales Count")
			self.info.config(text="/: Resets the sales count to 0. Don't do this unless POS is new")

		elif self.input == "2/":
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")

			c.execute("UPDATE settings SET value = 0 WHERE settingName = 'Sales Count'")
			conn.commit()
			c.execute("DROP table transactionPointer")
			c.execute("DROP table transactionList")
			c.execute('CREATE TABLE IF NOT EXISTS transactionPointer(transID TEXT, employeeNumber TEXT, totalcost REAL, transdate TEXT, transtype TEXT, rewardsnum TEXT, accountnum TEXT)')
			c.execute('CREATE TABLE IF NOT EXISTS transactionList(transID TEXT, barcode TEXT, quantity REAL, price REAL)')



			self.settingsValue.delete(1)
			self.settingsValue.insert(1, "0")
			self.settingsValue.itemconfig(1, bg = 'orange')
			self.settingsValue.itemconfig(1, fg = 'white')






			self.search.delete(0, END)



		# Setting three

		elif self.input == "3":
			self.frame.config(text="Options for setting: Enable Lookup")
			self.info.config(text="When set to true, users can look up the price, name and\n quantity in stock of a specific item by entering the barcode and then hitting \nthe + symbol.\n/ : sets to true\n* : sets to false")

		elif self.input == "3/":
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")

			c.execute("UPDATE settings SET value = 1 WHERE settingName = 'Enable Lookup'")
			conn.commit()

			self.settingsValue.delete(2)
			self.settingsValue.insert(2, "True")
			self.settingsValue.itemconfig(2, bg = 'green')
			self.settingsValue.itemconfig(2, fg = 'white')

			self.search.delete(0, END)

		elif self.input == "3*":
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")

			c.execute("UPDATE settings SET value = 0 WHERE settingName = 'Enable Lookup'")
			conn.commit()

			self.settingsValue.delete(2)
			self.settingsValue.insert(2, "False")
			self.settingsValue.itemconfig(2, bg = 'red')
			self.settingsValue.itemconfig(2, fg = 'white')


			self.search.delete(0, END)




		elif self.input == "4":
			self.frame.config(text="Options for setting: Destroy Trans On Logout")
			self.info.config(text="When set to true, the transaction will be canceled upon logout. \nAll items in the cart list will be removed.\n/ : sets to true\n* : sets to false(not yet Implemented)")

		elif self.input == "4/":
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")

			c.execute("UPDATE settings SET value = 1 WHERE settingName = 'Destroy Trans On Logout'")
			conn.commit()

			self.settingsValue.delete(3)
			self.settingsValue.insert(3, "True")
			self.settingsValue.itemconfig(3, bg = 'green')
			self.settingsValue.itemconfig(3, fg = 'white')


			self.search.delete(0, END)


		elif self.input == "4*":
			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")

			c.execute("UPDATE settings SET value = 1 WHERE settingName = 'Destroy Trans On Logout'")
			conn.commit()

			self.settingsValue.delete(3)
			self.settingsValue.insert(3, "True")
			self.settingsValue.itemconfig(3, bg = 'green')
			self.settingsValue.itemconfig(3, fg = 'white')


			self.search.delete(0, END)

			

		else:

			self.frame.config(text="Type setting number to modify")
			self.info.config(text="Actions Appear Here")







		return True


def insertSetting(settingName, value):
	c.execute('SELECT settingName FROM settings WHERE settingName = ?', [settingName])
	dbFetch = c.fetchone()
	conn.commit()
	if dbFetch == None:
		c.execute("INSERT INTO settings(settingName, value) VALUES ( ?, ?)", ([settingName, value,]))

def isWeighed(barcode):
		c.execute("SELECT priceIncrement FROM allItemsAndCodes WHERE barcode = ?", [barcode])
		dbFetch = c.fetchone()
		if dbFetch == None:
			print("Barcode Not Foudn")

		else:
			if dbFetch[0] == 0:
				tempVar = " kilo"

			else:
				tempVar = " units"

			return tempVar
		


def start():
	x =1 
	global voidmode
	global mainWindowwindow
	c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL, priceIncrement INT, quantityInStock REAL, itemType INT)')
	c.execute('CREATE TABLE IF NOT EXISTS employees(firstName TEXT, lastName TEXT, employeeNumber TEXT, email TEXT, phone TEXT, address TEXT, dob TEXT, mgr TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS settings(settingName TEXT, value INT)')
	c.execute('CREATE TABLE IF NOT EXISTS transactionPointer(transID TEXT, employeeNumber TEXT, totalcost REAL, transdate TEXT, transtype TEXT, rewardsnum TEXT, accountnum TEXT)')
	c.execute('CREATE TABLE IF NOT EXISTS transactionList(transID TEXT, barcode TEXT, quantity REAL, price REAL)')
	insertSetting("Default Employee Number", 0)
	insertSetting("Sales Count", 1)
	insertSetting("Enable Lookup", 1)
	insertSetting("Destroy Trans On Logout", 1)


	root = Tk()
	
	
	
	root.withdraw()
	mainWindowwindow = mainWindow(root)
	root.mainloop()
	return None


