import serial
from serial import Serial



# bord = pyfirmata.Arduino('COM7')
# bord.digital[0].mode = pyfirmata.OUTPUT
# bord.digital[0].write(0)


# # while True:
try:
     ser = serial.Serial("COM7",9600)
     while True:
          
          data = ser.readline()
          print(data)
          Data = str(data)
          Data = Data.replace("b'","")
          Data = Data.replace("\\n","")
          Data = Data.replace("\'","")
          print(Data)
          l = Data.split(",")
          # print([float(x) for x in l])
          A = [float(x) for x in l]
          # hum_str = l[0]
          # # hum = float(hum)
          # print(hum)
          # for any use of var use A list as it's already converted into a float list
          # print(type(A[0]))
          print(A)
          # print(l[1])
          # print(l[2])
          # hum = float(l[0])
          # with open("hum.txt","w") as f:
          #      f.write(l[0])
 
          # with open("temp.txt","w") as f1:
          #      f1.write(l[1])
          # with open("soil_m.txt","w") as f2:
          #      f2.write(l[2])
          # f.close()
          # f1.close()
          # f2.close()
          # ser.write(1,"high")
          if A[2]<10:
               ser.write(b'g')
               with open("motor.txt","w") as f3:
                    f3.write('1')
               # bord.digital[0].write(1)
          else:
               ser.write(b'u')
               with open("motor.txt","w") as f3:
                    f3.write('0')
               
               # bord.digital[0].write(0)
except Exception as e:
     print(e)