usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "TENT" and passwordInput == "0123" :
    print("------Welcome SHINO Store----------")
    print("ลำดับ  รหัสสินค้า   รายการ    ราคา(บาท)")
    print("1.     A01     Computer   20,000")
    print("2.     A02     Printer     3,500")
    Buy1  = input("เโปรดใส่่รหัสสินค้าที่จะซื้อ : ")
    Quan1 = int(input("จำนวน : "))
    if Buy1  == "A01" :
        Price1 = 20000*Quan1
        print("ยอดที่ต้องชำระ : ",Price1)
    elif Buy1  == "A02" :
        Price1 = 3500*Quan1
        print("ยอดที่ต้องชำระ : ",Price1)
