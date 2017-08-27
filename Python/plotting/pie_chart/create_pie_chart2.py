#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 25, 2017 Tue
""" Create pie chart usign pylab.

.. note::

  We may need to update libpng to run this program .
  
  locate libpng16.16.dylib
  
  cd /usr/local/lib
  
  ln -s /Users/poudel/anaconda/pkgs/libpng-1.6.27-0/lib/libpng16.16.dylib
  
  
  """


# Imports
from pylab import *
import matplotlib.pyplot as plt


def main():
    """Main Module."""
    # make a square figure and axes
    figure(1, figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])

    # The slices will be ordered and plotted counter-clockwise.
    labels = 'Dark Energy', 'Dark Matter', 'Normal Matter'
    fracs = [75, 21, 4]
    explode=(0, 0.05, 0)

    pie(fracs, explode=explode, labels=labels,
                    autopct='%1.1f%%', shadow=True, startangle=90)
                    # The default startangle is 0, which would start
                    # the Frogs slice on the x-axis.  With startangle=90,
                    # everything is rotated counter-clockwise by 90 degrees,
                    # so the plotting starts on the positive y-axis.

    title('Contents of Universe', bbox={'facecolor':'0.8', 'pad':5})
    
    savefig('pie-chart.png')

    show()

    

if __name__ == '__main__':
    main()
