'''
Created on 2 juin 2013

@author: Hoareau
'''
import datetime
import sqlite3

class DatabaseConnector():
    
    def __init__(self):
        pass
        
    def connect(self):
        self.conn = sqlite3.connect('pyTeleinfo.db')
        
        
    def insert(self,where,value):
        self.cursor=self.conn.cursor()
        self.cursor.execute("INSERT INTO "+ where + " VALUES ('"+str(datetime.datetime.now())+"',"+str(value)+")")
        self.conn.commit()
        
    def close(self):
        self.conn.close()