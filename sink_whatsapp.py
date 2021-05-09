"""
 Covid Volunteers Aggregator Bot Pluggin class

   Copyright (C) 2007-2017 Free Software Foundation, Inc.
   Contributed by : Salil G K <gksalil@gmail.com>
   Contributed by :

   This file is part of Covid Volunteers Aggregator Bot
"""

#url = "https://maytapi-whatsapp.p.rapidapi.com/" + YOUR_PHONE_ID + "/sendMessage"


def send_message(msg, group_id, rapid_host, rapid_key):

    payload = '{ "to_number": "%s" ,"type": "text", "message": "%s" }' %(group_id, msg)

    headers = {
        'x-rapidapi-host': rapid_host,
        'x-rapidapi-key': rapid_key,
        'content-type': "application/json",
        'accept': "application/json"
    }

    print headers
    print payload
    #response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    #print(response.text)
    #if "false" in  response.text:
    #   return -1
    #else:
    #   return 0

"""
send_message("Message" ,"GROUP", "HOST", "KEY")
"""
