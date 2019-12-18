'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Updates the database tables.
'''  
class DatabaseUpdateClass(object):
    '''
    
    '''

    def __init__(self):
        '''
        Constructor
        '''

    
    def updateclub(self, database, connection, itemlist, id):
        '''
        Updates the club table.
        ''' 
            
        itemtuple = tuple(itemlist + [id])    
            
        sqlitecode = '''
                             UPDATE 'Club'
        
                             SET name = ?, advisor = ?, meetings = ?, senator_id = ?
                      

                             
                             WHERE club_id = ? 
                             '''
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit() 
                
        itemlist = [id] + itemlist          
                
        return itemlist
        
    def updateclubinfo(self, database, connection, itemlist, id):
        '''
        Updates the club info table.
        ''' 
            
        itemtuple = tuple(itemlist + [id])    
            
        sqlitecode = '''
                             UPDATE 'Club_Info'
        
                             SET planned_officer_meeting_per_week = ?, 
                                 planned_general_meeting_per_week = ?, 
                                 actual_meeting_number = ?, 
                                 actual_activity_number = ?, 
                                 average_meeting_attendance = ?, 
                                 average_activity_attendance = ?,
                                 club_id  = ?
                      

                             
                             WHERE club_info_id = ? 
                             '''
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit() 
                
        itemlist = [id] + itemlist          
                
        return itemlist
    
    def updatesenator(self, database, connection, itemlist, id):
        '''
        Updates the senator table.
        ''' 
            
        itemtuple = tuple(itemlist + [id]) 
        
       
            
        sqlitecode = '''
                             UPDATE 'Senator'
        
                             SET name = ?, 
                                 phone_number = ?, 
                                 email = ?, 
                                 is_club_repesentative = ?
                      

                             
                             WHERE senator_id = ? 
                             '''
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit() 
        
                
        itemlist = [id] + itemlist          
                
        return itemlist
    
    def updatebudget(self, database, connection, itemlist, id): 
        '''
        Updates the budget table.
        '''   
            
        itemtuple = tuple(itemlist + [id])    
        
   
            
        sqlitecode = '''
                             UPDATE 'Budget'
        
                             SET amount_requested = ?, 
                                 net_expenses = ?, 
                                 net_revenue = ?, 
                                 club_id = ?
                      

                             
                             WHERE budget_id = ? 
                             '''
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit() 
        
                
        itemlist = [id] + itemlist          
                
        return itemlist
        
    def updatemeeting(self, database, connection, itemlist, id):
        '''
        Updates the meeting table.
        ''' 
            
        itemtuple = tuple(itemlist + [id])    
            
        sqlitecode = '''
                             UPDATE 'Meeting'
        
                             SET date = ?, 
                                 type = ?
                      

                             
                             WHERE meeting_id = ? 
                             '''
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit() 
        
                
        itemlist = [id] + itemlist          
                
        return itemlist    
        
    def updateattendance(self, database, connection, itemlist, id):
        '''
        Updates the attendance table.
        ''' 
            
        itemtuple = tuple(itemlist + [id])    
            
      
        
        sqlitecode = '''
                             UPDATE 'Attendance'
        
                             SET status = ?,
                                 senator_id = ?, 
                                 meeting_id = ? 
                
                      
                      
                             WHERE attendance_id = ? 
                             '''
        
        database.execute(sqlitecode, itemtuple)
        
        connection.commit() 
        
                
        itemlist = [id] + itemlist          
                
        return itemlist
        
        
        

