'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Creates the database tables.
'''  

class DatabaseCreateClass(object):
    '''
    Creates database tables.
    '''

    def __init__(self):
        '''
        Constructor
        '''   

    def createclub(self, database):
        '''
        Creates the club table.
        '''
            
        database.execute('''CREATE TABLE Club (
                            [club_id] INTEGER PRIMARY KEY NOT NULL,
                            [name] TEXT NOT NULL, 
                            [advisor] TEXT NOT NULL, 
                            [meetings] TEXT NOT NULL,       
                            [senator_id] INTEGER NOT NULL,
                            FOREIGN KEY(senator_id) REFERENCES Senator(senator_id))                            
                            ''')
        
    def createsenator(self, database):
        '''
        Creates the senator table.
        '''
        
        database.execute('''CREATE TABLE Senator (
                            [senator_id] INTEGER PRIMARY KEY,
                            [name] TEXT,
                            [phone_number] TEXT, 
                            [email] TEXT,
                            [is_club_repesentative] Text)''')
        
        
    def createmeeting(self, database):
        '''
        Creates the meeting table.
        '''
        
        database.execute('''CREATE TABLE Meeting(
                             [meeting_id] INTEGER PRIMARY KEY,
                             [date] TEXT, 
                             [type] TEXT)''')
        
    def createattendance(self, database):
        '''
        Creates the senator table.
        '''
        
        database.execute('''CREATE TABLE Attendance(
                             [attendance_id] INTEGER PRIMARY KEY,
                             [status] TEXT,
                             [senator_id] INTEGER NOT NULL, 
                             [meeting_id] INTEGER NOT NULL,
                             FOREIGN KEY(senator_id) REFERENCES Senator(senator_id)
                             FOREIGN KEY(meeting_id) REFERENCES Meeting(meeting_id))''')
        
    def createbudget(self, database):
        '''
        Creates the budget table.
        '''
        
        database.execute('''CREATE TABLE Budget(
                            [budget_id] INTEGER PRIMARY KEY,                            
                            [amount_requested] INTEGER,
                            [net_expenses] INTEGER, 
                            [net_revenue] INTEGER,
                            [club_id] INTEGER NOT NULL,
                            FOREIGN KEY(club_id) REFERENCES Club(club_id))''')
        

        
    def createclubinfo(self, database):
        '''
        Creates the club info table.
        '''
        
        database.execute('''CREATE TABLE Club_Info(
                            [club_info_id] INTEGER PRIMARY KEY,         
                            [planned_officer_meeting_per_week] INTEGER, 
                            [planned_general_meeting_per_week] INTEGER, 
                            [actual_meeting_number] INTEGER,
                            [actual_activity_number] INTEGER,  
                            [average_meeting_attendance] INTEGER, 
                            [average_activity_attendance] INTEGER,
                            [club_id] INTEGER NOT NULL,
                            FOREIGN KEY(club_id) REFERENCES Club(club_id))''')
        
    def createall(self, database):
        '''
        Creates all tables in a database.
        '''
        
     
        self.createattendance(database)
        self.createbudget(database)
        self.createclub(database)
        self.createclubinfo(database)
        self.createmeeting(database)
        self.createsenator(database)


    