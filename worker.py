# Connecting to the database: 
'mdm_data': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mdm.canada_provinces',
        'USER': 'choi1602',
        'PASSWORD': 'L5_lb*_NLTK',
        'HOST': 'gta-ins07.fadm.usherbrooke.ca',
        'PORT': '3307',
    }


import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='choi1602',
                                database='mdm.canada_provinces')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()