#!/usr/bin/python
"""
 Covid Volunteers Aggregator Bot Pluggin class

   Copyright (C) 2007-2017 Free Software Foundation, Inc.
   Contributed by : Salil G K <gksalil@gmail.com>
   Contributed by :

   This file is part of Covid Volunteers Aggregator Bot
"""

import sqlite3
from sqlite3 import IntegrityError
from datetime import datetime , time

SERVICES = { "AMBULANCE": "ambulance", "BLOOD": "blood", "HOSPBED": "hospitalbed", "QUARANTINE": "quarantine", "PLASMA":"plasma", "OXYGEN": "oxygen"}

####
## Base class
####
class DataBase(object):
    """
        Base class for database
    """

    db_file="example.db"

    def __init__(self):
        self.con = sqlite3.connect(self.db_file)
        if self.con:
            self.cur = self.con.cursor()

    def print_all(self): raise Exception("Method not implemented")
    def add_entry(self, data): 
        try: 
            self.cur.execute(self.insert_request, data)
            self.con.commit()
        except IntegrityError as exp:
            print "Exception occured: Duplicate ID is for entry is coming  = %s \n" %(str(exp))

    def update_entry(self, query_string):
        self.cur.execute(query_string) 
        self.con.commit()

    def delete_entry(self, query_string):
        self.cur.execute(query_string) 
        self.con.commit()

    def read_from_gl(self): raise Exception("Method not implemented")
    def write_to_whtsp(self): raise Exception("Method not implemented")

    def close(self):
        self.con.close()

  
####
## Class to configure the site specific configurations
####
class SiteConfigDB(DataBase):
    """
        table to store site specific data
         - Site, - Bangalore
         - Feature, - Ambulance
         - Status - Available
 
        for logging purpose, we can create one more Table to store daily status of the feature
         - Date
         - Site, - Bangalore
         - Feature, - Ambulance
         - Status - Available
    """
    create_table="CREATE TABLE IF NOT EXISTS site_capacity ( \
                     id int primary key, \
                     site text, \
                     feature text, \
                     status real \
                     )"

    create_table_hist="CREATE TABLE IF NOT EXISTS site_capacity_hist ( \
                     id int primary key, \
                     entry_date timestamp, \
                     site text, \
                     feature text, \
                     status real \
                     )"

    def __init__(self):
        super(RequestDataBase, self).__init__()
        self.cur.execute(self.create_table)
        self.cur.execute(self.create_table_hist)
        self.con.commit()

    def add_entry(self, data):
      
        site_cap = self.cur.execute("SELECT * from site_capacity( site, feature, status) VALUES (?, ?)" ,(data['site'], data['feature']))
        if not site_cap:
            self.cur.execute("INSERT INTO site_capacity( site, feature, status) VALUES (?, ?, ?)" ,(data['site'], data['feature'], data['status']))
        else:
            print "Entry already exist"

    def update_entry(self, data): pass
    def delete_entry(self, data): pass
    def is_service_available(self, data): pass

    def print_all(self): pass

    
######
##  Request DB class 
##  For each type of requests ( ambulance, blood etc ) create one request instance
######
class RequestDB(DataBase):

    create_table="CREATE TABLE IF NOT EXISTS stocks (  \
                      date text,  \
                      trans text, \
                      symbol text, \
                      qty real, \
                      price real \
                      )"
    insert_stock="INSERT INTO stocks VALUES %s"
  
    def __init__(self, service):
        super(RequestDB, self).__init__()
        self.service = service
        self.cur.execute(self.create_table)
        self.con.commit()

    def print_data(self, symb):
        for row in self.cur.execute("SELECT * FROM stocks where symbol='%s'" % symb):
            print row

    def print_all(self):
        
        self.cur.execute('SELECT * FROM stocks ORDER BY price')
        records = self.cur.fetchall()
        for row in records:
            print row

    def add_entry(self, data):
        insert_val=self.insert_stock % data
        self.cur.execute(insert_val)
        self.con.commit()

    def update_entry(self, data):
        update_val="UPDATE stocks SET price=%s where symbol='%s'" % (data['price'], data['symb'])
        self.cur.execute(update_val)
        self.con.commit()

    def delete_entry(self, symb):
        delete_val="DELETE from stocks where symbol='%s'" % ( symb)
        self.cur.execute(delete_val)
        self.con.commit()

if __name__ == '__main__':
    db = RequestDB(SERVICES["AMBULANCE"])
    
    data="('2006-01-05','BUY','IBM',100,35.14)"
    db.add_entry(data)
    data="('2006-01-05','BUY','RHEL',100,65.64)"
    db.add_entry(data)
    db.print_all()
    print ""
    db.print_data('IBM')
    print ""
    
    db.update_entry({'symb':"IBM", 'price':"18.13"})
    db.print_all()
    db.delete_entry("IBM")
    db.print_all()
    db.close()
