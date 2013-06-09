'''
Created on 9 juin 2013

@author: Hoareau
'''
from tornado.websocket import WebSocketHandler
from Threads.SenderThread import SenderThread



class WsHandler(WebSocketHandler):
    
    
    def open(self):
        print 'connection open !'
        self.sender=SenderThread(self)
        self.sender.start()


    def on_close(self):
        self.sender.stop()
        self.isopen=False
        print 'connection closed'