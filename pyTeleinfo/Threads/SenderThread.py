'''
Created on 9 juin 2013

@author: Hoareau
'''


from Connectors import SerialConnector
import threading


class SenderThread(threading.Thread):
    
    def __init__(self,wshandler):
        
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self.wshandler=wshandler
      
        
    def run(self):
        
        while not self._stopevent.isSet():
            self.ser=SerialConnector()
            self.ser.retrievePower()
            self.wshandler.write_message(str(self.ser.getPower()))
            self._stopevent.wait(1.0)
      
    def stop(self):
        self._stopevent.set()