'''
Created on 2 juin 2013

@author: Hoareau
'''

import Util
import random
import serial


class SerialConnector():


    
    def __init__(self):
        
        #Variables initialization
        
        self.simu=False
        self.datas={}
        
        #Try a serial connection
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 1200, bytesize=7, stopbits=1, parity=serial.PARITY_EVEN, rtscts=1)
        except:
            #If it fail we are in SimuMode
            self.simu = True;
                
                
    def retrieve(self,tag):
        if (self.simu==False):
            while True:
                self.line = self.ser.readline().decode('utf-8')
              
                if self.line:  # If it isn't a blank line
                    print self.line
                    if tag in self.line:
                        self.value = self.line.split(" ")[1]
                        print self.value
                        self.ser.close()
                        self.datas[tag]=self.value
                        break        
                
                
    # Retrieve all datas         
    def retrieveAllDatas(self):
        
        if (self.simu==False):


            while True:
                
                self.line = self.ser.readline().decode('utf-8')
                
                if self.line:  # If it isn't a blank line
                    
                    if Util.POWER_TAG in self.line:
                        
                        self.nb=self.nb+1
                        
                        if self.nb<2 :
                            self.power = int(self.line.split(" ")[1])
    
                        else:
                            self.nb=0
                            self.ser.close()
                            break        
                        
                    if Util.IINST_TAG in self.line:
                        self.datas[Util.IINST_TAG]=int(self.line.split(" ")[1])
                        
                    if Util.HP_TAG in self.line:
                        self.datas[Util.HP_TAG]=int(self.line.split(" ")[1])
                        
                    if Util.HC_TAG in self.line:
                        self.datas[Util.HC_TAG]=int(self.line.split(" ")[1])
                        
                    if Util.CURRENTH_TAG in self.line:
                        self.datas[Util.CURRENTH_TAG]=self.line.split(" ")[1]



    def get(self,tag):
        
        if self.simu:
            self.ret = random.randint(1,7000)
        else:
            self.ret= self.datas[tag]
        print "serial data ="+str(self.ret)
        return self.ret

