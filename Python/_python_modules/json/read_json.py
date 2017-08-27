#!python
# -*- coding: utf-8 -*-
#
# Author      : Bhishan Poudel, Physics PhD Student, Ohio University
# Date        : Jul 23, 2017 Sun
# Last update :
#
# Imports
import json
from pprint import pprint


def read_json():
    """ ."""
    
    with open('a.cson') as data_file:    
        data = json.load(data_file)

    pprint(data)
    #print(data["maps"][0]["id"])
    #print(data["masks"]["id"])
    #print(data["om_points"])

if __name__ == '__main__':
    read_json()
