'''
Created on 2 juin 2013

@author: Hoareau
'''

from Handlers.LiveHandler import LiveHandler
from Handlers.MainHandler import MainHandler
from Handlers.DataHandler import DataHandler

import os
import tornado.httpserver
import tornado.ioloop



   
class Application(tornado.web.Application):   
    
    def __init__(self):
        settings = dict(
                        template_path=os.path.join(os.path.dirname(__file__), "Templates"),
                        static_path=os.path.join(os.path.dirname(__file__), "Templates/Static"),
                        )
        handlers = [
                    (r"/", MainHandler),
                    (r"/live", LiveHandler),
                    (r"/data", DataHandler),
                    ]
        tornado.web.Application.__init__(self,handlers, **settings)

if __name__ == "__main__":
    # db=DatabaseConnector()
    # db.connect()
    # serial=SerialConnector()
    # power=serial.getPower()
    # db.close()
    # db.insert('power',power)
    app=Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(9090,'0.0.0.0')

   
    # periodic.start()
    tornado.ioloop.IOLoop.instance().start()