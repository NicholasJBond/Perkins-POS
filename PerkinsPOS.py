import sqlite3

conn = sqlite3.connect('PerkinPOSDatabase')
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS allItemsAndCodes(barcode TEXT, description TEXT, price REAL, priceIncrement REAL, quantityInStock REAL)') 

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
                        
def changePrice():
    lineInput = input("Barcode:")
    
    c.execute('SELECT price FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    priceEntry = c.fetchone()
    priceEntry = str(priceEntry[0])
    
    c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    descriptionEntry = c.fetchone()
    descriptionEntry = str(descriptionEntry[0])
    
    c.execute('SELECT priceIncrement FROM allItemsAndCodes WHERE barcode=?;',[lineInput])
    priceIncrementEntry=c.fetchone()
    priceIncrementEntry=priceIncrementEntry[0]
    
    if (priceIncrementEntry == 0):
            itemType = "per kg"
    else:
            itemType = "each"

            
    print("The current price for " + descriptionEntry + " is $" + priceEntry + " " + itemType)
    print("What did you want to change it to?")
    lineInput = input("$")
    c.execute('UPDATE allItemsAndCodes SET price = ?',[lineInput])
    print('Success')

def changeQuantity():
    lineInput = input("Barcode:")
    
    c.execute('SELECT  quantityInStock FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    quantityInStockEntry = c.fetchone()
    quantityInStockEntry = str(quantityInStockEntry[0])
    
    c.execute('SELECT description FROM allItemsAndCodes WHERE barcode=?', [lineInput])
    descriptionEntry = c.fetchone()
    descriptionEntry = str(descriptionEntry[0])


            
    print(quantityInStockEntry + " of " + descriptionEntry + " in stock")
    
    lineInput = input(":")

    if (lineInput == "00"):
        lineInput = input("How many " + descriptionEntry + " in stock? :")
        
        c.execute('UPDATE allItemsAndCodes SET quantityInStock = ?',[lineInput])
        print('Success! Returning to cl~')

    elif (lineInput == "01"):
        lineInput = input("How many new " + descriptionEntry + " are there? :")
        
        
        c.execute('UPDATE allItemsAndCodes SET quantityInStock = ?',[lineInput+quantityInStock])
        print('Success! Returning to cl~')

    else:
        print("No changes made. Returning to cl~")
    



#Login
print("Welcome To Perkins POS")
while (loginLoop == 1):
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
                    print("Commands:")
                    print("logout - logs out of your session")
                    print("new - creates a new item")
                    print("change price - changes the price of an item in the database")
                    print("change qty - changes the quantity of an item in the database")





##Edit database meny
                    
            elif (lineInput == "02"):
                lineInput = input("Action:")
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
        exit()
        loginLoop = 0
        
        

    else:
            
        print("XXXXXX")

    

    

