import clothing, stationery

class cart:
    def __init__(self) -> None:
        self.discount_amt = 0
        self.amt_to_pay = 0
        self.itemObjs = {}  #Contains string(Item name):Object(Item Obj) maps

    def addItem(self, item, quantity):
        itemObj = self.itemDecider(item) #Stores the right object

        #Checks max quantity rule
        if itemObj.quantity_purchased + int(quantity) <= itemObj.max_quantity:
            self.amt_to_pay += itemObj.price * int(quantity) #Update amt to pay
            itemObj.quantity_purchased += int(quantity) #Update the current purchased quantity of the item
            print("ITEM_ADDED")
        else:
            print("ERROR_QUANTITY_EXCEEDED") #max quantity rule violation
        pass
    
    def itemDecider(self, item):
        #Returns the object in the hashMap based ont the item string
        if item in self.itemObjs:
            return self.itemObjs[item]

        if item == "TSHIRT":
            self.itemObjs[item] = clothing.tshirt()
        elif item == "JACKET":
            self.itemObjs[item] = clothing.jacket()
        elif item == "CAP":
            self.itemObjs[item] = clothing.cap()
        elif item == "NOTEBOOK":
            self.itemObjs[item] = stationery.notebook()
        elif item == "PENS":
            self.itemObjs[item] = stationery.pen()
        elif item == "MARKER":
            self.itemObjs[item] = stationery.marker()
        else:
            print("ENTER_VALID_ITEM_NAME")
            exit(1)

        return self.itemObjs[item]

    def printBill(self):
        addDiscount = 0

        #Check if Discount applicable
        if self.amt_to_pay >= 1000:
            #Check if additional Discount applicable
            if self.amt_to_pay >= 3000:
                addDiscount = 5

            #print(f"total amount before discounts {self.amt_to_pay}")

            #Calculate discounts on individual items
            for item in self.itemObjs:
                itemObj = self.itemObjs[item]
                discount_amt = itemObj.price * itemObj.quantity_purchased * itemObj.discount / 100
                self.discount_amt += discount_amt

            #Discount the amount to pay
            self.amt_to_pay -= self.discount_amt
            #print(f"total amount after discounts {self.amt_to_pay}")

            #If additional discount applicable
            if addDiscount == 5:
                self.amt_to_pay -= self.amt_to_pay * addDiscount / 100
                #print(f"total amount after add. discount {self.amt_to_pay}")

        self.amt_to_pay += self.amt_to_pay * 0.1    #Taxes after discount is applied 
        
        self.amt_to_pay = round(self.amt_to_pay, 2)
        self.discount_amt = round(self.discount_amt, 2)

        print(f"TOTAL_DISCOUNT {self.discount_amt}\n" + f"TOTAL_AMOUNT_TO_PAY {self.amt_to_pay}")