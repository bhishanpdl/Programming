#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 25, 2017 Tue
# Ref: https://chrisalbon.com/python/matplotlib_pie_chart.html
""" Create pie chart usign pylab.

.. note::

  We may need to update libpng to run this program .
  
  locate libpng16.16.dylib
  
  cd /usr/local/lib
  
  ln -s /Users/poudel/anaconda/pkgs/libpng-1.6.27-0/lib/libpng16.16.dylib
  
  
  """


# Imports
import pandas as pd
import matplotlib.pyplot as plt


def main():
    """Main Module."""
    # make a square figure and axes
    raw_data = {'officer_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
            'jan_arrests': [4, 24, 31, 2, 3],
            'feb_arrests': [25, 94, 57, 62, 70],
            'march_arrests': [5, 43, 23, 23, 51]}
    df = pd.DataFrame(raw_data, columns = ['officer_name', 'jan_arrests', 'feb_arrests', 'march_arrests'])
    print(df)

    # Create a column with the total arrests for each officer
    df['total_arrests'] = df['jan_arrests'] + df['feb_arrests'] + df['march_arrests']
    print(df)
        
    # Create a list of colors (from iWantHue)
    colors = ["#E13F29", "#D69A80", "#D63B59", "#AE5552", "#CB5C3B", "#EB8076", "#96624E"]

    # Create a pie chart
    plt.pie(
        # using data total)arrests
        df['total_arrests'],
        # with the labels being officer names
        labels=df['officer_name'],
        # with no shadows
        shadow=False,
        # with colors
        colors=colors,
        # with one slide exploded out
        explode=(0, 0, 0, 0, 0.15),
        # with the start angle at 90%
        startangle=90,
        # with the percent listed as a fraction
        autopct='%1.1f%%',
        )

    # View the plot drop above
    plt.axis('equal')

    # View the plot
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()
