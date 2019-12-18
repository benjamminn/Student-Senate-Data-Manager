'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Inserts data into the database tables.
'''  

import sqlite3 as sqlite

class DatabaseInsertClass(object):
    '''
    
    '''

    def __init__(self):
        '''
        Constructor
        '''
           
        
    def insertclub(self, database, connection, itemlist):
        '''
        Inserts into the club table.
        '''
   
   
        itemtuple = tuple(itemlist)
            
        sqlitecode =       '''
                             INSERT INTO 'Club'
        
                             ('name', 'advisor', 'meetings', 'senator_id')
                      
                             VALUES(?,?,?,?)
                             
                           '''        
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit()    
        
        
        # Gets last inserted id.
        sqlitecode = ''' SELECT last_insert_rowid()'''
        
        database.execute(sqlitecode)

        lastinsertedid = database.fetchone()      
        
        itemlist = list(lastinsertedid) + itemlist  
        

        
        return itemlist    
        
    def insertclubinfo(self, database, connection, itemlist):
        '''
        Inserts into the club info table.
        '''         
        
        itemtuple = tuple(itemlist)
        
        sqlitecode =       '''
                             INSERT INTO 'Club_Info'
        
                             ('planned_officer_meeting_per_week', 
                             'planned_general_meeting_per_week', 
                             'actual_meeting_number', 
                             'actual_activity_number', 
                             'average_meeting_attendance', 
                             'average_activity_attendance',
                             'club_id')
                      
                             VALUES(?,?,?,?,?,?,?)
                             
                           '''
 
        
 
        database.execute(sqlitecode, itemtuple)
        
        connection.commit()    
        
        # Gets last inserted id.
        sqlitecode = ''' SELECT last_insert_rowid()'''
        
        database.execute(sqlitecode)
        
        lastinsertedid = database.fetchone()
        
        itemlist = list(lastinsertedid) + itemlist  
        
        return itemlist    
        
    def insertsenator(self, database, connection, itemlist = ['Ben Gordon', '661-263-1963', 'capbenjammin@gmail.com', 'Yes']):
        '''
        Inserts into the senator table.
        ''' 
            
        itemtuple = tuple(itemlist)    
            
        sqlitecode =       '''
                             INSERT INTO 'Senator'
        
                             ('name', 'phone_number', 'email', 'is_club_repesentative')
                      
                             VALUES(?,?,?,?)
                             
                           '''
 
        database.execute(sqlitecode, itemtuple)
        
        connection.commit()    
        
        # Gets last inserted id.
        sqlitecode = '''SELECT last_insert_rowid()'''
        
        database.execute(sqlitecode)
        
        lastinsertedid = database.fetchone() 
        
        itemlist = list(lastinsertedid) + itemlist  
        
        return itemlist        
        
    def insertbudget(self, database, connection, itemlist):
        '''
        Inserts into the budget table.
        '''     
    
        
        itemtuple = tuple(itemlist)    
            
        sqlitecode =       '''
                             INSERT INTO 'Budget'
        
                             ('amount_requested', 'net_expenses', 'net_revenue', 'club_id')
                      
                             VALUES(?,?,?,?)
                             
                           '''
 
        database.execute(sqlitecode, itemtuple)
        
        connection.commit()    
        
        # Gets last inserted id.
        sqlitecode = '''SELECT last_insert_rowid()'''
        
        database.execute(sqlitecode)
        
        lastinsertedid = database.fetchone() 
        
        itemlist = list(lastinsertedid) + itemlist 
        
        return itemlist      
    
    def insertmeeting(self, database, connection, itemlist):
        '''
        Inserts into the meeting table.
        ''' 
            
        itemtuple = tuple(itemlist)      
            
        sqlitecode =       '''
                             INSERT INTO 'Meeting'
        
                             ('date', 'type')
                      
                             VALUES(?,?)
                             
                           '''
 
        database.execute(sqlitecode, itemtuple)
        
        connection.commit()    
        
        # Gets last inserted id.
        sqlitecode = '''SELECT last_insert_rowid()'''
        
        database.execute(sqlitecode)
        
        lastinsertedid = database.fetchone() 
        
        itemlist = list(lastinsertedid) + itemlist  
        
        return itemlist        
    

    def insertattendance(self, database, connection, itemlist):
        '''
        Inserts into the attendance table.
        ''' 
            
        itemtuple = tuple(itemlist)
            
        sqlitecode =       '''
                             INSERT INTO 'Attendance'
        
                             ('senator_id', 'meeting_id')
                      
                             VALUES(?,?)
                             
                           '''
 
        database.execute(sqlitecode, itemtuple)
        
        connection.commit()    
        
        # Gets last inserted id.
        sqlitecode = '''SELECT last_insert_rowid()'''
        
        database.execute(sqlitecode)
        
        lastinsertedid = database.fetchone() 
        
        itemlist = list(lastinsertedid) + itemlist  
        
        return itemlist      
    
        

        

