menuList = []
priceList = []
priceTotal = 0

def showBill():
    global priceTotal
    print("---- My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
        priceTotal = priceTotal + int(priceList[number])
    print("price Total = ",priceTotal)
while True:
    menuName = input("Plese Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()