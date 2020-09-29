from tkinter import *
import math

def leftClickButton(event):
    BMI = (float(textBoxWeight.get())/math.pow(float(textBoxHight.get())/100,2))
    if BMI >= 30:
        BMIResult = "คุณอ้วนเกินไป"
    elif 25.0 < BMI and BMI < 29.9:
        BMIResult = "คุณอ้วนแล้วน่ะ"
    elif 23.0 < BMI and BMI < 24.9:
        BMIResult = "คุณน้ำหนักเกิน"
    elif 18.6 < BMI and BMI < 22.9:
        BMIResult = "คุณน้ำหนักปกติ เหมาะสม"
    elif BMI >= 18.5:
        BMIResult = "คุณผอมเกินไป"
    labelResult.configure(text = BMIResult)

MainWindow = Tk()
labelHight = Label(MainWindow, text = "ส่วนสูง (cm.)")
labelHight.grid(row = 0, column = 0)

textBoxHight = Entry(MainWindow)
textBoxHight.grid(row = 0, column = 1)

labelWeight = Label(MainWindow, text = "น้ำหนัก (kg.)")
labelWeight.grid(row = 1, column = 0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row = 1, column = 1)

calculateButton = Button(MainWindow, text = "คำนวณ")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row = 2, column = 0)

labelResult = Label(MainWindow,text = "ผลลัพธ์",bg = "yellow")
labelResult.grid(row = 2, column = 1)

MainWindow.mainloop()