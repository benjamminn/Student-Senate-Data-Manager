'''
Author(s): Benjamin Gordon
Last Edited: 12/9/2019
Purpose:  Controls the data control program GUI.
'''  

# Imports
import tkinter
from tkinter import ttk, Listbox
from tkinter import Menu
from msilib.schema import ComboBox, ListBox
from tkinter.ttk import Treeview
from newwindows import NewWindowsClass
from attendancewindows import AttendanceWindowsClass
from databaseconnection import DatabaseConnectionClass
from clubfunctions import ClubFunctionsClass
from editwindows import EditWindowsClass
from budgetfunctions import BudgetFunctionsClass
from meetingfunctions import MeetingFunctionsClass
from senatorfunctions import SenatorFunctionsClass
from querywindows import QueryWindowsClass
from databasequery import DatabaseQueryClass
from programmanager import ProgramManagerClass
from tkinter.constants import BOTH




# Global Array
globalbuttonarray = 18 * [0]


# Global Button State
globalbuttonstate = 'disabled'



class DataManagerClass:
      '''
      Manages the main window GUI.
      
      '''
    

         
         
      def newstate(self):     
          '''
          Turns on the buttons and calls the new database function.
          '''
          
          globalbuttonstate = 'normal'
          
          # Turns on buttons
          a = 0
          while a <= 17:
              globalbuttonarray[a].config(state = globalbuttonstate ) 

              a += 1  
              
          self.programmanager.new()

           
      def openstate(self):
          '''
          Turns on the buttons and calls the open database function.
          '''
          
          
          globalbuttonstate = 'normal'
          
          
          # Turns on buttons
          a = 0
          while a <= 17:
              globalbuttonarray[a].config(state = globalbuttonstate ) 

              
              a += 1  
              
          self.programmanager.open()
              
      def closestate(self):
          '''
          Turns off the buttons and calls the close database function.
          '''
          
          
          # Turns off buttons
          a = 0
          while a <= 17:
              globalbuttonarray[a].config(state = globalbuttonstate ) 

              
              a += 1  
              
          self.programmanager.close()          
    
          
     

      def create(self):
          '''
          Creates an instance of the data control program.
          '''
          
             #database, connection = DatabaseConnectionClass().connect("studentsenate.db")
             
          # Creates main program window
          mainwindow = tkinter.Tk()
          
          mainwindow.geometry("1000x500")
          
          # Sets Title
          mainwindow.title('Student Senate Data Manager')
             
          # Dropdown menu
          dropdown = Menu(mainwindow)
             
          # Attaches dropdown menu to mainwindow.
          mainwindow.config(menu = dropdown)  
                
          # File menu object.
          filedropdown = Menu(dropdown, tearoff=0)
                

                
          # Help menu object.
          helpdropdown = Menu(dropdown, tearoff=0)
             
          # Adds menus objects to dropdown menu.
          dropdown.add_cascade(label = 'File', menu = filedropdown)
          dropdown.add_cascade(label = 'Help', menu = helpdropdown)
    
            
          # Commands under the file dropdown menu.      
          filedropdown.add_command(label = 'New Database', command=lambda: DataManagerClass().newstate())
          filedropdown.add_command(label = 'Open Database', command=lambda:  DataManagerClass().openstate())  
          filedropdown.add_command(label = 'Close Database', command=lambda:  DataManagerClass().closestate()) 
          filedropdown.add_separator()
          filedropdown.add_command(label = 'Quit', command=lambda: mainwindow.destroy())
             
          # Help dropdown menu commands.    
          helpdropdown.add_command(label = 'About', command=lambda:self.programmanager.about(mainwindow)) 
    
          # Notebook object
          tabobject = ttk.Notebook(mainwindow)
             
          # Create the object for each tab.   
          panel1 = ttk.Frame(tabobject)
          panel2 = ttk.Frame(tabobject)
          panel3 = ttk.Frame(tabobject)
          panel4 = ttk.Frame(tabobject)       
             
          # Tab titles   
          tabobject.add(panel1, text = 'Clubs')
          tabobject.add(panel2, text = 'Senators')         
          tabobject.add(panel3, text = 'Meetings')
          tabobject.add(panel4, text = 'Budgets')
            
            
          # Places tab structure.  
          tabobject.pack(side = 'top', fill = BOTH, expand = 1)
             
             
          # Treeview objects   
          clubtreeview = Treeview(panel1, columns = ('Club', 'Advisor', 'Meetings'), show = 'headings')
          senatortreeview = Treeview(panel2, columns = ('Name', 'Phone', 'Email', 'Student Senator'), show = 'headings')
          meetingtreeview = Treeview(panel3, columns = ('Date', 'Type'), show = 'headings')
          budgettreeview = Treeview(panel4, columns = ('Club', 'Amount Requested', 'Net Expenses', 'Net Revenue'), show = 'headings')
          
          # Adds scrolling objects
          scroll1 = tkinter.Scrollbar(clubtreeview, command=clubtreeview.yview)
          scroll2 = tkinter.Scrollbar(senatortreeview, command=senatortreeview.yview)
          scroll3 = tkinter.Scrollbar(meetingtreeview, command=meetingtreeview.yview)
          scroll4 = tkinter.Scrollbar(budgettreeview, command=budgettreeview.yview)

     

          
        
        

             
             
          # Fills headers for the club treeview.   
          clubtreeview.heading('Club', text = ('Club'))
          clubtreeview.heading('Advisor', text = ('Advisor'))
          clubtreeview.heading('Meetings', text = ('Meetings'))
          
          # Fills headers for the senator treeview.    
          senatortreeview.heading('Name', text = ('Name'))
          senatortreeview.heading('Phone', text = ('Phone'))
          senatortreeview.heading('Email', text = ('Email'))
          senatortreeview.heading('Student Senator', text = ('Student Senator'))
             
             
          # Fills headers for the meeting treeview.              
          meetingtreeview.heading('Date', text = ('Date'))
          meetingtreeview.heading('Type', text = ('Type'))
             
             
          # Fills budget treeview.   
          budgettreeview.heading('Club', text = ('Club'))
          budgettreeview.heading('Amount Requested', text = ('Amount Requested'))
          budgettreeview.heading('Net Expenses', text = ('Net Expenses'))
          budgettreeview.heading('Net Revenue', text = ('Net Revenue'))
             
          # Packs treeview   
          clubtreeview.pack(fill = BOTH, expand = 1)      
          senatortreeview.pack(fill = BOTH, expand = 1)                     
          meetingtreeview.pack(fill = BOTH, expand = 1)   
          budgettreeview.pack(fill = BOTH, expand = 1)  
          
             
          # Adds scrolling
          scroll1.pack(side="right", fill="y")
          scroll2.pack(side="right", fill="y")
          scroll3.pack(side="right", fill="y")
          scroll4.pack(side="right", fill="y")
             
          clubtreeview.configure(yscrollcommand=scroll1.set)
          senatortreeview.configure(yscrollcommand=scroll2.set)
          meetingtreeview.configure(yscrollcommand=scroll3.set)
          budgettreeview.configure(yscrollcommand=scroll4.set)
             
          # Creates the    
          DataManagerClass.programmanager = ProgramManagerClass(mainwindow, clubtreeview, budgettreeview, meetingtreeview, senatortreeview) 
             

          self.programmanager = ProgramManagerClass(mainwindow, clubtreeview, budgettreeview, meetingtreeview, senatortreeview)
           
          globalbuttonarray[0] = ttk.Button(panel1, text = 'New', state = globalbuttonstate , command=lambda:self.programmanager.clubnew())
          globalbuttonarray[0].pack(side = 'left')
             
          globalbuttonarray[1] = ttk.Button(panel1, text = 'Edit', state = globalbuttonstate , command=lambda:self.programmanager.clubedit())
          globalbuttonarray[1].pack(side = 'left')
             
          globalbuttonarray[2] = ttk.Button(panel1, text = 'Remove', state = globalbuttonstate , command=lambda:self.programmanager.clubdelete())
          globalbuttonarray[2].pack(side = 'left')
             
          globalbuttonarray[3] = ttk.Button(panel1, text = 'Query', state = globalbuttonstate , command=lambda:self.programmanager.clubquery())
          globalbuttonarray[3].pack(side = 'right')
             
          globalbuttonarray[4] = ttk.Button(panel2, text = 'New', state = globalbuttonstate , command=lambda:self.programmanager.senatornew())
          globalbuttonarray[4].pack(side = 'left')
             
          globalbuttonarray[5] = ttk.Button(panel2, text = 'Edit', state = globalbuttonstate , command=lambda:self.programmanager.senatoredit())
          globalbuttonarray[5].pack(side = 'left')
             
          globalbuttonarray[6] = ttk.Button(panel2, text = 'Remove', state = globalbuttonstate , command=lambda:self.programmanager.senatordelete())
          globalbuttonarray[6].pack(side = 'left')
             
          globalbuttonarray[7] = ttk.Button(panel2, text = 'Query', state = globalbuttonstate , command=lambda:self.programmanager.senatorquery())
          globalbuttonarray[7].pack(side = 'right')
             
          globalbuttonarray[8] = ttk.Button(panel3, text = 'New', state = globalbuttonstate , command=lambda:self.programmanager.meetingnew())
          globalbuttonarray[8].pack(side = 'left')
             
          globalbuttonarray[9] = ttk.Button(panel3, text = 'Edit', state = globalbuttonstate , command=lambda:self.programmanager.meetingedit())
          globalbuttonarray[9].pack(side = 'left')
             
          globalbuttonarray[10] = ttk.Button(panel3, text = 'Remove', state = globalbuttonstate , command=lambda:self.programmanager.meetingdelete())
          globalbuttonarray[10].pack(side = 'left')
             
             
          globalbuttonarray[11] = ttk.Button(panel3, text = 'Query', state = globalbuttonstate , command=lambda:self.programmanager.meetingquery())
          globalbuttonarray[11].pack(side = 'right')
             
          globalbuttonarray[12] = ttk.Button(panel3, text = 'Take Attendance', state = globalbuttonstate , command=lambda:self.programmanager.takeattendance())
          globalbuttonarray[12].pack(side = 'right')
             
          globalbuttonarray[13] = ttk.Button(panel3, text = 'Manage Attendance', state = globalbuttonstate , command=lambda:self.programmanager.manageattendance())
          globalbuttonarray[13].pack(side = 'right')
             
          globalbuttonarray[14] = ttk.Button(panel4, text = 'New', state = globalbuttonstate , command=lambda:self.programmanager.budgetnew())
          globalbuttonarray[14].pack(side = 'left')
             
          globalbuttonarray[15] = ttk.Button(panel4, text = 'Edit', state = globalbuttonstate , command=lambda:self.programmanager.budgetedit())
          globalbuttonarray[15].pack(side = 'left')
             
          globalbuttonarray[16] = ttk.Button(panel4, text = 'Remove', state = globalbuttonstate , command=lambda:self.programmanager.budgetdelete())
          globalbuttonarray[16].pack(side = 'left')
             
          globalbuttonarray[17] = ttk.Button(panel4, text = 'Query', state = globalbuttonstate , command=lambda:self.programmanager.budgetquery())
          globalbuttonarray[17].pack(side = 'right')
          
          # Calls the quit menu on exit   
          mainwindow.protocol("WM_DELETE_WINDOW", lambda:self.programmanager.quit(mainwindow))
    
          # Starts program loop
          mainwindow.mainloop()
         
         
