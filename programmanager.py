'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all file operations.
'''
# Imports
import tkinter  
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter import Menu, messagebox, Toplevel, Label
from databaseconnection import DatabaseConnectionClass
from databasecreate import DatabaseCreateClass
from clubfunctions import ClubFunctionsClass
from budgetfunctions import BudgetFunctionsClass
from meetingfunctions import MeetingFunctionsClass
from senatorfunctions import SenatorFunctionsClass
from querywindows import QueryWindowsClass
from editwindows import EditWindowsClass
from newwindows import NewWindowsClass
from attendancewindows import AttendanceWindowsClass
from databaseinsert import DatabaseInsertClass
from multiprocessing import sys


class ProgramManagerClass(object):
    '''
    Gives functionality to buttons in the editor and manages the classes needed for the database.
    '''

    def __init__(self, mainwindow, clubtreeview, budgettreeview, meetingtreeview, senatortreeview):
        '''
        Constructor
        '''
        
        # Global filepath.
        self.filepath = ''
        
        # Main window
        self.mainwindow = mainwindow
        
        # Sets treeviews
        self.clubtreeview = clubtreeview
        self.meetingtreeview = meetingtreeview
        self.budgettreeview = budgettreeview
        self.senatortreeview = senatortreeview
        
 
    def close(self):
          '''
          Closes the database.
          '''
        
 
          try:
              # Closes the database connections
              DatabaseConnectionClass().close(self.connection)
              
              
              # Clears the classes and treeviews.
              self.clubfunction.clearclub()
              self.budgetfunctions.clearbudget()
              self.meetingfunctions.clearmeeting()
              self.senatorfunctions.clearsenator()
              
              # Removes objects from memory
              del self.clubfunction
              del self.budgetfunctions
              del self.meetingfunctions
              del self.senatorfunctions
              
          except:
               return
       
    

       
    def new(self):
        '''
        Creates and opens a new database.
        '''
        
        try:
    
            # In case the user forgets to close the last database.
            self.close()
      
            # Gets file path from menu.
            self.filepath = asksaveasfilename(defaultextension=".db", initialfile='database.db', filetypes=[("Database File","*.db")]) 
            
            # Converts the file filepath to a string.
            file = str(self.filepath)
    
            # Creates the database and gets the connection and database.
            ProgramManagerClass.database, ProgramManagerClass.connection = DatabaseConnectionClass().connect(file)
            
            
          
            # Creates all tables in the database.
            DatabaseCreateClass().createall(self.database)
            
            DatabaseInsertClass().insertclub(self.database, self.connection, ['', '', '', ''])
            DatabaseInsertClass().insertclubinfo(self.database, self.connection, ['', '', '', '', '', '', 1])
            DatabaseInsertClass().insertsenator(self.database, self.connection, ['', '', '', ''])
            DatabaseInsertClass().insertbudget(self.database, self.connection, ['', '', '', 1])
            DatabaseInsertClass().insertmeeting(self.database, self.connection, ['', ''])
            DatabaseInsertClass().insertattendance(self.database, self.connection, [1, 1])
    
    
            
            # Creates all the classes needed for operations.
            ProgramManagerClass.clubfunction = ClubFunctionsClass(self.connection, self.database, self.clubtreeview)
            ProgramManagerClass.budgetfunctions = BudgetFunctionsClass(self.connection, self.database, self.budgettreeview)
            ProgramManagerClass.meetingfunctions = MeetingFunctionsClass(self.connection, self.database, self.meetingtreeview)
            ProgramManagerClass.senatorfunctions = SenatorFunctionsClass(self.connection, self.database, self.senatortreeview)     
     
        except:
            return
          
    
    def open(self):
        '''
        Opens a database.
        '''
        
        try:
       
            # In case the user forgets to close the last database.
            self.close()
           
            # Gets the files path from the user.   
            self.filepath = askopenfilename()
                
            # Converts the file to a string.    
            file = str(self.filepath)
    
            # Creates the database and gets the connection and database.
            ProgramManagerClass.database, ProgramManagerClass.connection = DatabaseConnectionClass().connect(file)
            
            
            # Creates all classes needed for operations.
            ProgramManagerClass.clubfunction = ClubFunctionsClass(self.connection, self.database, self.clubtreeview)
            ProgramManagerClass.budgetfunctions = BudgetFunctionsClass(self.connection, self.database, self.budgettreeview)
            ProgramManagerClass.meetingfunctions = MeetingFunctionsClass(self.connection, self.database, self.meetingtreeview)
            ProgramManagerClass.senatorfunctions = SenatorFunctionsClass(self.connection, self.database, self.senatortreeview)
            
            
            
            
        
    
       
        except:
            return

        
   
        
    def about(self, mainwindow):
         """
         Creates the about window
         """
         
         # About window options.
         window = Toplevel(mainwindow)
         window.resizable(0, 0)
         window.title('About')
         
         # Labels
         label1 = Label(window, text="Author: Benjamin Gordon")  
         label2 = Label(window, text="Github: https://github.com/benjamminn/Student-Senate-Data-Manager")
         
         # Puts labels on top.
         label1.pack(side = "top")
         label2.pack(side = "top")
         
         # Creates textbox.    
         textbox = tkinter.Text(window) 
          
    
         
         # Creates scrollbar
         scroll = tkinter.Scrollbar(textbox, command=textbox.yview)
         

         textbox.insert('insert',  
"""Student Senate Data Manager: A data manager for student governments.
Copyright (C) 2019 Benjamin Gordon
Student Senate Data Manager: is free software: you can redistribute it 
and/or modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of the License
, or (at your option) any later version.
Student Senate Data Manager: is distributed in the hope that it will be 
useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
Public License for more details.
You should have received a copy of the GNU General Public License
along with the Feather Text Editor.  If not, see
<https://www.gnu.org/licenses/>.
*Freely available text taken from gnu.com""")
        
         
    
         
         
         # Disables Editing
         textbox.config(state="disabled")
                   
             
         # Attaches scrollbar and main menu to window.
         textbox.pack(side="left", fill="both", expand=1, padx = 6, pady = 6)
         scroll.pack(side="right", fill="y")  
         
         # Set Pixel Size
         window.geometry("625x300")
        
        
        
    def quit(self, mainwindow):
        """
        Verify's the user wants to close.
        """
        
        # Opens messagebox to check if the user wants to quit.
        if messagebox.askyesno("Student Senate Data Manager","Are you sure you want to quit?") == True:
           self.close()
           mainwindow.destroy() 
           sys.exit()
        

        
        
        
        
        

        
        
 
    
    def clubnew(self):
        '''
        Abstraction Function.
        '''
        try:
            NewWindowsClass.newclubbox(self.mainwindow, self.clubfunction, self.senatorfunctions)
        except:
            return        
        
    def clubedit(self):
        '''
        Abstraction Function.
        '''
        try:
            EditWindowsClass.editclubbox(self.mainwindow, self.clubfunction, self.senatorfunctions)
        except:
            return
        
    def clubdelete(self):
        '''
        Abstraction Function.
        '''
        try:
            self.clubfunction.deleteclub()
        except:
            return
        
    def clubquery(self):
        '''
        Abstraction Function.
        '''
        try:
            QueryWindowsClass.queryclubbox(self.mainwindow, self.clubfunction)
        except:
            return
        
    def senatornew(self):
        '''
        Abstraction Function.
        '''
        try:
            NewWindowsClass.newsenatorbox(self.mainwindow, self.senatorfunctions)
        except:
            return
        
    def senatoredit(self):
        '''
        Abstraction Function.
        '''
        try:
            EditWindowsClass.editsenatorbox(self.mainwindow, self.senatorfunctions)
        except:
            return
        
    def senatordelete(self):
        '''
        Abstraction Function.
        '''
        try:
            self.senatorfunctions.deletesenator()
        except:
            return
        
    def senatorquery(self):
        '''
        Abstraction Function.
        '''
        try:  
            QueryWindowsClass.querysenatorbox(self.mainwindow, self.senatorfunctions)
        except:
            return
        
    def meetingnew(self):
        '''
        Abstraction Function.
        '''
        try:
            NewWindowsClass.newmeetingbox(self.mainwindow, self.meetingfunctions)
        except:
            return        
    def meetingedit(self):
        '''
        Abstraction Function.
        '''
        try:
            EditWindowsClass.editmeetingbox(self.mainwindow, self.meetingfunctions)
        except:
            return
        
    def meetingdelete(self):
        '''
        Abstraction Function.
        '''
        try:
            self.meetingfunctions.deletemeeting()
        except:
            return
        
    def meetingquery(self):
        '''
        Abstraction Function.
        '''
        try:
            QueryWindowsClass.querymeetingbox(self.mainwindow, self.meetingfunctions)
        except:
            return
            
    def manageattendance(self):
        '''
        Abstraction Function.
        '''
        try:
            AttendanceWindowsClass.manageattendancebox(self.mainwindow, self.database, self.connection, self.meetingfunctions)
        except:
            return
        
    def takeattendance(self):
        '''
        Abstraction Function.
        '''
        try:
            AttendanceWindowsClass.takeattendancebox(self.mainwindow, self.database, self.connection, self.meetingfunctions)
        except:
            return
        
    def budgetnew(self):
        '''
        Abstraction Function.
        '''
        try:
            NewWindowsClass.newbudgetbox(self.mainwindow, self.budgetfunctions, self.clubfunction)
        except:
            return
        
    def budgetedit(self):
        '''
        Abstraction Function.
        '''
        try:
            EditWindowsClass.editbudgetbox(self.mainwindow, self.budgetfunctions, self.clubfunction)
        except:
            return
        
    def budgetdelete(self):
        '''
        Abstraction Function.
        '''
        try:
            self.budgetfunctions.deletebudget()
        except:
            return
        
    def budgetquery(self):
        '''
        Abstraction Function.
        '''
        try:
            QueryWindowsClass.querybudgetbox(self.mainwindow, self.budgetfunctions)
        except:
            return
       
        
        

        

    