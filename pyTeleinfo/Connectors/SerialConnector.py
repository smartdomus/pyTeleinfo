'''
Created on 2 juin 2013

@author: Hoareau
'''
import serial


class SerialConnector():

   
    
    def __init__(self):
        
        self.simu=False
        
        self.power=0
        self.currentH=""
        self.hp=0
        self.hc=0
        self.iinst=0
        self.nb=0
        
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 1200, bytesize=7, stopbits=1, parity=serial.PARITY_EVEN, rtscts=1)
        except:
            self.simu = True;
                #print 'error while opening serial communication'
                
                
                
                
    def getDatas(self):
        
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

    
    def getPower(self):
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.power
        return self.ret
        

    
    def getCurrentH(self):
        
        if self.simu:
            self.ret = "-"
        else:
            self.ret= self.currentH
        return self.ret
        
        
    def getHP(self):
        
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.hp
        return self.ret
    
        
    def getHC(self):
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.hc
        return self.ret
    
    def getIinst(self):
        
        if self.simu:
            self.ret = 0
        else:
            self.ret= self.iinst
        return self.ret
            
        
    