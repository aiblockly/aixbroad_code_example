
#由于megapi涉及多线程，请在终端中执行此脚本，请勿直接在idle中运行！
import time
from megapi import *

class MBOT_MEGA:
    def __init__(self,portName,wheelports_lf_lb_rf_rb=[1,9,10,2]):
        self.mbot = MegaPi()
        self.mbot.start(portName)
        self.wheelports = wheelports_lf_lb_rf_rb

    def __del__(self):
        self.mbot.close()
        self.mbot.exiting = True

    def run(self,direction="forward",speed=100):
        if direction=="forward":
            speedList = [i*speed for i in [-1,-1,1,1]]
        elif direction=="back":
            speedList = [i*speed for i in [1,1,-1,-1]]
        elif direction=="turn_left":
            speedList = [i*speed for i in [1,1,1,1]]
        elif direction=="turn_right":
            speedList = [i*speed for i in [-1,-1,-1,-1]]
        elif direction=="move_left":
            speedList = [i*speed for i in [-1,1,-1,1]]
        elif direction=="move_right":
            speedList = [i*speed for i in [1,-1,1,-1]]
        else:
            speedList = [0,0,0,0]           
        self.mbot.motorRun(self.wheelports[0],speedList[0])
        self.mbot.motorRun(self.wheelports[1],speedList[1])
        self.mbot.motorRun(self.wheelports[2],speedList[2])
        self.mbot.motorRun(self.wheelports[3],speedList[3])
        
    def stop(self):
        self.mbot.motorRun(self.wheelports[0],0)
        self.mbot.motorRun(self.wheelports[1],0)
        self.mbot.motorRun(self.wheelports[2],0)
        self.mbot.motorRun(self.wheelports[3],0)

if __name__ == "__main__":
    a = MBOT_MEGA("/dev/ttyUSB0",[1,9,10,2])
    time.sleep(3)
    for d in ["forward","back","turn_left","turn_right","move_left","move_right"]:
        a.run(d,100)
        time.sleep(3)
    a.stop()
    time.sleep(3)
    del a
