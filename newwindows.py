'''
Author(s): Benjamin Gordon
Last Edited: 12/16/2019
Purpose: Handles all new window operations.
'''
# Imports
import tkinter
import sys
from tkinter import *
from tkinter import messagebox
from tkinter import Menu
from tkinter.ttk import Button, Treeview
from msilib.schema import ComboBox, ListBox
from clubfunctions import ClubFunctionsClass
import senatorfunctions




class NewWindowsClass(object):
    '''
    Controls everything new window related.
    '''

    def __init__(self, mainwindow):
        '''
        Constructor
        '''
        
        self.mainwindow = mainwindow
        
        
        
    def newclubbox(mainwindow, clubfunctions, senatorfunctions):
        '''
        Window that takes data for new club entry.
        '''       
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('New Club')
        window.resizable(0, 0)
        

        
        # Treeview for club selection       
        selecttreeview = Treeview(window, columns = ('Senator'), show = 'headings')
        
        selecttreeview.heading('Senator', text = ('Senator'))
        
        
        selecttreeview.pack(side = LEFT)
        
        # Fills club senator treeview.
        senatorfunctions.fillsenatornames(selecttreeview)
    

        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)

        

        label1 = Label(frame1, text="Name:")
        label1.pack(side = LEFT)
        

        entry1 = Entry(frame1)
        entry1.pack(side = LEFT, padx = 4, pady = 4)
        

        label2 = Label(frame1, text="Advisor:")
        label2.pack(side = LEFT)
        

        entry2 = Entry(frame1)
        entry2.pack(side = LEFT, padx = 4, pady = 4)

        label3 = Label(frame1, text="Meetings:")
        label3.pack(side = LEFT)
        
        # Meetings Combobox
        menu1 = ttk.Combobox(frame1, value = ["Yes", "No"])      
        menu1.pack(side = LEFT)
        

        frame2 = Frame(window)
        frame2.pack(side = TOP, padx = 4, pady = 4)
        

        label4 = Label(frame2, text="Planned Weekly Officer Meetings:")
        label4.pack(side = LEFT)
        
        entry3 = Entry(frame2)
        entry3.pack(side = LEFT, padx = 4, pady = 4)        


        label5 = Label(frame2, text="Planned Weekly Meetings:")
        label5.pack(side = LEFT)
        
        entry4 = Entry(frame2)
        entry4.pack(side = LEFT, padx = 4, pady = 4)    
        

        frame3 = Frame(window)
        frame3.pack(side = TOP, padx = 4, pady = 4)  
        
        label6 = Label(frame3, text="Average Meeting Frequency:")
        label6.pack(side = LEFT)
        
        entry5 = Entry(frame3)
        entry5.pack(side = LEFT, padx = 4, pady = 4) 
        
        label7 = Label(frame3, text="Average Activity Frequency:")
        label7.pack(side = LEFT)
        
        entry6 = Entry(frame3)
        entry6.pack(side = LEFT, padx = 4, pady = 4)  
        

        frame4 = Frame(window)
        frame4.pack(side = TOP, padx = 4, pady = 4)  
        
        label8 = Label(frame4, text="Actual Meeting Number:")
        label8.pack(side = LEFT)
        
        entry7 = Entry(frame4)
        entry7.pack(side = LEFT, padx = 4, pady = 4) 
        
        label9 = Label(frame4, text="Actual Activity Number:")
        label9.pack(side = LEFT)
        
        entry8 = Entry(frame4)
        entry8.pack(side = LEFT, padx = 4, pady = 4)                 

        # Submit button
        button1 = Button(window, text="Submit", command=lambda:(clubfunctions.newclub( itemlist = [entry1.get(), entry2.get(), menu1.get(), selecttreeview.item(selecttreeview.selection())["values"][1], entry3.get(), entry4.get(), entry7.get(), entry8.get(), entry5.get(), entry6.get(), 1]),window.destroy()))
        button1.pack(anchor = "s", side = RIGHT, padx = 4, pady = 4)
        
        # Cancel Button
        button2 = Button(window, text="Cancel", command=lambda: window.destroy())
        button2.pack(anchor = "s", side = RIGHT, padx = 4, pady = 4)
        

        
    def newsenatorbox(mainwindow, senatorfunctions):
        '''
        
        Window that takes data for new senator entry.
               
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('New Senator')
        window.resizable(0, 0)
        
 
        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        

        label1 = Label(frame1, text="Name:")
        label1.pack(side = LEFT)
        

        entry1 = Entry(frame1)
        entry1.pack(side = LEFT, padx = 4, pady = 4)
        

        frame2 = Frame(window)
        frame2.pack(side = TOP, padx = 4, pady = 4)
        

        label3 = Label(frame1, text="Phone Number:")
        label3.pack(side = LEFT)
        

        entry2 = Entry(frame1)
        entry2.pack(side = LEFT, padx = 4, pady = 4)
        
    
        label4 = Label(frame2, text="Email:")
        label4.pack(side = LEFT)
        

        entry3 = Entry(frame2)
        entry3.pack(side = LEFT, padx = 4, pady = 4)
        
        label5 = Label(frame2, text="Student Representative:")
        label5.pack(side = LEFT)
        
        # Representative Combobox
        menu2 = ttk.Combobox(frame2, value = ["Yes", "No"])      
        menu2.pack(side = LEFT)
        
        # Submit button
        button1 = Button(window, text="Submit", command=lambda:(senatorfunctions.newsenator(itemlist = [entry1.get(), entry2.get(), entry3.get(), menu2.get()]),window.destroy()))
        button1.pack(side = RIGHT, padx = 4, pady = 4)
        
        # Cancel Button
        button2 = Button(window, text="Cancel", command=lambda:window.destroy())
        button2.pack(side = RIGHT, padx = 4, pady = 4)
        
    def newmeetingbox(mainwindow, meetingfunctions):
        '''
        
        Window that takes data for new meeting entry.
               
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('New Meeting')
        window.resizable(0, 0)
        
        # Top frame for text and entry box
        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        

        label2 = Label(frame1, text="Date:")
        label2.pack(side = LEFT)
        

        entry2 = Entry(frame1)
        entry2.pack(side = LEFT, padx = 4, pady = 4)
        

        label3 = Label(frame1, text="Type:")
        label3.pack(side = LEFT)
        
        # Meeting type combobox
        menu1 = ttk.Combobox(frame1, value = ["General", "Officer"])      
        menu1.pack(side = LEFT)

        
        # Submit Button
        button1 = Button(window, text="Submit", command=lambda:(meetingfunctions.newmeeting([entry2.get(), menu1.get()]),window.destroy()))
        button1.pack(side = RIGHT, padx = 4, pady = 4)
        
        # Cancel button
        button2 = Button(window, text="Cancel", command=lambda:window.destroy())
        button2.pack(side = RIGHT, padx = 4, pady = 4)
        
    def newbudgetbox(mainwindow, budgetfunctions, clubfunctions):
        '''
        
        Window that takes data for new senator entry.
               
        '''
        
        # Creates window
        window = Toplevel(mainwindow)  
        
        # Window attributes
        window.title('New Budget')
        window.resizable(0, 0)
        
        # Club treeview
        selecttreeview= Treeview(window, columns = ('Club'), show = 'headings')
        
        selecttreeview.heading('Club', text = ('Club'))
        
        
        selecttreeview.pack(side = LEFT)
        
        # Fills club treeview
        clubfunctions.fillclubnames(selecttreeview)
        

        frame1 = Frame(window)
        frame1.pack(side = TOP, padx = 4, pady = 4)
        

        
  
        label2 = Label(frame1, text="Amount Requested:")
        label2.pack(side = LEFT)
        

        entry2 = Entry(frame1)
        entry2.pack(side = LEFT, padx = 4, pady = 4)

        frame2 = Frame(window)
        frame2.pack(side = TOP, padx = 4, pady = 4)    
        

        label3 = Label(frame2, text="Net Expenses:")
        label3.pack(side = LEFT)
        

        entry3 = Entry(frame2)
        entry3.pack(side = LEFT, padx = 4, pady = 4)

           

        label4 = Label(frame2, text="Net Revenue:")
        label4.pack(side = LEFT)
        
   
        entry4 = Entry(frame2)
        entry4.pack(side = LEFT, padx = 4, pady = 4)
        
      
        frame3 = Frame(window)
        frame3.pack(side = RIGHT, padx = 4, pady = 4)
        
        # Submit button
        button1 = Button(window, text="Submit", command=lambda:(budgetfunctions.newbudget(itemlist = [entry2.get(), entry3.get(), entry4.get(), selecttreeview.item(selecttreeview.selection())["values"][1]]),window.destroy()))
        button1.pack(anchor = "s", side = RIGHT, padx = 4, pady = 4)
        
        # Cancel Button
        button2 = Button(window, text="Cancel", command=lambda:window.destroy())
        button2.pack(anchor = "s", side = RIGHT, padx = 4, pady = 4)