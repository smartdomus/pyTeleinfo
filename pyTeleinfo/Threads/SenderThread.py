'''
Created on 9 juin 2013

@author: Hoareau
'''


from Connectors import SerialConnector, DatabaseConnector
import Util
import threading


class SenderThread(threading.Thread):
    
    def __init__(self,wshandler):
        
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self.wshandler=wshandler
        self.db=DatabaseConnector()
      
        
    def run(self):
        
        while not self._stopevent.isSet():
           
            self.db.connect()
          
            power=self.db.get_last('power', 'value')
            self.wshandler.write_message(str(power))
            self.db.close()                            
            self._stopevent.wait(1.5)
      
    def stop(self):
        
        self._stopevent.set()