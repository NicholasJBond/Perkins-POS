import sqlite3
from tabulate import tabulate

conn = sqlite3.connect('PerkinPOSDatabase')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL, priceIncrement INT, quantityInStock REAL, itemType INT)')

barcodeEntry = "0"
descriptionEntry = "0"
priceEntry = 0
priceIncrementEntry = 0
quantityInStockEntry = 0

shoppingCart = []
global priceTotal
priceTotal = [0]
quantityTotal = [0]
global itemType

lineInput = 0
loginLoop = 1
mainLoop = 0

itemTypeArray = ["Fruit", "Vegetable", "Value Pack"]








def check_float(potential_float):
    try:
        float(potential_float)

        return True
    except ValueError:
        return False






def searchForItem(bcode):
    c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?',[bcode])
    descriptionEntry=c.fetchone()

    if (descriptionEntry == None):
        print("Barcode Not Found")

    else:

        c.execute('SELECT * FROM allItemsAndCodes WHERE barcode = ?', [bcode])
        row=c.fetchall()
        row=row[0]
        
        if (row[3] == 0):
            lineInput = input("Enter the weight in kilograms:")
            if check_float(lineInput) == True:

                priceTotal.append(float(row[2])*float(lineInput))
                quantityTotal.append(float(lineInput))
                priceEntry=row[2]*float(lineInput)
                shoppingCart.append([str(row[1]), "$"+str(priceEntry), str(lineInput)])

            else:
                print("Not a valid weight - Returning to cl~:")

        else:
            
            priceTotal.append(row[2])
            quantityTotal.append(1)
            shoppingCart.append([str(row[1]), "$"+str(row[2]), str(1)])

        head = ["Description", "Price", "Quantity"]
        
        
        print(tabulate(shoppingCart, headers= head, tablefmt="fancy_grid", showindex=True))




        
def payForItem():
    global shoppingCart
    global priceTotal
    a=sum(priceTotal)
    print(a)
    head = ["Description", "Price", "Quantity"]
    shoppingCart.append(["", "", ""])
    shoppingCart.append(["Total:", "$"+str(a), ""])
    print(tabulate(shoppingCart, headers= head, tablefmt="fancy_grid"))
    
    shoppingCart=[]
    priceTotal=[]









## 02/00
def newItem():
    barcodeEntry = input("Type the barcode of the new item and then press enter:")
    descriptionEntry = input("Type the description/name of the new item and then press enter:")
    priceEntry = input("Type the price of the new item. Do not include the $ sign:")
    priceIncrementEntry = input("If measured by kilograms enter (0) if it is per item enter (1):")
    quantityInStockEntry = 0
    c.execute("INSERT INTO allItemsAndCodes(barcode, description, price, priceIncrement, quantityInStock) VALUES (?, ?, ?, ?, ?)",
                                  (barcodeEntry, descriptionEntry, priceEntry, priceIncrementEntry, quantityInStockEntry))
    conn.commit()
    print(descriptionEntry + " with an access code of " + barcodeEntry + " has successfully been added to the database with a price of $" + priceEntry + " per increment.")
    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")











def delData():
    
    lineInput=input("Barcode:")
    if (descriptionEntry == None):
        print("Barcode Not Found")
    else:
        descriptionEntry = str(descriptionEntry[0])
        c.execute('DELETE FROM allItemsAndCodes WHERE barcode =?', [lineInput])
        print("Success")
    



    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")










def changeBarcode():
    print("Change Barcode - Coming soon")
    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")











def changeDescription():
    lineInput = input("Barcode:")



    barcodePlaceholder = lineInput
    c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    descriptionEntry = c.fetchone()
    if (descriptionEntry == None):
        print("Barcode Not Found")
    else:
        descriptionEntry = str(descriptionEntry[0])


        print("The name of " + barcodePlaceholder + " is " + descriptionEntry)
        print("What did you want to rename it to??")
        lineInput = str(input(":"))

        c.execute('SELECT * FROM allItemsAndCodes WHERE barcode=?', [barcodePlaceholder])

        c.execute('UPDATE allItemsAndCodes SET description = ? WHERE barcode=?', (lineInput, barcodePlaceholder))
        conn.commit()
        print('Success')

    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")















def changePrice():
    lineInput = input("Barcode:")



    barcodePlaceholder = lineInput
    c.execute('SELECT price FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    priceEntry = c.fetchone()
    if (priceEntry == None):
        print("Barcode Not Found")
    else:
        priceEntry = str(priceEntry[0])

        c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?', [lineInput])
        descriptionEntry = c.fetchone()
        descriptionEntry = str(descriptionEntry[0])

        c.execute('SELECT priceIncrement FROM allItemsAndCodes WHERE barcode=?;',[lineInput])
        priceIncrementEntry=c.fetchone()
        priceIncrementEntry=int(priceIncrementEntry[0])


        if (priceIncrementEntry == 0):
            itemType = "per kg"
        else:
            itemType = "each"


        print("The current price for " + descriptionEntry + " is $" + priceEntry + " " + itemType)
        print("What did you want to change it to?")
        lineInput = input("$")
        if (check_float(lineInput) == True):

            lineInput=float(lineInput)

            if (lineInput == ""):
                print("No changes made. Returning to cl~")

            else:





                c.execute('SELECT * FROM allItemsAndCodes WHERE barcode=?', [barcodePlaceholder])

                c.execute('UPDATE allItemsAndCodes SET price = ? WHERE barcode=?', (lineInput, barcodePlaceholder))
                conn.commit()

                print('Success')

        else:
            print("Non Numeric number. Returning to cl~:")



    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")












def changeQuantity():
    lineInput = input("Barcode:")


    c.execute('SELECT  quantityInStock FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    quantityInStockEntry = c.fetchone()
    if (quantityInStockEntry == None):
        print("Barcode Not Found")

    else:
        quantityInStockEntry = str(quantityInStockEntry[0])
        barcodePlaceholder = lineInput


        c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?', [lineInput])
        descriptionEntry = c.fetchone()
        descriptionEntry = str(descriptionEntry[0])

        c.execute('SELECT priceIncrement FROM allItemsAndCodes WHERE barcode=?;',[lineInput])
        priceIncrementEntry=c.fetchone()
        priceIncrementEntry=int(priceIncrementEntry[0])



        if (priceIncrementEntry == 0):
            itemType = "kg"

        else:
            itemType = ""


            if (quantityInStockEntry == None):
                quantityInStockEntry = "0"
            else:


                quantityInStockEntry = str(quantityInStockEntry)


        print(quantityInStockEntry + itemType + " of " + descriptionEntry + " in stock")

        lineInput = input("cl/02/02~:")


        if (lineInput == "00"):
            lineInput = input("How many " + descriptionEntry + " in stock? :")

            c.execute('UPDATE allItemsAndCodes SET quantityInStock = ? WHERE barcode = ?',[lineInput, barcodePlaceholder])
            conn.commit()
            print('Success! Returning to cl~')


        elif (lineInput == "01"):
            lineInput = input("How many new " + descriptionEntry + " are there? :")


            c.execute('UPDATE allItemsAndCodes SET quantityInStock = ? WHERE barcode = ?',[str(float(lineInput)+float(quantityInStockEntry)), barcodePlaceholder])
            conn.commit
            print('Success! Returning to cl~')

        else:
            print("No changes made. Returning to cl~")

    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")















def changeIncrement():
    lineInput=input("Barcode:")

    c.execute("SELECT * FROM allItemsAndCodes WHERE barcode=?", [lineInput])
    a = c.fetchall()
    b = a[0]

    if (b[3] == 0):
        itemType = "kg"

    else:
        itemType = "item"


    print(str(b[1]) + " was measured per " + itemType)
    c.execute('UPDATE allItemsAndCodes SET priceIncrement = ? WHERE barcode = ?', [1-b[3], lineInput])
    if (1-b[3] == 0):
        itemType = "kg"

    else:
        itemType = "item"
    print(str(b[1]) + " is now measured per " + itemType)


    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")

















def checkStock():
    lineInput = input("cl/02/07~:")
    itemsInfo = []
    head = ["Description", "Barcode", "Price", "Quantity In Stock", "Price Increment", "Item Type"]





    if (lineInput == "00"):

        
        print("------+++++------+++++------+++++------+++++------+++++------")
        print("---All Items and Stock---")

        print(c.execute('SELECT description FROM allItemsAndCodes ORDER BY description ASC'))
        c.execute('SELECT * FROM allItemsAndCodes')

        row = c.fetchall()

        for row in c.fetchall():
            if(row[3]==0):
                priceIncrementEntry = "per kg"
            else:
                priceIncrementEntry = "each"

            for i in range(15):

                if(row[5]==i):
                    itemType =itemTypeArray[i]


            
            itemsInfo.append([row[1], row[0], "$"+str(row[2]), row[4], priceIncrementEntry, itemType])
        
            
        

            
            
        print(tabulate(itemsInfo, headers=head, tablefmt="fancy_grid", showindex=True))





    elif (lineInput == "01"):
        lineInput = input("Barcode:")


        c.execute('SELECT  * FROM allItemsAndCodes WHERE barcode=?', [lineInput])
        quantityInStockEntry = c.fetchall()
        if (quantityInStockEntry == None):
            print("Barcode Not Found")

        else:
            c.execute('SELECT  * FROM allItemsAndCodes WHERE barcode=?', [lineInput])
            for row in c.fetchall():
                if(row[3]==0):
                    priceIncrementEntry = "per kg"
                else:
                    priceIncrementEntry = "each"

                for i in range(15):

                    if(row[5]==i):
                        itemType =itemTypeArray[i]


            
            itemsInfo.append([row[1], row[0], "$"+str(row[2]), row[4], priceIncrementEntry, itemType])
        
            
        

            
            
        print(tabulate(itemsInfo, headers=head, tablefmt="fancy_grid", showindex=True))






        
    elif (lineInput == "02"):
        
        lineInput = input("Type of stock:")

        c.execute('SELECT * FROM allItemsAndCodes WHERE ItemType =?', [lineInput])

        for row in c.fetchall():
            if(row[3]==0):
                priceIncrementEntry = "per kg"
            else:
                priceIncrementEntry = "each"

            for i in range(15):

                if(row[5]==i):
                    itemType =itemTypeArray[i]


            
            itemsInfo.append([row[1], row[0], "$"+str(row[2]), row[4], priceIncrementEntry, itemType])
        
            
        

            
            
        print(tabulate(itemsInfo, headers=head, tablefmt="fancy_grid", showindex=True))





    else:
        print("No changes made. Returning to cl~")




    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")






































#Login
print("Welcome To Perkins POS")
while (loginLoop == 1):
    conn = sqlite3.connect('PerkinPOSDatabase')
    c = conn.cursor()
    lineInput = input("Login:")
    if (lineInput == "1111"):
        print("------+++++------+++++------+++++------+++++------+++++------")
        #Search
        mainLoop = 1
        while (mainLoop == 1):
            lineInput = input("cl~:")


            #Exact if statements


            ##Logout
            if (lineInput == "00"):
                conn.commit
                c.close()
                conn.close()
                mainLoop = 0



##Help menu
            elif(lineInput == "01"):

                    helpList = open('helpPage.txt', 'r')

                    print(helpList.read())
                    
                  
                    print("------+++++------+++++------+++++------+++++------+++++------")





##Edit database menu

            elif (lineInput == "02"):
                lineInput = input("cl/02~:")
                if (lineInput == "00"):
                    newItem()

                elif (lineInput == "01"):
                    delData()

                elif (lineInput == "02"):
                    changeBarcode()

                elif (lineInput == "03"):
                    changeDescription()

                elif (lineInput == "04"):
                    changePrice()

                elif (lineInput == "05"):
                    changeQuantity()

                elif (lineInput == "06"):
                    changeIncrement()

                elif(lineInput == "07"):
                    checkStock()

                else:
                    print("No changes made. Returning to cl~")
                    print("Type 01 and hit enter for the help page")





           ##Manager Menu
            elif (lineInput == "03"):
                print("Manager Menu - coming soon")
                print("No changes made. Returning to cl~")
                print("------+++++------+++++------+++++------+++++------+++++------")

            elif (lineInput == "04"):
                payForItem()










##Seach for barcode


            else:
                searchForItem(lineInput)










    elif (lineInput == "00"):

        loginLoop = 0



    else:

        print("XXXXXX")

print("Thank You for using Perkins POS")
