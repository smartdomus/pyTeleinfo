'''
Created on 8 juin 2013

@author: Hoareau
'''

import Util
import socket


class Network():
    
    @staticmethod
    def getPrivateIp():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("google.com",80))
        ip=s.getsockname()[0]
        Util.MY_IP=ip
        s.close()
        return  ip
    
    def isWAN(self,ip):
        
        ipB1=self.ipBeginning(ip)
        ipB2=self.ipBeginning(Util.MY_IP)
        
        if(ipB1==ipB2):
            ret=False
        else :
            ret=True
        return ret
        
    
    def ipBeginning(self,ip):
        ipsplit=str(ip).split('.')
        ipbegin=ipsplit[0]+ipsplit[1]
        return ipbegin
    
    