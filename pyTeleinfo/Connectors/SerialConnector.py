'''
Created on 2 juin 2013

@author: Hoareau
'''

import random
import serial


class SerialConnector():

   
    
    def __init__(self):
        
        #Variables initialization
        
        self.simu=False
        self.power=0
        self.currentH=""
        self.hp=0
        self.hc=0
        self.iinst=0
        self.nb=0
        
        #Try a serial connection
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 1200, bytesize=7, stopbits=1, parity=serial.PARITY_EVEN, rtscts=1)
        except:
            #If it fail we are in SimuMode
            self.simu = True;
                
    def retrievePower(self):
        if (self.simu==False):
            while True:
                self.line = self.ser.readline().decode('utf-8')
                if self.line:  # If it isn't a blank line
                    
                    if 'PAPP' in self.line:
                        self.power = int(self.line.split(" ")[1])
                        self.ser.close()
                        break        
                        
                
                
    # Retrieve all datas         
    def retrieveAllDatas(self):
        
        if (self.simu==False):


            while True:
                
                self.line = self.ser.readline().decode('utf-8')
                
                if self.line:  # If it isn't a blank line
                    
                    if 'PAPP' in self.line:
                        
                        self.nb=self.nb+1
                        
                        if self.nb<2 :
                            self.power = int(self.line.split(" ")[1])
    
                        else:
                            self.nb=0
                            self.ser.close()
                            break        
                        
                    if 'IINST' in self.line:
                        self.iinst = int(self.line.split(" ")[1])
                        
                    if 'HCHP' in self.line:
                        self.hp = int(self.line.split(" ")[1])
                        
                    if 'HCHC' in self.line:
                        self.hc = int(self.line.split(" ")[1])
                        
                    if 'OPTARIF' in self.line:
                        self.currentH = self.line.split(" ")[1]

    
    #Return the power
    def getPower(self):
        if self.simu:
            self.ret = random.randint(1,7000)
        else:
            self.ret= self.power
        return self.ret
        

    #Return the current period
    def getCurrentPeriod(self):
        
        if self.simu:
            self.ret = "-"
        else:
            self.ret= self.currentH
        return self.ret
        
    #Return the HP index 
    def getHP(self):
        
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.hp
        return self.ret
    
    #Return the HC index    
    def getHC(self):
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.hc
        return self.ret
    
    #Return the Current I
    def getIinst(self):
        
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.iinst
        return self.ret
            
        
    
