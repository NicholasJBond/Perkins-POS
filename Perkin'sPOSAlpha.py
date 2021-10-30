
#Python imports
from tkinter import *
import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('PerkinPOSDatabase')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL, priceIncrement INT, quantityInStock REAL, itemType INT)')



#Variables
companyName = "Perkin's POS"
state = "00"
itemTypeArray = ["Fruit", "Vegetable", "Value Pack"]
cartPrice = []
cartQuantity = []
cart = []
barcodeHolder = 0

#Tk window
root = Tk()
root.title("PerkinsPOSTest-1.3.1")
root.geometry('400x600')

#Tk Widgets
inputEntry = Entry(root, width=60)
inputEntry.pack()

textOutput = Text(root, width=60, height=50)

textOutput.pack()







#Functions
def check_float(potential_float):
    try:
        float(potential_float)

        return True
    except ValueError:
        return False


def endLine():
    textOutput.insert(1.0, "+--------------======+"+companyName+"+======--------------+\n")

def printText(text):
    textOutput.config(state=NORMAL)
    textOutput.delete(1.0, END)
    endLine()
    textOutput.insert(1.0, text+"\n")
    endLine()
    textOutput.config(state=DISABLED)

def search(barcode):
    global barcodeHolder
    barcodeHolder = barcode
    conn = sqlite3.connect('PerkinPOSDatabase')
    c = conn.cursor()
    c.execute("SELECT description FROM allItemsAndCodes WHERE barcode =?", [barcode])
    dbFetch = c.fetchone()
    
    global state
    if (dbFetch == None):
        printText("Barcode not on file; Please try again\nType 'help' and then hit enter to show a list of\ncommands")

    else:
        c.execute("SELECT * FROM allItemsAndCodes WHERE barcode =?", [barcode])
        dbFetch = c.fetchone()
        if (dbFetch[3] == 0):
            printText("Enter weight in kilograms")
            state = "0101"
            


        else:
            cartPrice.append(dbFetch[2])
            cartQuantity.append(1)
            cart.append([str(dbFetch[1]), "$"+str(dbFetch[2]), str(1)])
            head = ["Description", "Price", "Quantity"]
        
        
            printText(tabulate(cart, headers= head, tablefmt="fancy_grid", showindex=True))
            state = "01"







def getInput(self):
    
    global state
    global dbFetch
    global barcodeHolder
    entryInput = inputEntry.get()
    inputEntry.delete(0, END)
    print(state)
    

    if (state == "00"):
        printText("Enter your login number\nHint: 010209")
        if (entryInput == "00"):
            exit()

        elif (entryInput == "010209"):
            state = "01"
            printText("Login Successful\nType 'help' and then enter to show a list of commands")
            

    if (state == "0101"):
        global dbFetch
        

        
        state = "01"
        c.execute("SELECT * FROM allItemsAndCodes WHERE barcode =?", [barcodeHolder])
        dbFetch = c.fetchone()
        

        if(check_float(entryInput) == True):
            cartPrice.append(float(dbFetch[2])*float(entryInput))
            cartQuantity.append(entryInput)
            
            cart.append([str(dbFetch[1]), "$"+str(dbFetch[2]*float(entryInput)), entryInput+"kg"])
            head = ["Description", "Price", "Quantity"]
        
        
            printText(tabulate(cart, headers= head, tablefmt="fancy_grid", showindex=True))
            state = "01"

        else:
            printText("Invalid weight\nType 'help' and then enter to show a list of commands")

    elif (state == "01"):
        printText("Scan barcode to begin invoice\nType 'help' and then enter to show a list of commands")
        
        if (entryInput == "00"):
            state = "00"
            printText("Log out Successful")

        elif (entryInput == "help" or entryInput == "01"):
            state = "01"
            helpList = open('helpPage.txt', 'r')
            printText(helpList.read())

        elif (entryInput == "02"):
            state = "0102"
            
            printText("Entering database mode!!!\nEditing the database is dangerous.\n nly do it if you know what you are doing.\nSelect the table you want to edit:\n00 - Cancel Operation\n01 - allItemsAndCodes.db")

        else:
            if (entryInput != None):
                barcodeHolder = entryInput
                search(entryInput)
            else:
                printText("Please try again")
            

    elif (state == "0102"):
        if (entryInput == "00"):
            state = "01"
            printText("Operation canceled\nPress <enter> to continue")

        if (entryInput == "01"):
            state = "010201"
            printText("allItemsAndCodes.db selected\n\n00 - Cancel Operation\n01 - Create entry\n02 - Delete entry\n03 - Change barcode\n04 - Change item description\n05 - Change item price\n06 - Change item quantity in stock\n07 - Change price measurement\n08 - Check quantity in stock\n09 - Show database")


    elif (state == "010201"):
        if (entryInput == "00"):
            state = "01"
            printText("Operation canceled\nPress <enter> to continue")
        
        if (entryInput == "01"):
            state = "01"
            printText("Create Entry\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")


        if (entryInput == "02"):
            state = "01"
            printText("Delete Entry\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "03"):
            state = "01"
            printText("Change Barcode\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "04"):
            state = "01"
            printText("Change Item Description\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "05"):
            state = "01"
            printText("Change Item Price\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "06"):
            state = "01"
            printText("Change Item Quantity in Stock\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        
        if (entryInput == "07"):
            state = "01"
            printText("Change Price Measurement\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "08"):
            state = "01"
            printText("Check Quantity\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "09"):
            state = "01"
            printText("Show Database\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")

    
        
def systemNotResponding(self):
    global state
    state="00"
   
    printText("System Terminated; Press <Enter> to continue")
        

        

printText("Enter your login number\nHint: 010209")

    

    
        
    

root.bind("<Escape>", systemNotResponding )
root.bind("<Return>", getInput)




   
    





root.mainloop()