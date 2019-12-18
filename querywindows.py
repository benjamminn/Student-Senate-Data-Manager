'''
Author(s): Benjamin Gordon
Last Edited: 12/16/2019
Purpose: Handles all query window operations.
'''
# Imports
import tkinter
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Button
from msilib.schema import ComboBox, ListBox
import clubfunctions
import budgetfunctions
import senatorfunctions




class QueryWindowsClass(object):
    '''
    Controls everything related to the windows that display the queries.
    '''

    def __init__(self, mainwindow):
        '''
        Constructor
        '''
        
        self.mainwindow = mainwindow
        
        
        
    def queryclubbox(mainwindow, clubfunctions):
        '''
        The window that shows club queries.
        '''
  
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('Club Query')
        window.resizable(0, 0)
        
        
        # List of queries.
        valuelist = clubfunctions.queryclub()
        
        
        label1 = Label(window, text="Name:")
        label1.grid(row=1,column=0)  
        
        label2 = Label(window, text="Advisor:")
        label2.grid(row=2,column=0) 
        
        label3 = Label(window, text="Meetings:")
        label3.grid(row=3,column=0) 
        
        label4 = Label(window, text="Planned Weekly Officer Meetings:")
        label4.grid(row=4,column=0) 
        
        label5 = Label(window, text="Planned Weekly Meetings:")
        label5.grid(row=5,column=0) 
        
        label6 = Label(window, text="Actual Meeting Number:")
        label6.grid(row=6,column=0) 
        
        label7 = Label(window, text="Actual Activity Number:")
        label7.grid(row=7,column=0)
        
        label8 = Label(window, text="Average Meeting Attendance:")
        label8.grid(row=8,column=0)
        
        label9 = Label(window, text="Average Activity Attendance:")
        label9.grid(row=9,column=0)
                     
        value1 = Label(window, text=valuelist[0])
        value1.grid(row=1,column=2)  
        
        value2 = Label(window, text=valuelist[1])
        value2.grid(row=2,column=2) 
        
        value3 = Label(window, text=valuelist[2])
        value3.grid(row=3,column=2) 
        
        value4 = Label(window, text=valuelist[3])
        value4.grid(row=4,column=2) 
        
        value5 = Label(window, text=valuelist[4])
        value5.grid(row=5,column=2) 
        
        value6 = Label(window, text=valuelist[5])
        value6.grid(row=6,column=2) 
        
        value7 = Label(window, text=valuelist[6])
        value7.grid(row=7,column=2)
        
        value8 = Label(window, text=valuelist[7])
        value8.grid(row=8,column=2)
        
        value9 = Label(window, text=valuelist[8])
        value9.grid(row=9,column=2)


        # Ok button
        button1 = Button(window, text="Ok", command=lambda: window.destroy())
        button1.grid(row=10,column=1)
        
        
    def querysenatorbox(mainwindow, senatorfunctions):
        '''
        The window that shows senator queries.
        '''
  
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('Senator Query')
        window.resizable(0, 0)
        
        # List of queries.
        valuelist = senatorfunctions.querysenator()
        

        
        label1 = Label(window, text="Name:")
        label1.grid(row=1,column=0)  
        
        label2 = Label(window, text="Phone Number:")
        label2.grid(row=2,column=0) 
        
        label3 = Label(window, text="Email:")
        label3.grid(row=3,column=0) 
        
        label4 = Label(window, text="Club Representative:")
        label4.grid(row=4,column=0) 

                     
        value1 = Label(window, text=valuelist[0])
        value1.grid(row=1,column=2)  
        
        value2 = Label(window, text=valuelist[1])
        value2.grid(row=2,column=2) 
        
        value3 = Label(window, text=valuelist[2])
        value3.grid(row=3,column=2) 
        
        value4 = Label(window, text=valuelist[3])
        value4.grid(row=4,column=2) 

        # Ok button
        button1 = Button(window, text="Ok", command=lambda: window.destroy())
        button1.grid(row=10,column=1)
        
        
        
    def querymeetingbox(mainwindow, meetingfunctions):
        '''
        The window that shows meeting queries.
        '''
        
  
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('Meeting Query')
        window.resizable(0, 0)
        
        # List of queries.
        valuelist = meetingfunctions.querymeeting()
        

        
        label1 = Label(window, text="Date:")
        label1.grid(row=1,column=0)  
        
        label2 = Label(window, text="Type:")
        label2.grid(row=2,column=0) 
        

                     
        value1 = Label(window, text=valuelist[0])
        value1.grid(row=1,column=2)  
        
        value2 = Label(window, text=valuelist[1])
        value2.grid(row=2,column=2) 
        

        # Ok button
        button1 = Button(window, text="Ok", command=lambda: window.destroy())
        button1.grid(row=10,column=1)
        
        
    def querybudgetbox(mainwindow, budgetfunctions):
        '''
        The window that shows budget queries.
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('Budget Query')
        window.resizable(0, 0)
        
        # List of queries.
        valuelist = budgetfunctions.querybudget()
        
        
        
        label1 = Label(window, text="Club:")
        label1.grid(row=1,column=0)  
        
        label2 = Label(window, text="Amount Requested:")
        label2.grid(row=2,column=0) 
        
        label3 = Label(window, text="Net Expenses:")
        label3.grid(row=3,column=0) 
        
        label4 = Label(window, text="Net Revenue:")
        label4.grid(row=4,column=0) 


                     
        value1 = Label(window, text=valuelist[0])
        value1.grid(row=1,column=2)  
        
        value2 = Label(window, text=valuelist[1])
        value2.grid(row=2,column=2) 
        
        value3 = Label(window, text=valuelist[2])
        value3.grid(row=3,column=2) 
    
        value4 = Label(window, text=valuelist[3])
        value4.grid(row=4,column=2) 

        # Ok button
        button1 = Button(window, text="Ok", command=lambda: window.destroy())
        button1.grid(row=10,column=1)