from Connectors import SerialConnector, DatabaseConnector
import Util
import threading


class LoggerThread(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
      
        
    def run(self):
        
        while not self._stopevent.isSet():
            self.ser=SerialConnector()
            self.ser.retrieve(Util.POWER_TAG)
            db=DatabaseConnector()
            db.connect()
            db.insert('power',self.ser.get(Util.POWER_TAG) )
            db.close()
            self._stopevent.wait(2.0)
      
    def stop(self):
        
        self._stopevent.set()