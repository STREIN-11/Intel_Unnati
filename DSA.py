import serial
from serial import Serial
import time
import Water_AI
import pyfirmata
import Callibrartion

ptime=time.time()
ctime=time.time()
flag=0

d=[]
time_period=-1
AI=Water_AI.waterAI()
callibration=Callibrartion.callibration()

# bord = pyfirmata.Arduino("COM11")

# bord.digital1[13].mode = pyfirmata.OUTPUT
# bord.digital1[13].write(0)
# bord.digital2[12].mode = pyfirmata.OUTPUT
# bord.digital2[12].write(0)
# bord.digital3[9].mode = pyfirmata.OUTPUT   
# bord.digital3[9].write(0)

cap_p1 = 0
cap_p2 = 0
cap_w1 = 0

# # while True:
try:
     ser = serial.Serial("COM5",9600)
     ser1 = serial.Serial("COM6",9600)
     # p_moist=ser.readline().decode()
     # x=p_moist.split(',')

     # P_M=float(x[2])
     # ser.write(b'g')
     # time.sleep(5)
     # ser.write(b'u')
     # C_moist=ser.readline().decode()
     # y=C_moist.split(',')

     # C_M=float(x[2])8

     # m_rate=(C_M-P_M)/5
     m_rate=0.4
     

     while True:
          f1 = open("kill.txt", "r")
          var = int(f1.readline())
          if var==1:
               f = open("save2.txt", "r")
               user_time=float(f.readline())
               f.close()
               f = open("save1.txt", "r")
               low_threshold=float(f.readline())
               f.close()
               f = open("save.txt", "r")
               high_threshold=float(f.readline())
               f.close()
               data = ser.readline()
               data = data.decode()
               # print(data)s
               # data2 = ser2.readline()
               waterSource=[0,0,0]
               # data2 = data2.decode()
               Data = str(data)
               # print(Data)
               # Data2 = str(data2)
               # Data = Data.replace("b'","")
               # Data = Data.replace("\\n","")
               # Data = Data.replace("\'","")
               
               # Data2 = Data2.replace("b'","")
               Data = Data.replace("\\n","")
               # Data2 = data2.replace("\'","")
               d = Data.split(",")
               # print(d)
               # waterSource = waterSource.remove(waterSource[2])
               # print(waterSource)
               # print(Data)
               # l = Data.split(",")

               # print([float(x) for x in l])
               A = [float(x) for x in d]

               print(A)
               cap_p1 = A[0]
               cap_p2 = A[1]
               cap_w1 = A[2]
               with open("cap_p1.txt","w") as f1:
                    distance1 = A[0]
                    height1 = 16
                    radious1 = 43/(2*3.1416)
                    capacity_of_well1 = 3.14*(radious1**2)*(height1)
                    volume_of_well1 = 3.14*(radious1*radious1)*(height1-distance1)
                    percent_filled1 =(volume_of_well1/capacity_of_well1*100)
                    Percent_filled1 = str(percent_filled1)
                    print('close system : ',percent_filled1)
                    f1.write(Percent_filled1)
                    waterSource[0] = float(percent_filled1)
               with open("cap_w1.txt","w") as f3:
                    distance = A[1]
                    height = 16
                    radious = 4.3
                    capacity_of_well = 3.14*(radious**2)*(height)
                    volume_of_well = 3.14*(radious*radious)*(height-distance)
                    percent_filled =(volume_of_well/capacity_of_well*100)
                    Percent_filled = str(percent_filled)
                    print('well : ',percent_filled)
                    f3.write(Percent_filled)
                    waterSource[1] = float(percent_filled)
               with open("cap_p2.txt","w") as f2:
                    distance2 = A[2]
                    height2 = 5
                    down = 12
                    up = 14
                    avg_side=up+down/2
                    area = avg_side*avg_side
                    vol = area*(height2-distance2)
                    capacity=area*height2
                    percent_filled2 =(vol/capacity*100)
                    Percent_filled2 = str(percent_filled2)
                    print("Pond : ",percent_filled2)
                    f2.write(Percent_filled2)
                    waterSource[2] = float(percent_filled2)
               print(d[3])    
               callibrated_Value=callibration.LM393(float(d[3]))
               print(callibrated_Value)
               with open("soil_m.txt","w") as f3:
                    f3.write(str(callibrated_Value))
               # with open("hum.txt","w") as f3:
               #      f3.write(d[4])
               # with open("temp.txt","w") as f3:
               #      f3.write(d[5])

               
               # waterSource = waterSource.append(x for x in )
               # waterSource.append(cap_p1)
               # waterSource.append(cap_p2)
               # waterSource.append(cap_w1)
               # print(waterSource)
               
               on_time=ctime-ptime
               # hum_str = l[0]
               # # hum = float(hum)
               # print(hum)
               # for any use of var use A list as it's already converted into a float list
               # print(type(A[0]))
               # print(A)
               if(callibrated_Value<low_threshold and flag==0):
                    times=AI.latency(high_threshold,low_threshold,user_time,callibrated_Value,m_rate)
                    ontime_perCycle=float(times[0])
                    offtime_perCycle=float(times[1])
                    
                    # offtime_perCycle=-12
                    # if offtime_perCycle<0:
                    #      f = open("kill.txt", "w")
                    #      f.write("0")

                    time_period=float(ontime_perCycle + offtime_perCycle)
                    flag=1
                    print("times: ",times)
                    
                    
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
               # offtime if
               # if offtime_perCycle>0:
               #      f = open("offtime.txt", "w")
               #      f.write("0")
               #      f.close()
               #      time.sleep(1)
               if callibrated_Value<low_threshold and on_time<(ontime_perCycle):
                    ctime=time.time()
                    print("Ontime : ",on_time)
                    source=AI.find_source(waterSource)
                    print(source)
                    if source==0:
                         ser1.write(b'g')
                         f = open("motor.txt", "w")
                         f.write("0")
                         f.close()
                         # bord.digital[13].write(1)
                    elif source==1:
                         ser1.write(b'v')
                         f = open("motor.txt", "w")
                         f.write("1")
                         f.close()
                         # bord.digital[12].write(1)
                    elif source==2:
                         ser1.write(b'b')
                         print("fhggjhjhj")
                         f = open("motor.txt", "w")
                         f.write("2")
                         f.close()
                    

                         # bord.digital[9].write(1)
                    # with open("motor.txt","w") as f3:
                    #      f3.write('1')
                    # bord.digital[0].write(1)
               else:
                    ser1.write(b'u')
                    # bord.digital[13].write(0)
                    # bord.digital[12].write(0)
                    # bord.digital[9].write(0)
                    print("Ontime : ",on_time)
                    if on_time>=(time_period):
                         ptime=ctime
                    if callibrated_Value>low_threshold:
                         ptime,ctime=time.time(),time.time()
                         f = open("motor.txt", "w")
                         f.write("3")
                         flag=0
                    ctime=time.time()
               # else:
               #      f = open("offtime.txt", "w")
               #      f.write("1")
               #      f.close()
                    # with open("motor.txt","w") as f3:
                    #      f3.write('0')
                    
                    # bord.digital[0].write(0)
          else:
               exit()
except Exception as e:
     print(e)

















































