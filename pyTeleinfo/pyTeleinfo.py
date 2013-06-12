'''
Created on 2 juin 2013

@author: Hoareau
'''

from Connectors import DatabaseConnector
from Handlers import MainHandler, DatasHandler, LiveHandler, WsHandler
from Modules import LiveModule, MenuModule
from Threads import LoggerThread
import os
import tornado.httpserver
import tornado.ioloop











class Application(tornado.web.Application):   
    
    def __init__(self):
        self.port=9090
        

        settings = dict(
                        template_path=os.path.join(os.path.dirname(__file__), "Templates"),
                        static_path=os.path.join(os.path.dirname(__file__), "Templates/Static"),
                        ui_modules={'Live': LiveModule,'Menu': MenuModule,}
                        ) 
                            
        handlers = [
                    (r"/", MainHandler),
                    (r"/live", LiveHandler),
                    (r"/datas", DatasHandler),
                    (r"/ws", WsHandler),
                    ]
       
       
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == "__main__":
    db=DatabaseConnector()
    db.connect()
    db.read('power')
    db.close()
    logger=LoggerThread()
    logger.start()
    # serial=SerialConnector()
    # power=serial.getPower()
    # db.close()
    # db.insert('power',power)
    app=Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(app.port,'0.0.0.0')

   
    # periodic.start()
    tornado.ioloop.IOLoop.instance().start()