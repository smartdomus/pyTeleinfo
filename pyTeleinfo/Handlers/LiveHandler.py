'''
Created on 2 juin 2013

@author: Hoareau
'''

import tornado.web


class LiveHandler(tornado.web.RequestHandler):
    

    def get(self): 
        self.render("live.html")

        