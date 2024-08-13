import tkinter as tk
import time
import serial
import threading
import continuous_threading
# from tkinter import * 
from tkinter import messagebox
from twilio.rest import Client
from tkinter import *


acc_sid = "AC708aaa8c9555929c7d9bc937e8d2dd47"
auth_token = "baeffbc9a4b94b5f6656cb8b30f14ad1"


val = 0
index=[]

# def change_text():
#      ref.con

def readSerial():
     try:
          ser = serial.Serial("COM1",9600)
          data = ser.readline()
          Data = str(data)
          Data = Data.replace("b'","")
          Data = Data.replace("\\n","")
          Data = Data.replace("\'","")
          print(Data)
          l = Data.split(",")
          # print([float(x) for x in l])
          A = [float(x) for x in l]
          display2 = tk.Label(root,text=A[0]).place(x=70,y=40)
          display1 = tk.Label(root,text=A[1]).place(x=70,y=10)
          canvas = Canvas(root, width=450, height=240)
          canvas.pack()
          # rectangle = canvas.create_rectangle(100, 100, 400, 400, fill='orange')
          global ref
          # ref = tk.Label(root,text=f"Moisture level is low").place(x=110,y=70)
          if A[2]<10:
               # canvas.itemconfig(rectangle, fill='red')
               # messagebox.showinfo("showinfo", "Alert Water Moisture is very low")
               # client = Client(acc_sid,auth_token)
               # msg = client.messages.create(body="hello",
               #      from_= "+19499903573",
               #      to="+919800866506"
               # )
               # print(msg.sid)
               a1 = tk.Label(root,text="Moisture level is low").place(x=110,y=70)
               a2 = tk.Label(root,text="Please Give Water to the soil",bg="red").place(x=110,y=170)
               
          elif A[2]>10 and A[2]<40:
               b1 = tk.Label(root,text="Moisture level is Mid").place(x=110,y=70)
               b2 = tk.Label(root,text="                                                      ").place(x=110,y=170)
               # canvas.itemconfig(rectangle, fill='blue')
          elif A[2]>40 and A[2]<100:
               c1 = tk.Label(root,text="Moisture level is high").place(x=110,y=70)
               c2 = tk.Label(root,text="                                                       ").place(x=110,y=170)
               # canvas.itemconfig(rectangle, fill='green')

     except Exception as e:
          print(e)
     try:
          ser1 = serial.Serial("COM1",9600)
          data1 = ser1.readline()
          Data1 = str(data1)
          Data1 = Data1.replace("b'","")
          Data1 = Data1.replace("\\n","")
          Data1 = Data1.replace("\'","")
          Data1 = Data1.replace("\\r","")
          Data1 = Data1.replace("CM","")
          Data1=str(Data1)
          print("Distance is: ",Data1)
          # l1 = Data1.split(",")
          # tk.Label(root,text=Data1).place(x=170,y=170)
          distance = float(Data1)
          # print(distance)
          height = 20
          radious = 4
          volume_of_well = 3.14*(radious*radious)*(height-distance)
          print("Volume of Well is: ",volume_of_well)

     except Exception as e:
          print(e)

t1 = continuous_threading.PeriodicThread(0.5,readSerial)



root = tk.Tk()
root.geometry("700x450")
root.resizable(True, True)
temp = tk.Label(root,text="Temp:- ").place(x=10,y=10)
hum = tk.Label(root,text="Hum:- ").place(x=10,y=40)
hum = tk.Label(root,text="Soil Moisture:- ").place(x=10,y=70)


t1.start()

root.mainloop()



























