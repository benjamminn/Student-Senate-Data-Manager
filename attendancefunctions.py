'''
Author(s): Benjamin Gordon
Last Edited: 12/16/2019
Purpose:  Calls database functions and controls the relevant treeview for the attendance category
          It holds a dictionary to give it any data it needs to do operations.
'''  
from databaseinsert import DatabaseInsertClass
from tkinter import ttk, Listbox
from tkinter import Menu
from msilib.schema import ComboBox, ListBox
from tkinter.ttk import Treeview

from databaseconnection import DatabaseConnectionClass
from databaseupdate import DatabaseUpdateClass
from databasedelete import DatabaseDeleteClass
from databasequery import DatabaseQueryClass




class AttendanceFunctionsClass(object):
    '''
    This function control operations on the database and treeview for the attendance category.
    It holds the table data needed to operate on the database and treeview in a dictionary.
    '''

    def __init__(self, connection, database, treeview, meetingfunctions, data = {}):

        '''
        Constructor
        '''
        
        self.database = database
        
        self.connection = connection
        
        self.data = data
        
        self.treeview = treeview 
          
        self.meetingid = meetingfunctions.retrievemeetingid()
        
             
        
        
    def populatenames(self): 
        '''
        Populates the attendance treeview.
        ''' 
        
            
        
        datalist = DatabaseQueryClass.queryattendanceall(self.database, self.meetingid)
            
         
         # Inserts the attendance entry into the treeview.
        for i in datalist:
            
            senatorname = DatabaseQueryClass.querysenatorname(self.database, i[2])
            
    
            id = self.treeview.insert('', 'end', values = tuple([senatorname[0]]+[i[1]]))
        
        
            self.data[id] = list(i)
      
        try:

            self.treeview.selection_set(id)
            self.treeview.focus(id)
            
        except:
            return
    def editattendance(self, status):
        '''
        Edits selected attendance entry in the database, treeview and dictionary. 
        Edits the attendance table.
        '''
        
        id = self.treeview.selection()
        
        id = str(id[0])
        

        
        oldlist = self.data[id] 
        
        oldlist[1] = status
        
        senatorname = DatabaseQueryClass.querysenatorname(self.database, oldlist[2])
        
        newlist = DatabaseUpdateClass().updateattendance(self.database, self.connection, oldlist[1:4], oldlist[0])
        
         
        
        self.treeview.item(id, values = tuple([senatorname[0]]+[newlist[1]]))
        
        self.data[id] = newlist
        
        

            
        
        
        
        
        
        
         
        
        