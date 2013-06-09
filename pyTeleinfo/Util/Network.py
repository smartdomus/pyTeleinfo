'''
Created on 8 juin 2013

@author: Hoareau
'''

import socket


class Network(object):
    
    def getPrivateIp(self):
        return socket.gethostbyname(socket.gethostname())
    
    def isWAN(self,ip):
        
        ipB1=self.ipBeginning(ip)
        ipB2=self.ipBeginning(self.getPrivateIp())
        
        if(ipB1==ipB2):
            ret=False
        else :
            ret=True
        return ret
        
    
    def ipBeginning(self,ip):
        ipsplit=str(ip).split('.')
        ipbegin=ipsplit[0]+ipsplit[1]
        return ipbegin
    
    