#!/usr/bin/python
"""
 Covid Volunteers Aggregator Bot Pluggin class

   Copyright (C) 2007-2017 Free Software Foundation, Inc.
   Contributed by : Salil G K <gksalil@gmail.com>
   Contributed by :

   This file is part of Covid Volunteers Aggregator Bot
"""


from database import DataBase
from string import Template

SERVICES = { "AMBULANCE": "ambulance", "BLOOD": "blood", "HOSPBED": "hospitalbed", "QUARANTINE": "quarantine", "PLASMA":"plasma", "OXYGEN": "oxygen"}

SERV_STATUS = {"ENTRY_MADE": "Request Entered", "MESSAGE_SENT": "Message Send", "DUPLICATE": "Duplicate entry"}

send_message = " \
--------------------------- \n \
Patient name    : $name \n \
Locality        : $locality \n \
SPO2            : $spo \n \
--------------------------- \
"

    
######
##  Request DB class 
##  For each type of requests ( ambulance, blood etc ) create one request instance
######
class ChennaiRequest(DataBase):

    table_name = "request_chn"
    google_sheet = "" # link to google sheet for this class

    create_table="CREATE TABLE IF NOT EXISTS %s (  \
                    ID int , \
                    TIMESTAMP timestamp , \
                    CITY text , \ 
                    TESTSTATUS text , \ 
                    SERV_REQUEST text , \ 
                    PATIENT_NAME text , \ 
                    AGE int , \ 
                    GENDER text , \ 
                    LOCALITY text, \ 
                    SRF_NUM int , \ 
                    PLASMA_NEEDED text , \ 
                    ATTENDER_NAME text, \ 
                    ATTENDER_NUMBER text , \ 
                    SPO2 real , \ 
                    DOCTOR_NAME text , \ 
                    HOSPITALISATION_STATUS text , \ 
                    OTHER_DETAILS text , \ 
                    COVID_TEST_DATE timestamp , \ 
                    CT_SCORE int, \ 
                    PRE_EXISTING_DESEASE text, \ 
                    STATUS text, \ 
                    REMARKS text, \
                    SERVED_STATUS text \
                      )" %(table_name)
    insert_stock="INSERT INTO %s (ID , \
                    TIMESTAMP , \
                    CITY , \ 
                    TESTSTATUS , \ 
                    SERV_REQUEST , \ 
                    PATIENT_NAME , \ 
                    AGE , \ 
                    GENDER , \ 
                    LOCALITY , \ 
                    SRF_NUM , \ 
                    PLASMA_NEEDED , \ 
                    ATTENDER_NAME , \ 
                    ATTENDER_NUMBER , \ 
                    SPO2 , \ 
                    DOCTOR_NAME , \ 
                    HOSPITALISATION_STATUS , \ 
                    OTHER_DETAILS , \ 
                    COVID_TEST_DATE , \ 
                    CT_SCORE , \ 
                    PRE_EXISTING_DESEASE , \ 
                    STATUS , \ 
                    REMARKS , \
                    SERVED_STATUS ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" % (table_name)
  
    def __init__(self, service):
        super(ChennaiRequest, self).__init__()
        self.service = service
        self.cur.execute(self.create_table)
        self.con.commit()

    def print_data(self, symb):
        for row in self.cur.execute("SELECT * FROM request " ):
            print row

    def print_all(self):
        
        self.cur.execute('SELECT * FROM request ORDER BY ID')
        records = self.cur.fetchall()
        for row in records:
            print row

    def _format_data(self, data):
        data[0] = int(data[0])
        return data

    def add_entry(self, data):
        insert_val=self.insert_request % data
        self.cur.execute(insert_val)
        self.con.commit()

    def update_entry(self, data):
        update_val="UPDATE request SET SERVED_STATUS=%s where ID='%d'" % (data['status'], data['id'])
        self.cur.execute(update_val)
        self.con.commit()

    def read_from_gl(self):
        print " This is the generic call from application to read from google spreadsheet"
        # call google API to read from the google sheet self.google_sheet
        # call self.add_entry() in a loop

    def write_to_whtsp(self):
        print " This is the generic call from application to write to whatsapp group"


    def delete_entry(self, id):
        delete_val="DELETE from request where id='%d'" % ( id)
        self.cur.execute(delete_val)
        self.con.commit()

if __name__ == '__main__':
    db = ChennaiRequest("Chennai")
    
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

'''
'''
