import serial
from serial import Serial
# import keyboard
# # while True:
try:
     ser = serial.Serial("COM8",9600)
     while True:
          data = ser.readline(1000)
          # print(data)
          Data1 = str(data)
          Data1 = Data1.replace("b'","")
          Data1 = Data1.replace("\\n","")
          Data1 = Data1.replace("\'","")
          Data1 = Data1.replace("\\r","")
          Data1 = Data1.replace("CM","")
          Data1=str(Data1)
          distance = float(Data1)
          # print(distance)
          height = 18
          radious = 4.3
          capacity_of_well = 3.14*(radious**2)*(height)
          volume_of_well = 3.14*(radious*radious)*(height-distance)
          percent_filled =(volume_of_well/capacity_of_well*100)
          print(percent_filled)
          # Data = str(data)
          # print(Data1)
          f = open("t.txt", "w")
          f.write(f"{percent_filled}")
except:   
     print("Data not found")

# print(data)
# ser = serial.Serial(port="COM8",baudrate="9600",bytesize=8,timeout=2,stopbits=serial.STOPBITS_ONE)
# data = ser.readline(1000)


# while True:

#      if keyboard.is_pressed('q'):
#           print("Quit?")
#           break


# ser.close()













