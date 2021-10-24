import sqlite3


conn = sqlite3.connect('PerkinPOSDatabase')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL, priceIncrement INT, quantityInStock REAL)') 

barcodeEntry = "0"
descriptionEntry = "0"
priceEntry = 0
priceIncrementEntry = 0
quantityInStockEntry = 0

priceTotalList = [0]
barcodeList = [0]
quantityList = [0]
itemType = "0"

lineInput = 0
loginLoop = 1
mainLoop = 0







##Functions

def searchForItem(bcode):
    c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?;',[bcode])
    descriptionEntry=c.fetchone()
    
    if (descriptionEntry == None):
        print("Barcode Not Found")

    else:

    
        c.execute('SELECT price FROM allItemsAndCodes WHERE barcode=?;',[bcode])
        priceEntry=c.fetchone()

        c.execute('SELECT priceIncrement FROM allItemsAndCodes WHERE barcode=?;',[bcode])
        priceIncrementEntry=c.fetchone()
        priceIncrementEntry=int(priceIncrementEntry[0])
        
        if (priceIncrementEntry == 0):
            itemType = "per kg"
        else:
            itemType = "each"

        priceTotalList.append(priceEntry)
        barcodeList.append(bcode)

        print("1x " + str(descriptionEntry[0]) + " at $" + str(priceEntry[0]) + " " + itemType)

    
              


def newItem():
    barcodeEntry = input("Type the barcode of the new item and then press enter:")
    descriptionEntry = input("Type the description/name of the new item and then press enter:")
    priceEntry = input("Type the price of the new item. Do not include the $ sign:")
    priceIncrementEntry = input("If measured by weight enter (0) if it is per item enter (1):")
    quantityInStockEntry = 0
    c.execute("INSERT INTO allItemsAndCodes(barcode, description, price, priceIncrement, quantityInStock) VALUES (?, ?, ?, ?, ?)",
                                  (barcodeEntry, descriptionEntry, priceEntry, priceIncrementEntry, quantityInStockEntry))
    conn.commit()
    print(descriptionEntry + " with an access code of " + barcodeEntry + " has successfully been added to the database with a price of $" + priceEntry + " per increment.")
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
        lineInput = float(input("$"))
           
        c.execute('SELECT * FROM allItemsAndCodes WHERE barcode=?', [barcodePlaceholder])
            
        c.execute('UPDATE allItemsAndCodes SET price = ? WHERE barcode=?', (lineInput, barcodePlaceholder))
        conn.commit()
        print('Success')
            
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
            conn.commit
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
    





def delData():
    print("No changes made. Returning to cl~")
    conn.commit()
    print("------+++++------+++++------+++++------+++++------+++++------")


def checkStock():
    lineInput = input("cl/02/05~:")
    if (lineInput == "00"):
        
       
        

            
        c.execute('SELECT * FROM allItemsAndCodes')

        print("------+++++------+++++------+++++------+++++------+++++------")
        print("---All Items and Stock---")
        for row in c.fetchall():
            
            if (row[3] == 0):
                itemType = "kg"
            else:
                itemType = ""
            print(str(row[1]) + ":")
            print(str(row[4]) + str(itemType))
            print("")

            
         

    elif (lineInput == "01"):
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
    if (lineInput == "010209"):
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

           
                    print("Help Page:")
                    print("cl~:")
                    print("00 - Log Out")
                    print("01 - Help Page")
                    print("02 - Edit database")
                    print("03 - Manager menu")
                    print("cl/02~:")
                    print("00 - new entry")
                    print("01 - change price")
                    print("02 - change quantity in stock")
                    print("03 - change description")
                    print("04 - change pricing type")
                    print("05 - check stock")
                    print("------+++++------+++++------+++++------+++++------+++++------")





##Edit database menu
                    
            elif (lineInput == "02"):
                lineInput = input("cl/02~:")
                if (lineInput == "00"):
                    newItem()
                            
                elif (lineInput == "01"):
                    changePrice()

                elif (lineInput == "02"):
                    changeQuantity()

                elif (lineInput == "03"):
                    print("Change Description")
                    print("No changes made. Returning to cl~")

                elif (lineInput == "04"):
                    print("Delete Item")
                    print("No changes made. Returning to cl~")
                    
                elif (lineInput == "05"):
                    checkStock()
                    
                elif (lineInput == "06"):
                    print("Delete Item")
                    print("No changes made. Returning to cl~")

                else:
                    print("No changes made. Returning to cl~")
                    print("Type 01 and hit enter for the help page")





           ##Manager Menu         
            elif (lineInput == "03"):
                print("Manager Menu")
                
                
                    

                            





##Seach for barcode

                                
            else:
                searchForItem(lineInput)

            

                


        


            
    elif (lineInput == "00"):
        
        loginLoop = 0
        
        

    else:
            
        print("XXXXXX")

print("Thank You for using Perkins POS")

    

    

