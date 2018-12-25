#fix which b_lists error
import time
from math import floor
#work in progres.. the program that shows how many minutes to next coming rk for Sarıtepe Campus

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
        self.current_time = None
        self.target_bus_time = None
        self.current_day = time.strftime("%c")
        self.remaning_time = None
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
        count = 0
        while True:
            bh, bm = self.used_list[count].split(".")
            busL = (1971,0,0,int(bh),int(bm),0,0,0,0)
            busT = time.mktime(busL)
            sub = busT - self.current_time
            print(sub)
            if sub > 0:
                self.target_bus_time = busT
                break
            count += 1
            if len(self.used_list) == count:
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

    def print_bus(self):
        self.remaing_time = self.target_bus_time - self.current_time
        print("target",self.target_bus_time)
        print("kalan saniye",self.remaing_time)
    def bus_return(self):
        self.remaing_time = self.target_bus_time - self.current_time
        try:
            return (self.remaning_time//3600,floor(self.remaning_time/60%60))
        except TypeError:
            return (floor(self.remaning_time/60%60))
        
#,floor(self.remaning_time/60%60)
    def next_bus(self):
        pass
rk = bus("RK",rk_week,rk_sat,rk_sun)
rk.closest_bus()
def calc(bus = None):
    cd = time.strftime("%c")
    if cd == "Fri":
        pass
    elif cd == "Sat":
        pass
    elif cd == "Sun":
        
        pass
    if bus == "rk":
        if cd == "Sun":
            b_list = rk_sun
        elif cd == "Sat":
            b_list = rk_sat
        else:
            b_list = rk_week
    elif bus == "hs":
        if cd == "Sun":
            b_list = hs_sun
        elif cd == "Sat":
            b_list = hs_sat
        else:
            b_list = hs_week
    elif bus == "mekikA":
        if cd == "Sun" or "Sat":
            b_list = mekikA_end
        else:
            b_list = mekikA_week
    elif bus == "mekikZ":
        if cd == "Sun" or "Sat":
            b_list = mekikZ_end
        else:
            b_list = mekikZ_week

    cm = time.strftime("%M")
    ch = time.strftime("%H")
    cs = time.strftime("%S") 
    currentL = (1971,0,0,int(ch),int(cm),int(cs),0,0,0)
    currentT = time.mktime(currentL)    
    timedelta = 0 # bus time - current time
    count = 0 #bus number from 0 to how many buses on that b_list
    while timedelta <= 0: #I am trying to find when is the next bus
        bh, bm = b_list[count].split(".")
        busL = (1971,0,0,int(bh),int(bm),0,0,0,0)
        busT = time.mktime(busL)
        sub = busT - currentT
        if sub > 0:
            break
        count += 1
        if len(b_list) == count:
            return ("Next {} is tomorrow at {}".format(bus ,b_list[0]))
    return ("Remaining to {}: {}.{}".format(bus,round(sub//3600),floor(sub/60%60)))
