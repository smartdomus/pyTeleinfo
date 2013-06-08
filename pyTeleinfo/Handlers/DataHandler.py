'''
Created on 2 juin 2013

@author: Hoareau Jacky
'''
from Connectors import SerialConnector
from tornado.web import asynchronous
import tornado



class DataHandler(tornado.web.RequestHandler):
    
    
    
    
    @asynchronous
    def get(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.ser=SerialConnector()
        self.ser.getDatas()
        #self.power=random.randint(1,7000)
        self.write('{"power":"%d",' % self.ser.getPower())
        self.write('"Iinst":"%d",' % self.ser.getIinst())
        self.write('"HP":"%d",' % self.ser.getHP())
        self.write('"HC":"%d",' % self.ser.getHC())
        self.write('"plage":"%s"}' % self.ser.getCurrentH())
        self.finish()