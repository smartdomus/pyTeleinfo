'''
Created on 9 juin 2013

@author: Hoareau
'''
from Connectors import SerialConnector
from Util.Network import Network
import tornado.web

class LiveModule(tornado.web.UIModule):

    def render(self):
        return ''
    
    def javascript_files(self):
        return "/static/libs/power.js"
    
    def embedded_javascript(self):
        
        self.ser=SerialConnector()
        self.ser.retrievePower()
        
        n=Network()
        
        if n.isWAN(self.request.remote_ip):
            namespace="smartdomus.redirectme.net:9090"
        else:
            namespace=n.getPrivateIp()+":"+str(9090)
    
        return "power="+str(self.ser.getPower())+";var namespace=\""+namespace+"\";"
