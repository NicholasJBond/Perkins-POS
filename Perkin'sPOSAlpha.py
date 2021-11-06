
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
itemTypeArray = ["Undefined", "Vegetable", "Value Pack", "Fruit"]
cartPrice = []
cartQuantity = []
cart = []
barcodeHolder = 0

#Tk window
root = Tk()
root.title("PerkinsPOSTest-1.3.2")
root.geometry('825x900')

#Tk Widgets
inputEntry = Entry(root, width=89)
inputEntry.pack()




textOutput = Text(root, width=115, height=65)

textOutput.pack()







#Functions
def check_float(potential_float):
    try:
        float(potential_float)

        return True
    except ValueError:
        return False


def endLine():
    textOutput.insert(1.0, "+------------======+======+======+======+======+--+"+companyName+"+--+======+======+======+======+======------------+\n")

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
        if (state == "001"):
            printText("Welcome to Perkin's POS :)\nScan a barcode to begin invoice")
            state = "01"

        else:

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
    global priceIncrementEntry
    global state
    global dbFetch
    global barcodeHolder
    global barcodeEntry
    entryInput = inputEntry.get()
    inputEntry.delete(0, END)
    print(state)
    if (state == "001"):
        state = "01"

    if (state == "00"):
        printText("Enter your login number\nHint: 010209")
        if (entryInput == "00"):
            exit()

        elif (entryInput == "010209"):
            state = "001"
            printText("Login Successful\nType 'help' and then enter to show a list of commands")
            

    if (state == "0101"):
        global dbFetch
        

        
        state = "01"
        c.execute("SELECT * FROM allItemsAndCodes WHERE barcode =?", [barcodeHolder])
        dbFetch = c.fetchone()
        

        if(check_float(entryInput) == True):
            cartPrice.append(round(float(dbFetch[2])*float(entryInput), 2))
            cartQuantity.append(round(float(entryInput), 2))
            
            cart.append([str(dbFetch[1]), "$"+str(round(float(dbFetch[2])*float(entryInput), 2)), str(round(float(entryInput), 2))+"kg"])
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
            
            printText("Entering database mode!!!\nEditing the database is dangerous.\n Only do it if you know what you are doing.\nSelect the table you want to edit:\n00 - Cancel Operation\n01 - allItemsAndCodes.db")

        else:
            if (entryInput != None):
                barcodeHolder = entryInput
                search(entryInput)
            
            

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
            state = "newBarcode"
            printText("Enter barcode of the new item")
         

        if (entryInput == "02"):
            state = "deletestuff"
            printText("Enter the barcode you wish to delete>>")
            

        if (entryInput == "03"):
            state = "changeBarcode"
            printText("Enter the barcode you wish to change>>")


        if (entryInput == "04"):
            state = "changeDescription"
            printText("Enter the barcode you wish to change the description>>")
        

        if (entryInput == "05"):
            state = "changeprice"
            printText("Enter the barcode you which to change the price>>")
        

        if (entryInput == "06"):
            state = "01"
            printText("Change Item Quantity in Stock\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        
        if (entryInput == "07"):
            state = "changepriceincrement"
            printText("Enter the barcode you wish to change the price increment")
        

        if (entryInput == "08"):
            state = "01"
            printText("Check Quantity\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
        

        if (entryInput == "09"):
            state = "01"
            printText("Show Database\nWoopsy That feature is not in the GUI\nTry PerkinsPOSShellVersion.py")
            printText("---All Items and Stock---")
            c.execute('SELECT * FROM allItemsAndCodes')
        

            head = ["Description", "Barcode", "Price", "Quantity In Stock", "Price Increment", "Item Type"]
            global itemsInfo
            itemsInfo = []


            for row in c.fetchall():
                if(row[3]==0):
                    priceIncrementEntry = "per kg"
                else:
                    priceIncrementEntry = "each"

                for i in range(15):

                    if(row[5]==i):
                        itemType =itemTypeArray[i]


                
                itemsInfo.append([row[1], row[0], "$"+str(row[2]), row[4], priceIncrementEntry, itemType,])
            printText(tabulate(itemsInfo, headers=head, tablefmt="fancy_grid", showindex=False))
        
        if (entryInput == "10"):
            state = "01"
            conn.commit()
            printText("Conn is committed>>state is 01. Scan a barcode to continue")


        
        

            
            
        

    elif (state == "newBarcode"):
        global barcodeEntry
        barcodeEntry = entryInput
        c.execute('SELECT barcode FROM allItemsAndCodes WHERE barcode = ?', [barcodeEntry])
        
        if (c.fetchone() == None):

            state = "newBarcode1"

            printText("Enter the description of the new item")

        else:
            printText("An item already exists with the barcode of " + str(barcodeEntry))
            state = "01"


    elif (state == "newBarcode1"):
        global descriptionEntry
        descriptionEntry = entryInput
        state = "newBarcode2"
        printText("Enter the price of the new item")

    elif (state == "newBarcode2"):
        global priceEntry
        if (check_float(entryInput) == True):
            priceEntry = entryInput
            state = "newBarcode3"
            printText("If measured in kilograms enter 0, if measured per item enter 1")

        else:
            printText("Do not use a $ sign when entering price. Press escape to cancel")

    elif (state == "newBarcode3"):

        priceIncrementEntry = entryInput
        state = "newBarcode4"
        printText("What type of product is it? (Type 0 if unsure. Check the help page to find out)")
        
    elif (state == "newBarcode4"):

        
        itemType = itemTypeArray[int(entryInput)]
        state = "01"
        a = "0"

        c.execute("INSERT INTO allItemsAndCodes(barcode, description, price, priceIncrement, quantityInStock, ItemType) VALUES (?, ?, ?, ?, ?, ?)",
         (barcodeEntry, descriptionEntry, priceEntry, priceIncrementEntry, "0", entryInput))

        printText("New Item Has been added:\nBarcode:" + barcodeEntry + "\nDescription:" + descriptionEntry + "\nPrice:$" + priceEntry + "\nItem Type:" + itemType + "\nQuantity In Stock:0")
        
        conn.commit()

    elif (state == "deletestuff"):
        state = "01"
        barcodeHolder = entryInput
        c.execute('SELECT description FROM allItemsAndCodes WHERE barcode =?', [barcodeHolder])
        descriptionEntry = c.fetchone()
        
        if (descriptionEntry == None):
            print("Barcode Not Found")
        else:
            descriptionEntry = str(descriptionEntry[0])
            c.execute('DELETE FROM allItemsAndCodes WHERE barcode =?', [barcodeHolder])
            printText("Successful Deletion")

    elif (state == "changeBarcode"):
        global barcodePlaceholder
        barcodePlaceholder = entryInput
        c.execute('SELECT * FROM allItemsAndCodes WHERE barcode = ?', [entryInput])
        line = c.fetchone()

        if (line != None):
            
            state = "changeBarcode2"
            printText("New Barcode>>")

        else:
            printText("LOL get rekt, imagine trying to change something that doesn't exist LMAO")

    elif (state == "changeBarcode2"):
        state = "01"
        print(barcodePlaceholder + entryInput)
        c.execute('UPDATE allItemsAndCodes SET barcode = ? WHERE barcode = ?',[entryInput, barcodePlaceholder])
        conn.commit()
        printText("You changed the barcode. Oh well if it was a mistake. But.. you can't undo it.")

    elif (state == "changeDescription"):
        
        barcodeEntry = entryInput
        c.execute('SELECT barcode FROM allItemsAndCodes WHERE barcode = ?', [barcodeEntry])
        
        if (c.fetchone() == None):
            printText("Item does not exist")
            state = "01"
            

        else:
            state = "changeDescription2"
            c.execute('SELECT description FROM allItemsAndCodes WHERE barcode = ?', [barcodeEntry])
            printText("Enter the new description for " + str(c.fetchone()[0]))


    elif (state == "changeDescription2"):
        c.execute('UPDATE allItemsAndCodes SET description = ? WHERE barcode = ?',[entryInput, barcodeEntry])
        state = "01"
        conn.commit()
        printText("Description changed to " + entryInput)

    elif (state == "changeprice"):
        barcodeHolder = entryInput
        c.execute("SELECT * FROM allItemsAndCodes WHERE barcode = ?", [entryInput])
        dbFetch = c.fetchone()

        if (dbFetch[0] == None):
            printText("Barcode Does Not Exist, try again. Press escape to cancel")

        else:
            state = "changeprice2"
            printText("Enter the new price of " + dbFetch[1])

    elif (state == "changeprice2"):
        c.execute("SELECT * FROM allItemsAndCodes WHERE barcode = ?", [barcodeHolder])
        dbFetch = c.fetchall()

        c.execute("UPDATE allItemsAndCodes SET price =? WHERE barcode =?", [entryInput, barcodeHolder])
        conn.commit()
        printText("The new price is $" + str(entryInput))
        state = "01"

    elif (state == "changepriceincrement"):
        barcodeHolder = entryInput
        c.execute("SELECT * FROM allItemsAndCodes WHERE barcode = ?", [entryInput])
        dbFetch = c.fetchone()
        

        if (dbFetch[0] == None):
            printText("Barcode Does Not Exist, try again. Press escape to cancel")

        else:
            state = "changepriceincrement2"
            print(dbFetch[3])
            c.execute("UPDATE allItemsAndCodes SET priceIncrement =? WHERE barcode =?", [str(1-int(dbFetch[3])), barcodeHolder])
            conn.commit()
            if (dbFetch[3] == 0):
                c.execute("SELECT description FROM allItemsAndCodes WHERE barcode =?", [entryInput])

                a=c.fetchone()
                a=a[0]
                
                printText(str(a) + " used to be measured per kilo but now is measure per item")

                state ="01"
                
            else:
                c.execute("SELECT description FROM allItemsAndCodes WHERE barcode =?", [entryInput])
                a=c.fetchone()
                a=a[0]
                printText(str(a) + " used to be measured per item but now is measure per kilo")
                
                state ="01"

            
            


        
        




        
            

    
        
def systemNotResponding(self):
    global state
    conn.commit()
    state="01"
   
    printText("Proccess Terminated; Press <Enter> to continue")
        

        

printText("Enter your login number\nHint: 010209")

    

    
        
    

root.bind("<Escape>", systemNotResponding )
root.bind("<Return>", getInput)




   
    





root.mainloop()