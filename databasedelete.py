'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Deletes tables from the database.
'''  

class DatabaseDeleteClass(object):
    '''
    Deletes a table with all tables related to it.
    '''

    def __init__(self):
        '''
        Constructor
        '''   
        
    def deleteclub(self, database, connection, id):
        '''
        Deletes clubs and related club info and budget relations with the given club id.
        '''
 
        id = tuple([id])
     
        database.execute('''DELETE FROM 'Club' WHERE club_id = ?''', id)
        
        connection.commit() 
        
        database.execute('''DELETE FROM 'Club_Info' WHERE club_id = ?''', id)
        
        connection.commit()   
        
        database.execute('''DELETE FROM 'Budget' WHERE club_id = ?''', id)
        
        connection.commit()   


    def deleteclubinfo(self, database, connection, id):
        '''
        Deletes clubs info table  with the given club id.
        '''
 
 
        id = tuple([id])
 
        database.execute('''DELETE FROM 'Club_Info' WHERE club_info_id = ?''', id)
        
        connection.commit() 
        
    def deletebudget(self, database, connection, id):
        '''
        Deletes budget table with the given budget id.
        '''
 
        id = tuple([id])
 
        database.execute('''DELETE FROM 'Budget' WHERE budget_id = ?''', id)
        
        connection.commit() 
        
    def deletesenator(self, database, connection, id):
        '''
        Deletes senator table and related club and attendance tables with the given senator id.
        '''
 
        id = tuple([id])
 
        database.execute('''DELETE FROM 'Senator' WHERE senator_id = ?''', id)
        
        connection.commit()
        
        database.execute('''DELETE FROM 'Club' WHERE senator_id = ?''', id)

        connection.commit()
        
        database.execute('''DELETE FROM 'Attendance' WHERE senator_id = ?''', id)

        connection.commit()
        
    def deletemeeting(self, database, connection, id):
        '''
        Deletes senator table and related attendance tables with the given meeting id.
        '''
        
 
        id = tuple([id])
 
        database.execute('''DELETE FROM 'Meeting' WHERE meeting_id = ?''', id)
        
        connection.commit()
        
        database.execute('''DELETE FROM 'Attendance' WHERE meeting_id = ?''', id)

        connection.commit()
        
    def deleteattendance(self, database, connection, id):
        '''
        Deletes attendance table with the correct attendance id.
        '''
        
        
        id = tuple([id])
 
        database.execute('''DELETE FROM 'Attendance' WHERE attendance_id = ?''', id)
        
        connection.commit()
        

        
        
        
 
        

        
        

