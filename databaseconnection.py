'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Connects and disconnects from the database.
'''  
import sqlite3 as sqlite

from databaseinsert import DatabaseInsertClass
from databasequery import DatabaseQueryClass
from databasecreate import DatabaseCreateClass
from databaseupdate import DatabaseUpdateClass
from databasedelete import DatabaseDeleteClass
from _sqlite3 import connect


class DatabaseConnectionClass(object):
      '''
      Handles database connection and closure.
      '''

  

      def connect(self, file):
          '''
          Connects to the database with the specifed filepath.
          '''
    
          connection = sqlite.connect(file)
        
          database = connection.cursor()
        

    
          return database, connection
    
    
    
      def close(self, connection):
          '''
          Closes the database.
          '''
    
        
          connection.close()

  

    
    




