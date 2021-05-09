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
from format_message import format_string, BLR_MSG_TEMPLATE
from site_c import SiteConfig
from sink_whatsapp import send_message
from sql_queries import *

SERVICES = { "AMBULANCE": "ambulance", "BLOOD": "blood", "ICUBED": "ICUBED", "QUARANTINE": "quarantine", "PLASMA":"plasma", "OXYGEN": "oxygen"}
SERV_STATUS = {"ENTRY_MADE": "Request Entered", "MESSAGE_SENT": "Message Send", "DUPLICATE": "Duplicate entry"}

send_msg = " \
\n \
----Covid Volunteer Group - Bangalore -- \n \
\n \
Patient name             : $name \n \
Locality                 : $locality \n \
SPO2                     : $spo \n \
\n \
--------------------------- \
"
    
######
##  Request DB class 
##  For each type of requests ( ambulance, blood etc ) create one request instance
######
class BangaloreRequest(DataBase):


    table_name = "request_blr"
    google_sheet = "" # link to google sheet for this class
    group_id = "GROUPID"
    rapid_host = "RAPID_HOST"
    rapid_key = "RAPID_KEY"

    create_table = blr_create_table % ( table_name)
    insert_request = blr_insert_request %(table_name)

    read_request = blr_read_request % (table_name, SERV_STATUS['ENTRY_MADE'] )
  
    def __init__(self, service):
        super(BangaloreRequest, self).__init__()
        self.service = service
        self.cur.execute(self.create_table)
        self.con.commit()

        self.source = None  # where we get data from - ( eg: googlesheet )
        self.sink = None    # where we send formated data to - ( eg: whatsapp API )

        self.site_config = SiteConfig()
        self.site_config.add_siteconfig('blr', 'ambulance', 'TRUE')
        self.site_config.add_siteconfig('blr', 'blood', 'FALSE')

    def print_data(self, symb):
        query_string = "SELECT * FROM %s " % (self.table_name)
        for row in self.cur.execute(query_string ):
            print row

    def print_all(self):
        
        query_string = "SELECT * FROM %s ORDER BY ID " % (self.table_name)
        self.cur.execute(query_string)
        records = self.cur.fetchall()
        for row in records:
            print row

    def add_entry(self, data):
        DataBase.add_entry(self, data)

    def update_entry(self, data):
        query_string = "UPDATE %s SET SERVED_STATUS='%s' where ID=%d" % (self.table_name, data['SERVED_STATUS'], data['ID'])
        DataBase.update_entry(self, query_string)

    def delete_entry(self, id):
        query_string="DELETE from %s where id='%d'" % (self.table_name, id)
        DataBase.delete_entry(self, query_string)

    def read_from_gl(self): 
        ## Here we chose which data source to read from
        # It could be whatsapp, mail, telegram etc
        # In init we initialise the source

        print " This is the generic call from application to read from google spreadsheet"
        # call google API to read from the google sheet self.google_sheet
        # call self.add_entry() in a loop

    def _form_dict(self, data, dict_1):
        ## here put all validations
        dict_1['form'] = "Bangalore"
        dict_1['requirement'] = data[2]
        dict_1['p_name'] = data[3]
        dict_1['age'] = data[4]
        dict_1['gender'] = data[5]
        dict_1['a_name'] = data[7]
        dict_1['a_number'] = data[8]
        dict_1['a_whatsapp'] = ""
        dict_1['town_city'] = data[10]
        dict_1['d_of_request'] = data[1]
        dict_1['spo2'] = data[11]
        dict_1['srf_number'] = data[17]
        dict_1['locality'] = data[18]
        dict_1['covid_positive'] = data[15]
        dict_1['d_of_covtest'] = data[14]
        dict_1['ct_score'] = data[20]
        dict_1['co_morbids'] = data[21]
        dict_1['other_details'] = data[9]


    def write_to_whtsp(self): 
        ## Here we chose which data sink to write to 
        # It could be whatsapp, mail, telegram etc
        # In init we initialise the sink

        # Lock here - may be later 
        request_l = self.cur.execute(self.read_request)
        request_list = self.cur.fetchall()
        
        for req in request_list: 
            
             #if self.site_config.get_siteconfig('blr', req['2']) == "TRUE":
             #    print " This is the generic call from application to write to whatsapp group"
             data_1 = {}
             self._form_dict(req, data_1)
             form_string = format_string(BLR_MSG_TEMPLATE, data_1)
             
             send_message(form_string, self.group_id, self.rapid_host, self.rapid_key)
             self.update_entry({'SERVED_STATUS':SERV_STATUS['MESSAGE_SENT'], 'ID':req[0]})
             print " --- "


if __name__ == '__main__':
    db = BangaloreRequest("Bangalore")
    
    data_input = ['Form 1794', '', '', '05/05/2021 18:17:40', 'ICU Bed ( only if SpO2< 80 )', 'Praveen kumar soni', '32', 'Male', '', 'Pramila soni', '8839230355', 'Vijaynagar hospital 17 cross road, MC layout,560040', 'Bengaluru', 'Ram manohar', '45', '', 'Covid Positive', '651980', '2952511127182', 'Vijaynagar', '', '', '', 'SOUTH', '080-22975750 / 8431816718 ']


    data_val = (int(data_input[0].split()[1]), data_input[3], data_input[4], data_input[5], int(data_input[6]), data_input[7], data_input[8], data_input[9], data_input[10], data_input[11], data_input[12], data_input[13], data_input[14], data_input[15], "today", data_input[16], int(data_input[17]), int(data_input[18]), data_input[19], data_input[23], 0, "NA", "Command", data_input[24], "", SERV_STATUS['ENTRY_MADE'])

    db.add_entry(data_val)
    db.print_all()
    db.update_entry({'ID':1794, 'SERVED_STATUS':SERV_STATUS['MESSAGE_SENT']})
    db.print_all()
    data = {"name": data_input[5] , "locality":  data_input[19] ,"spo": "32.4"}
    #print data
    print format_string(send_msg, data)
