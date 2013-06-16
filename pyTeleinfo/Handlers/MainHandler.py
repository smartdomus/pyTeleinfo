'''
Created on 2 juin 2013

@author: Hoareau
'''

from Util.Network import Network
import Util
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    

    def get(self):
        
        n=Network()
        
        if n.isWAN(self.request.remote_ip):
            self.namespace="http://smartdomus.redirectme.net:9090"
        else:
            self.namespace="http://"+Util.MY_IP+":"+str(9090)
        self.render("index.html",namespace=self.namespace)
