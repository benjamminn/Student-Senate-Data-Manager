'''
Author(s): Benjamin Gordon
Last Edited: 02/6/2019
Purpose: Handles all window operations.
'''
# Imports
import tkinter
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Button, Treeview
from msilib.schema import ComboBox, ListBox
from attendancefunctions import AttendanceFunctionsClass





    
class AttendanceWindowsClass(object):
    '''
    Windows used to manage attendance.
    '''

    def __init__(self, mainwindow):
        '''
        Constructor
        '''
        
        self.mainwindow = mainwindow
        
        
        
    def manageattendancebox(mainwindow, database, connection, meetingfunctions):
        '''
        A window that used to manage attendance for a meeting.
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title(' Manage Attendance')
        window.resizable(0, 0)
  
        

        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        
  
        # Creates treeview
        attendancetreeview = Treeview(frame1 , columns = ('Senator', 'Attendance'), show = 'headings')
        
        attendancetreeview.heading('Senator', text = ('Senator'))
        attendancetreeview.heading('Attendance', text = ('Attendance'))      

        attendancetreeview.pack(side = LEFT, fill = BOTH, expand = 1)          

        
        attendancefunctions = AttendanceFunctionsClass(connection, database, attendancetreeview, meetingfunctions)

        # Fills treeview
        attendancefunctions.populatenames()
        

        # Attendance
        menu1 = ttk.Combobox(frame1, value = ["Present", "Excused", "Absent"])      
        menu1.pack()

        # Commit Button
        button3 = Button(frame1, text="Commit", command=lambda: attendancefunctions.editattendance(menu1.get()))
        button3.pack(side = RIGHT, padx = 4, pady = 4)

        # Finish button
        button1 = Button(window, text="Finish", command=lambda: window.destroy())
        button1.pack(side = RIGHT, padx = 4, pady = 4)
        
        # Cancel button
        button2 = Button(window, text="Cancel", command=lambda:  window.destroy())
        button2.pack(side = RIGHT, padx = 4, pady = 4)
        
    def takeattendancebox(mainwindow, database, connection, meetingfunctions):
        '''
        A window used to a take attendance.
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('Take Attendance')
        window.resizable(0, 0)
 
        

        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        
  
        # Creates treeview
        attendancetreeview = Treeview(frame1 , columns = ('Senator', 'Attendance'), show = 'headings')
        
        attendancetreeview.heading('Senator', text = ('Senator'))
        attendancetreeview.heading('Attendance', text = ('Attendance'))
        
        attendancefunctions = AttendanceFunctionsClass(connection, database, attendancetreeview, meetingfunctions)
        
        # Fills treeview.
        attendancefunctions.populatenames()
        
        attendancetreeview.pack()



        # Present button
        button1 = Button(window, text="Present", command=lambda: attendancefunctions.editattendance("Present"))
        button1.pack(side = LEFT, padx = 4, pady = 4)
        
        # Cancel button
        button2 = Button(window, text="Close", command=lambda:  window.destroy())
        button2.pack(side = RIGHT, padx = 4, pady = 4)


    

        
