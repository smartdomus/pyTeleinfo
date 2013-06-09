'''
Created on 2 juin 2013

@author: Hoareau
'''

import tornado.web



class MainHandler(tornado.web.RequestHandler):
    

    def get(self):
        self.render("index.html")
