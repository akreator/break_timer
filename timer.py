import tkMessageBox, Tkinter, time, settings as s
from Tkinter import *
from gi.repository import Gtk as gtk

class Timer(Tkinter.Tk):

    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()


    def initialize(self):
        self.title("Take a Break")
        self.text = StringVar()
        self.text.set("Break time!")
        l = Label(self, textvariable=self.text)
        l.pack()


    def take_long_break(self):
        long_break = tkMessageBox.askyesno(title="Continue?", message="It's time for a long break.\nRest for %d minutes?" % (s.long_break_time / 60))
        if long_break:
            self.center(s.long_break_time)
            for x in range(s.break_time):
                self.text.set("Long break time!  \nLook away from the screen for %d seconds." % (s.long_break_time - x))
                self.update_idletasks()
                time.sleep(1)
        self.destroy()


    def take_break(self):
        self.center(s.break_time)
        for x in range(s.break_time):
            self.text.set("Break time!  \nLook away from the screen for %d seconds." % (s.break_time - x))
            self.update_idletasks()
            time.sleep(1)
        self.destroy()

    def center(self, start_time):
        self.text.set("Long break time!  \nLook away from the screen for %d seconds." % start_time)
        self.update_idletasks()
        w = self.geometry().split('x')[0]
        h = self.geometry().split('+')[0].split('x')[1]
        x = (int(self.winfo_screenwidth()) - int(w)) / 2
        y = (int(self.winfo_screenheight()) - int(h)) / 2
        self.geometry("%sx%s+%s+%s" % (w, h, x, y)) #widthxheight+xcoord+ycoord
