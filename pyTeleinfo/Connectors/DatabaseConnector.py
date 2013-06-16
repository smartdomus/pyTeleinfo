'''
Created on 2 juin 2013

@author: Hoareau
'''
import datetime
import sqlite3

class DatabaseConnector():
    
    def __init__(self):
        self.id=0
        
    def connect(self):
        self.conn = sqlite3.connect('pyTeleinfo.db')
        
        
    def insert(self,where,value):
        self.cursor=self.conn.cursor()

        self.cursor.execute("INSERT INTO "+where+"(power) VALUES ('"+str(value)+"');")
        self.id = self.cursor.lastrowid
        self.conn.commit()
        
    def update(self,where,value):
        self.cursor=self.conn.cursor()
        self.cursor.execute("UPDATE "+where+" SET power="+str(value))
        self.conn.commit()
        
        
    def read(self,where):
        self.cursor=self.conn.cursor()
        self.cursor.execute("SELECT * FROM "+where)
        self.rows = self.cursor.fetchall()
        #for row in self.rows:
        #print row
        
    def get_last(self,where,column):
        self.cursor=self.conn.cursor()
        self.cursor.execute("SELECT power FROM actual_power WHERE id='1'")
        #self.cursor.execute("SELECT LAST(value) FROM power ")
        #self.cursor.lastrowid
        self.ret=self.cursor.fetchone()[0]
        self.conn.commit()
        return  self.ret  
        
    def close(self):
        self.conn.close()