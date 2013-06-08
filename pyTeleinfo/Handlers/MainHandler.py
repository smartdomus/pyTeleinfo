'''
Created on 2 juin 2013

@author: Hoareau
'''

import tornado.web
from Util.Network import Network


class MainHandler(tornado.web.RequestHandler):
    

    def get(self):
        n=Network()
        print n.isWAN(self.request.remote_ip)
        self.render("index.html")

        