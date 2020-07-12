from tkinter import *
import math
def leftClickButton(event) :

   result = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)

   if result >= 30.0:
        labelResult.configure(text= (int(result),"อ้วนมาก"),fg= "red")
   elif result >= 25.0:
        labelResult.configure(text= (int(result),"อ้วน"),fg="red")
   elif result >= 23.0:
        labelResult.configure(text= (int(result),"น้ำหนักเกิน"))
   elif result >= 18.6:
        labelResult.configure(text= (int(result),"น้ำหนักปกติ"))
   else:
        labelResult.configure(text= (int(result),"ผอมเกินไป"))

MainWindow = Tk()

labelHight = Label(MainWindow,text="ส่วนสูง (cm)")
labelHight.grid(row=0,column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid (row=0,column=1)
labelweight = Label(MainWindow,text="น้ำหนัก (Kg)")
labelweight.grid(row=1,column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
CalculateButton = Button(MainWindow,text="คำนวณ")
CalculateButton.bind('<Button-1>',leftClickButton)
CalculateButton.grid(row=2,column=0)
labelResult = Label(MainWindow,text="ผลลัพธ์")
labelResult.grid(row=2,column=1)
MainWindow.mainloop() 
