'''
Created on 9 juin 2013

@author: Hoareau
'''
from Connectors import SerialConnector
from Util import Network
import Util
import tornado.web

class LiveModule(tornado.web.UIModule):

    def render(self):
        return ''
    
    def javascript_files(self):
        return "/static/libs/power.js"
    
    def embedded_javascript(self):
        
        self.ser=SerialConnector()
        self.ser.retrieve(Util.POWER_TAG)
       
        
        n=Network()
        
        if n.isWAN(self.request.remote_ip):
            namespace="smartdomus.redirectme.net:9090"
        else:
            namespace=Util.MY_IP+":"+str(9090)
        return "power="+str(self.ser.get(Util.POWER_TAG))+";var namespace=\""+namespace+"\";"
