"""
 Covid Volunteers Aggregator Bot Pluggin class

   Copyright (C) 2007-2017 Free Software Foundation, Inc.
   Contributed by : Salil G K <gksalil@gmail.com>
   Contributed by :

   This file is part of Covid Volunteers Aggregator Bot
"""

import importlib

modules = [('BangaloreDB', 'BangaloreRequest'), ('ChennaiDB', 'ChennaiRequest')]

objects= []

module = importlib.import_module(modules[0][0])
myclass = getattr(module, modules[0][1])
db = myclass("Bangalore")


data_input = ['Form 1794', '', '', '05/05/2021 18:17:40', 'ICU Bed ( only if SpO2< 80 )', 'Praveen kumar soni', '32', 'Male', '', 'Pramila soni', '8839230355', 'Vijaynagar hospital 17 cross road, MC layout,560040', 'Bengaluru', 'Ram manohar', '45', '', 'Covid Positive', '651980', '2952511127182', 'Vijaynagar', '', '', '', 'SOUTH', '080-22975750 / 8431816718 ']


SERV_STATUS = {"ENTRY_MADE": "Request Entered", "MESSAGE_SENT": "Message Send", "DUPLICATE": "Duplicate entry"}
data_val = (int(data_input[0].split()[1]), data_input[3], data_input[4], data_input[5], int(data_input[6]), data_input[7], data_input[8], data_input[9], data_input[10], data_input[11], data_input[12], data_input[13], data_input[14], data_input[15], "today", data_input[16], int(data_input[17]), int(data_input[18]), data_input[19], data_input[23], 0, "NA", "Command", data_input[24], "", SERV_STATUS['ENTRY_MADE'])

db.add_entry(data_val)
data_val = (int(data_input[0].split()[1])+1, data_input[3], data_input[4], data_input[5], int(data_input[6]), data_input[7], data_input[8], data_input[9], data_input[10], data_input[11], data_input[12], data_input[13], data_input[14], data_input[15], "today", data_input[16], int(data_input[17]), int(data_input[18]), data_input[19], data_input[23], 0, "NA", "Command", data_input[24], "", SERV_STATUS['ENTRY_MADE'])

db.add_entry(data_val)
data_val = (int(data_input[0].split()[1])+2, data_input[3], data_input[4], data_input[5], int(data_input[6]), data_input[7], data_input[8], data_input[9], data_input[10], data_input[11], data_input[12], data_input[13], data_input[14], data_input[15], "today", data_input[16], int(data_input[17]), int(data_input[18]), data_input[19], data_input[23], 0, "NA", "Command", data_input[24], "", SERV_STATUS['ENTRY_MADE'])

db.add_entry(data_val)
data_val = (int(data_input[0].split()[1])+3, data_input[3], data_input[4], data_input[5], int(data_input[6]), data_input[7], data_input[8], data_input[9], data_input[10], data_input[11], data_input[12], data_input[13], data_input[14], data_input[15], "today", data_input[16], int(data_input[17]), int(data_input[18]), data_input[19], data_input[23], 0, "NA", "Command", data_input[24], "", SERV_STATUS['ENTRY_MADE'])

db.add_entry(data_val)
data = {"name": "Gopal" , "locality":  "Bangalore" ,"spo": "32.4"}
#print db.validate_and_send(data)
db.write_to_whtsp()
#db.print_all()
