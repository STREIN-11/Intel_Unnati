import tkinter as tk
import time
import serial
import threading
import continuous_threading

ser = serial.Serial("COM7",9600)

val = 0
index=[]

def readSerial():
     data = ser.readline()
     Data = str(data)
     Data = Data.replace("b'","")
     Data = Data.replace("\\n","")
     Data = Data.replace("\'","")
     print(Data)
     l = Data.split(",")
     # print([float(x) for x in l])
     A = [float(x) for x in l]
     # global val
     # ser_bytes = ser.readline()
     # ser_bytes = ser_bytes.decode("utf-8")
     # val = ser_bytes
     # index.append(val)

     # if len(index) == 1:
     display1 = tk.Label(root,text=A[1]).place(x=50,y=10)
     # elif len(index) == 2:
     display2 = tk.Label(root,text=A[0]).place(x=50,y=40)
     # if len(index) == 2:
     #      index.clear()

t1 = continuous_threading.PeriodicThread(0.5,readSerial)



root = tk.Tk()
root.geometry("300x250")
temp = tk.Label(root,text="Temp.").place(x=10,y=10)
hum = tk.Label(root,text="Hum.").place(x=10,y=40)
t1.start()



root.mainloop()



























