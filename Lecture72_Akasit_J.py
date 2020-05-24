menuList = []
priceList = []
priceTotal = 0

def showBill():
    global priceTotal
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number])
        priceTotal = priceTotal + int(menuList[number][1])
    print("price Total = ",priceTotal)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
        #priceList.append(menuPrice)

showBill()