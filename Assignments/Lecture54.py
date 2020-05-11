def login():
    username = input("Username : ")
    password = input("Password : ")
    if (username == "Akasit" and password == "Tent"):
        return True
    else:
        return False
def showMenu():
    print("------IShop-----")
    print("ลำดับ รหัสสินค้า รายการ      ราคา ")
    print(" 1.   A01   Computer  17,000")
    print(" 2.   A02   Notebook  20,000")
def menuSelect():
    userSelected = input("ใส่รหัสสินค้า : ")
    return userSelected
def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice + (totalPrice * vat / 100)
    return result
def priceCalculate():
    price1 = int(input("first Product price: "))
    price2 = int(input("Second product prrice: "))
    return vatCalculate(price1 + price2)


while login() == False:
    print("login incorrect")
showMenu()
CodeMenu = menuSelect()
if CodeMenu == "A01":
    totalPrice = 17000
elif CodeMenu == "A02":
    totalPrice = 20000
else:
    "Not Found"

print("ราคาที่ต้องชำระ : ",vatCalculate(totalPrice))
