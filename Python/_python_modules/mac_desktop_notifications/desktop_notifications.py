#!python
# -*- coding: utf-8 -*-#
#
# Author      : Bhishan Poudel; Physics Graduate Student, Ohio University
# Date        : Aug 17, 2017 Thu
"""
Applescript to display notifications.

osascript -e 'tell app "System Events" to display alert "Hello World"'  # best
osascript -e 'display notification "This program finished." with title "Nofification"'
display notification "message" with title "title" subtitle "subtitle"
display notification "message" sound name "default"
osascript -e 'tell app "System Events" to display dialog "Hello World"'
osascript -e 'tell app "Finder" to display dialog "Hello World"'
"""


# Imports
import subprocess
import time

def notify_with_OK():
    """Notify program end time on MacOS.

    ..warning::

      This will prevent python script from closing, despite the fact
      that the code below this fucntion runs as usual.
    """
    osa = r'''osascript -e 'tell app "System Events" to display alert '''
    msg = "\" Program finished on \n {}\"".format(tm)
    notif = osa + msg + "'&"
    subprocess.call(notif, shell=True)
    print('This is after error notification.')

def notify():
    """Using desktop notifications in macos.

    ..note::

      To keep the notification button until you close it chage the
      system preferences of the notifications.
      System Preferences > Nofitications > Script Editor > Check all and choose alert

    """
    osa = r'''osascript -e 'display notification '''
    tm = time.ctime()
    msg = "\" Program finished on \n {}\"".format(tm)
    title = r'''with title "Notification"'''
    notif = osa + msg + title + "'&"
    subprocess.call(notif, shell=True)


def main():
    # notify_with_OK()
    notify()


if __name__ == "__main__":
    main()
