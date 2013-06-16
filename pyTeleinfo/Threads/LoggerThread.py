from Connectors import SerialConnector, DatabaseConnector
import Util
import threading


class LoggerThread(threading.Thread):
    
    def __init__(self):
        
        threading.Thread.__init__(self)
        self._stopevent = threading.Event()
        self.db=DatabaseConnector()
      
        
    def run(self):
        
        while not self._stopevent.isSet():
            self.ser=SerialConnector()
            self.ser.retrieve(Util.POWER_TAG)
            self.db.connect()
            self.db.update('actual_power',self.ser.get(Util.POWER_TAG))
            self.db.close()
            self._stopevent.wait(1.0)
      
    def stop(self):
        
        self._stopevent.set()