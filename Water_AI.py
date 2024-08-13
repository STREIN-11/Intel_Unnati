waterType=("ponds","Well","BoreWell")

waterSource= [0.8,0.7,0.65,0.85]



class waterAI:
    # def __init__(self,waterSource,m_high=0,m_low=0,time=0,m_val=0,pump_power=0):
    #     self.waterSource = waterSource
    #     self.m_high = m_high
    #     self.m_low = m_low
    #     self.time = time
    #     self.m_val=m_val
    #     self.power = pump_power
    def find_source(self,waterSource):
        self.waterSource=waterSource
        return (self.waterSource.index(max(self.waterSource)))
    def latency(self,m_high,m_low,app_time,m_val,m_rate):
            import time
            self.m_low=m_low
            self.m_high=m_high
            self.m_val=m_val
            self.time=app_time
            
            self.m_rate=m_rate
            target=(self.m_high+self.m_low)/2
            self.m_diff = target-self.m_val
            # ctime=time.time()
            # ptime=time.time()
            # self.period=ctime-ptime
            # self.t_diff=self.time
            self.ontime=self.m_diff/self.m_rate
            self.off_time=self.time-self.ontime
            x=1
            y=1
            for i in range(2,11):
                if int(self.ontime)%i==0:
                    x=i
                    if x>3:
                        break
                # elif self.off_time/i==0:
                #     y=i
            n=self.ontime/(x)
            y=self.off_time/n    
            # return_time=(10*self.m_diff/100)/self.m_rate
            print(x,y,i,self.ontime,self.off_time)
            output=[x,y]
            return output




# AI=waterAI()
# print(AI.latency(10,5,40,3.3989379991719844,0.4))