import timer as my_timer
import sched, threading
import settings as s
import signal
import os
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator


APPINDICATOR_ID = 'eyebreaktimer'
breaks = 0
interval_timer = None
enabled = True

def create_menu():
    menu = gtk.Menu()
    #disable
    disable_item = gtk.CheckMenuItem('Disable timer')
    disable_item.connect('activate', toggle_timer)
    menu.append(disable_item)
    #settings
    #settings_item = gtk.MenuItem('Settings')
    #settings_item.connect('activate', open_settings)
    #menu.append(settings_item)
    #quit
    quit_item = gtk.MenuItem('Quit')
    quit_item.connect('activate', quit)
    menu.append(quit_item)
    menu.show_all()
    return menu


def quit(source):
    interval_timer.cancel()
    gtk.main_quit()


#def open_settings(source):
#    app = s.Settings(None)
#    app.title("Settings")
#    app.mainloop()
#    global interval_timer
#    interval_timer.cancel()
#    run_timer()


def toggle_timer(source=""):
    global interval_timer
    global enabled
    if enabled:
        interval_timer.cancel()
        enabled = not enabled
    else:
        enabled = True
        run_timer()


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('clock.png'),
                                           appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(create_menu())
    gtk.main()


def run_timer():
    global breaks
    global interval_timer
    timer = my_timer.Timer(None)
    if breaks >= s.break_check:
        timer.take_long_break()
        breaks = 0
    else:
        timer.take_break()
        breaks += 1
    if enabled:
        interval_timer = threading.Timer(s.interval, run_timer)
        interval_timer.start()


if __name__ == "__main__":
    run_timer()
    main()
