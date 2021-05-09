"""
 Covid Volunteers Aggregator Bot Pluggin class

   Copyright (C) 2007-2017 Free Software Foundation, Inc.
   Contributed by : Salil G K <gksalil@gmail.com>
   Contributed by :

   This file is part of Covid Volunteers Aggregator Bot
"""

from string import Template

BLR_MSG_TEMPLATE = \
"------------------------------------------------- \n\
--* Covid Patients Help Request* #Form $form *--\n \
\n \
Requirement         : $requirement \n \
Patient Name        : $p_name \n \
Age                 : $age \n \
Gender              : $gender \n \
Attender Name       : $a_name \n \
Attender Number     : $a_number \n \
Attender Whatsapp   : $a_whatsapp \n \
Town/City           : $town_city \n \
Date of Request     : $d_of_request \n \
SPO2                : $spo2 \n \
SRF Number          : $srf_number \n \
Locality            : $locality \n \
Covid Positive?     : $covid_positive \n \
Date of Covid test  : $d_of_covtest \n \
CT Score            : $ct_score \n \
Co-morbidities      : $co_morbids \n \
Other Details       : $other_details \n "

CHENNAI_MSG_TEMPLATE = \
""

def format_string (template, data):
    template = Template (template)
    output = template.substitute(**data)
    return output

if __name__ == "__main__":
    data={'form': "Form", 'requirement': "Oxygen", 'p_name': "Gopal", 'age': 32, 'gender': "Male", 'a_name': 'Hari', 'a_number': 435443, 'a_whatsapp': "", 'town_city': "Bangalore", 'd_of_request': "12-5-2021", 'spo2': 92, 'srf_number': 3232, 'locality': "Marathalli", 'covid_positive': 'YES', 'd_of_covtest':"", 'ct_score':43, 'co_morbids': "", 'other_details': "NA"}

    print format_string(BLR_MSG_TEMPLATE, data)
