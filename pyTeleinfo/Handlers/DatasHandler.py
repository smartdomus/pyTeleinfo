'''
Created on 2 juin 2013

@author: Hoareau Jacky
'''
from Connectors import SerialConnector
from tornado.web import asynchronous

import Util
import tornado


class DatasHandler(tornado.web.RequestHandler):
    
    @asynchronous
    def get(self):
        
        self.set_header("Access-Control-Allow-Origin", "*")
        
        self.ser=SerialConnector()
        self.ser.retrieveAllDatas()
        
        self.write('{"Power":"%d",' % self.ser.get(Util.POWER_TAG))
        self.write('"Iinst":"%d",' % self.ser.get(Util.IINST_TAG))
        self.write('"HP":"%d",' % self.ser.get(Util.HP_TAG))
        self.write('"HC":"%d",' % self.ser.get(Util.HC_TAG))
        self.write('"Period":"%s"}' % self.ser.get(Util.CURRENTH_TAG))
        
        self.finish()