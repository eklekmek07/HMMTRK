import time
from math import floor

rk_week = ("07.00", "08.00", "09.00", "09.55", "10.35", "12.15", "13.05", "13.50", "14.55", "15.35", "16.15", "17.30", "18.35", "19.15", "20.35", "21.15", "22.00", "23.55")
rk_sat = ("07.20", "08.45", "10.00", "11.10", "12.25", "13.40", "15.00", "16.15", "17.45", "19.15", "20.35", "21.50", "23.55")
rk_sun = ("08.45", "11.15", "13.45", "16.15", "19.15", "19.45", "21.50","22.15", "23.55")
hs_week = ("08.30","10.15","12.40","16.35","18.10","20.00","21.40")
hs_sat = ("08.15","14.00","15.45","17.40")
hs_sun = ("12.50","14.40","16.30","18.20")
mekikA_week = ("08.00","14.00","15.30","16.30")
mekikA_end = ("10.00","16.00")
mekikZ_week = ("13.00","14.30","19.00")
mekikZ_end = ("11.00","13.30")

class bus():    
    def __init__(self ,name ,week , sat, sun):
        self.name = name
        self.time_week = week
        self.time_sat = sat
        self.time_sun = sun
        self.current_time = 0
        self.target_bus_time = 0
        self.current_day = time.strftime("%c")
        self.remaining_time = 0
        self.bus_count = 0
        if self.current_day == "Sat":
            self.used_list = self.time_sat
        elif self.current_day == "Sun":
            self.used_list = self.time_sun
        else:
            self.used_list = self.time_week
    
    def update_time(self):
        cm = time.strftime("%M")
        ch = time.strftime("%H")
        cs = time.strftime("%S") 
        timelist = (1971,0,0,int(ch),int(cm),int(cs),0,0,0)
        self.current_time = time.mktime(timelist)
        print("current", self.current_time)

    def closest_bus(self):
        self.update_time()
        while True:
            bh, bm = self.used_list[self.bus_count].split(".")
            busL = (1971,0,0,int(bh),int(bm),0,0,0,0)
            busT = time.mktime(busL)
            self.sub = busT - self.current_time
            print(self.sub)
            if self.sub > 0:
                self.target_bus_time = busT
                print("busT",busT)
                break
            self.bus_count += 1
            if len(self.used_list) == self.bus_count:
                if self.current_day == "Fri":
                    bh, bm = self.time_sat[0].split(".")
                    busL = (1971,0,1,int(bh),int(bm),0,0,0,0)
                    self.target_bus_time = time.mktime(busL)
                if self.current_day == "Sat":
                    bh, bm = self.time_sun[0].split(".")
                    busL = (1971,0,1,int(bh),int(bm),0,0,0,0)
                    self.target_bus_time = time.mktime(busL)
                if self.current_day == "Sun":
                    bh, bm = self.time_week[0].split(".")
                    busL = (1971,0,1,int(bh),int(bm),0,0,0,0)
                    self.target_bus_time = time.mktime(busL)
                break

    def bus_return(self):
        self.remaining_time = self.target_bus_time - self.current_time
        return round(self.remaining_time // 3600) , floor(self.remaining_time / 60 % 60)
    
    def next_bus(self):
        self.update_time()
        self.bus_count += 1
        bh, bm = self.used_list[self.bus_count].split(".")
        busL = (1971,0,0,int(bh),int(bm),0,0,0,0)
        busT = time.mktime(busL)
        self.sub = busT - self.current_time
        

hs = bus("HS",hs_week,hs_sat,hs_sun)
rk = bus("RK",rk_week,rk_sat,rk_sun)
rk.closest_bus()
print(rk.bus_return())
def rk_calc(n = 0): #n as bus number
    rk.closest_bus()
    rk.bus_count += n
    return rk.bus_return()
print(rk_calc(1))

