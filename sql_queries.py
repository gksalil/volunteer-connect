#Bangalore
blr_create_table="CREATE TABLE IF NOT EXISTS %s (  \
                    ID int PRIMARY KEY, \
                    TIMESTAMP text , \
                    SERV_REQUEST text , \
                    PATIENT_NAME text , \
                    AGE int , \
                    GENDER text , \
                    PLASMA_NEEDED text , \
                    ATTENDER_NAME text, \
                    ATTENDER_NUMBER text , \
                    HOSPITALISATION_STATUS text , \
                    CITY text , \
                    DOCTOR_NAME text , \
                    SPO2 real , \
                    OTHER_DETAILS text, \
                    COVID_TEST_DATE text , \
                    COVID_TEST_STATUS text , \
                    BU_NUM int , \
                    SRF_NUM int , \
                    LOCALITY text, \
                    ZONE text, \
                    CT_SCORE int, \
                    PRE_EXISTING_DESEASE text, \
                    COMMAND_CENTER_NAME text, \
                    COMMAND_CENTER_NUM text, \
                    REMARKS text, \
                    SERVED_STATUS text \
                      )" 

blr_insert_request="INSERT INTO %s (ID , \
                    TIMESTAMP , \
                    SERV_REQUEST , \
                    PATIENT_NAME , \
                    AGE , \
                    GENDER , \
                    PLASMA_NEEDED , \
                    ATTENDER_NAME , \
                    ATTENDER_NUMBER , \
                    HOSPITALISATION_STATUS , \
                    CITY , \
                    DOCTOR_NAME , \
                    SPO2 , \
                    OTHER_DETAILS , \
                    COVID_TEST_DATE , \
                    COVID_TEST_STATUS , \
                    BU_NUM , \
                    SRF_NUM , \
                    LOCALITY , \
                    ZONE , \
                    CT_SCORE , \
                    PRE_EXISTING_DESEASE , \
                    COMMAND_CENTER_NAME , \
                    COMMAND_CENTER_NUM , \
                    REMARKS , \
                    SERVED_STATUS ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 

blr_read_request = 'SELECT * from %s where SERVED_STATUS = "%s"' 
