'''
Created on 9 juin 2013

@author: Hoareau
'''
from Threads import SenderThread
from tornado.websocket import WebSocketHandler




class WsHandler(WebSocketHandler):
    
    
    def open(self):
        print 'connection open !'
        self.sender=SenderThread(self)
        self.sender.start()


    def on_close(self):
        self.sender.stop()
        print 'connection closed'