'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Queries the database.
'''  


class DatabaseQueryClass(object):
    '''
    Handles all queries from the database.
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def queryclub(database, id):
        '''
        Queries the club table and related clubinfo table by the given clubid.
        '''
        
        id = tuple([id])
        
             
        sqlitecode = ''' SELECT Club.name, 
                                Club.advisor, 
                                Club.meetings, 
                                Club_Info.planned_officer_meeting_per_week,
                                Club_Info.planned_general_meeting_per_week,
                                Club_Info.actual_meeting_number,
                                Club_Info.actual_activity_number,
                                Club_Info.average_meeting_attendance,
                                Club_Info.average_activity_attendance
                                FROM Club_Info
                                
                                INNER JOIN Club ON Club.club_id = Club_Info.club_id
                                
                                WHERE Club.club_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        
 
        
        return query
    
    def querybudget(database, id):
        '''
        Queries the budget by the given budget id.
        '''

        id = tuple([id])
        
    
        
        sqlitecode = ''' SELECT Club.name,
                                Budget.amount_requested, 
                                Budget.net_expenses, 
                                Budget.net_revenue
                                FROM Budget
                           
                                INNER JOIN Club ON Club.club_id = Budget.club_id
                                
                                WHERE Club.club_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        

        
        return query
    
    def querysenator(database, id):
        '''
        Queries the senator by the given senator id.
        '''

        id = tuple([id])
        

        
        sqlitecode = ''' SELECT Senator.name, 
                                Senator.phone_number, 
                                Senator.email,
                                Senator.is_club_repesentative
                           
                                FROM Senator
                    
                                WHERE Senator.senator_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        

        
        return query
    
    def querymeeting(database, id):
        '''
        Queries the meeting by the given meeting id.
        '''

        id = tuple([id])
        
     
        
        sqlitecode = ''' SELECT Meeting.date, 
                                Meeting.type
                           
                                FROM Meeting
                    
                                WHERE Meeting.meeting_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        

        
        return query
    
    def queryclub(database, id):
        
        id = tuple([id])
        
             
        sqlitecode = ''' SELECT Club.name, 
                                Club.advisor, 
                                Club.meetings, 
                                Club_Info.planned_officer_meeting_per_week,
                                Club_Info.planned_general_meeting_per_week,
                                Club_Info.actual_meeting_number,
                                Club_Info.actual_activity_number,
                                Club_Info.average_meeting_attendance,
                                Club_Info.average_activity_attendance
                                FROM Club_Info
                                
                                INNER JOIN Club ON Club.club_id = Club_Info.club_id
                                
                                WHERE Club.club_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        

        
        return query
            
    def querycluball(database):
        '''
        Queries all existing clubs and club info tables.
        '''
            

             
        sqlitecode = ''' SELECT Club.club_id,
                                Club.name, 
                                Club.advisor, 
                                Club.meetings,
                                Club.senator_id,
                                Club_Info.club_info_id, 
                                Club_Info.planned_officer_meeting_per_week,
                                Club_Info.planned_general_meeting_per_week,
                                Club_Info.actual_meeting_number,
                                Club_Info.actual_activity_number,
                                Club_Info.average_meeting_attendance,
                                Club_Info.average_activity_attendance,
                                Club_Info.club_id
                                FROM Club_Info
                                
                                INNER JOIN Club ON Club.club_id = Club_Info.club_id
                                
                            
                                '''
        
        database.execute(sqlitecode)
        
        query = database.fetchall()
        
  
        
        return query
    
    def querybudgetall(database):
        '''
        Queries all existing budget tables.
        '''
 
        
        sqlitecode = ''' SELECT Budget.budget_id,
                                Budget.amount_requested, 
                                Budget.net_expenses, 
                                Budget.net_revenue,
                                Budget.club_id
                                FROM Budget
                                '''
        
        database.execute(sqlitecode)
        
        query = database.fetchall()
        

        
        return query
    
    def querymeetingall(database):
        '''
        Queries all existing meeting tables.
        '''

        
        sqlitecode = ''' SELECT Meeting.meeting_id,
                                Meeting.date, 
                                Meeting.type
                           
                                FROM Meeting
                    
                                '''
        
        database.execute(sqlitecode)
        
        query = database.fetchall()
        
   
        
        return query
    
    def querysenatorall(database):
        '''
        Queries all existing senator tables.
        '''

        
        sqlitecode = ''' SELECT senator.senator_id,
                                Senator.name, 
                                Senator.phone_number, 
                                Senator.email,
                                Senator.is_club_repesentative

                           
                                FROM Senator
                    

                                '''
        
        database.execute(sqlitecode)
        
        query = database.fetchall()
        
    
        
        return query
    
    def querymeetingnameall(database, id):
        '''
        Queries all existing meeting date attributes.
        '''


        id = tuple([id])
        
  
        
        sqlitecode = ''' SELECT Meeting.date, 

                           
                                FROM Meeting
                    
                             
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchall()
        
   
        
        return query
    
    def querymeetingidall(database):
        '''
        Queries all existing meeting id attributes.
        '''

        
        sqlitecode = ''' SELECT Meeting.meeting_id

                           
                                FROM Meeting
                    
                             
                                '''
        
        database.execute(sqlitecode)
        
        query = database.fetchall()
        
      
        
        return query

    def querysenatoridall(database):
        '''
        Queries all existing senator id attributes.
        '''
 
        
        sqlitecode = ''' SELECT Senator.senator_id

                           
                                FROM Senator
                    
                             
                                '''
        
        database.execute(sqlitecode)
        
        query = database.fetchall()
        

        
        return query



    def queryattendance(database):
        '''
        Queries all existing attendance attributes.
        '''
        
        sqlitecode = '''     Attendance.attendance_id,
                             Attendance.status,
                             Attendance.senator_id, 
                             Attendance.meeting_id
                             FROM Attendance
                                '''
        
   
        
        query = database.fetchall()
        
  
        
        return query
    
    def queryattendanceall(database, id):
        '''
        Queries all existing attendance attributes for a meeting id.
        '''
            
        id = tuple([id])
             
        sqlitecode = ''' SELECT Attendance.attendance_id,
                                Attendance.status,
                                Attendance.senator_id,
                                Attendance.meeting_id
                                
                                FROM Attendance
                                
                                Where Attendance.meeting_id = ?
                                
                            
                                '''
      
        database.execute(sqlitecode, id)
        
        query = database.fetchall()
        
     
        
        return query
    
    def querysenatorname(database, id):
        '''
        Queries all existing senator names.
        '''

        id = tuple([id])
        
     
        
        sqlitecode = ''' SELECT Senator.name 
                              
                           
                                FROM Senator
                    
                                WHERE Senator.senator_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        
    
        
        query = list(query)
        
    
        
        return query
    
    def queryclubname(database, id):
        '''
        Queries all existing senator names.
        '''

        id = tuple([id])
        
    
        
        sqlitecode = ''' SELECT Club.name 
                              
                           
                                FROM Club
                    
                                WHERE Club.club_id = ?
                                '''
        
        database.execute(sqlitecode, id)
        
        query = database.fetchone()
        
    
        
        query = list(query)
        
    
        
        return query
            
            
        

