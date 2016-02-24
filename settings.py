import time
import Tkinter
import tkMessageBox
from Tkinter import *



#CUSTOMIZE SETTINGS HERE
interval = 20 * 60 #in seconds - time between breaks
break_time = 15 #in seconds - how long each break lasts
long_break_time = 3 * 60 #in seconds - time for long break
break_check = 3 #how many times before the app asks if the user wants a break



#******CLASS CURRENTLY NOT IMPLEMENTED******
class Settings(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()

        self.interval_entry = StringVar(self, value=interval)
        self.break_time_entry = StringVar(self, value=break_time)
        self.long_break_time_entry = StringVar(self, value=long_break_time)
        self.break_check_entry = StringVar(self, value=break_check)

        Label(self, text="Customize Settings:").grid(column=1, row=1, columnspan=2)

        entries=[
            ["Interval between short breaks:", 2, self.interval_entry],
            ["Duration of short breaks:", 3, self.break_time_entry],
            ["Duration of long breaks:", 4, self.long_break_time_entry],
            ["Amount of short breaks before long break:", 5, self.break_check_entry]
        ]
        for x in range(len(entries)):
            self.create_entry(entries[x][0], entries[x][1], entries[x][2])

        #Save button
        b = Button(self, text="Save settings", command=self.update_settings)
        b.grid(row=6, column=1, columnspan=2)


    def create_entry(self, text, row, var):
        Label(self, text=text).grid(column=1, row=row)
        Entry(self, width=3, textvariable=var).grid(column=2, row=row)


    def update_settings(self):
        uinterval = self.interval_entry.get()
        ubreak_time = self.break_time_entry.get()
        ulong_break_time = self.long_break_time_entry.get()
        ubreak_check = self.break_check_entry.get()

        if uinterval.isdigit() and ubreak_time.isdigit() and ulong_break_time.isdigit() and ubreak_check.isdigit():
            interval = int(uinterval)
            break_time = int(ubreak_time)
            long_break_time = int(ulong_break_time)
            break_check = int(ubreak_check)
            print "all recieved!"
            print "interval = %s" % str(interval)
            self.destroy()
        else:
            tkMessageBox.showinfo(title="Error", message="Please enter numeric value only.")
