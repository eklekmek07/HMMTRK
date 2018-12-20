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
def calc(bus = None):
    cd = time.strftime("%c")
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
    currentL = (2000,1,1,int(ch),int(cm),int(cs),1,1,1)
    currentT = time.mktime(currentL)    
    timedelta = 0 # bus time - current time
    count = 0 #bus number from 0 to how many buses on that b_list
    while timedelta <= 0: #I am trying to find when is the next bus
        bh, bm = b_list[count].split(".")
        busL = (2000,1,1,int(bh),int(bm),0,1,1,1)
        busT = time.mktime(busL)
        sub = busT - currentT
        if sub > 0:
            break
        count += 1
    return ("Remaining to {}: {}.{}".format(bus,round(sub//3600),floor(sub/60%60)))

