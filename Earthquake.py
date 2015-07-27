#!/usr/bin/env python
""" This script prints the last 5 earthquake occured in Nepal in your terminal.
"""
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
        
data=get_page('https://docs.google.com/spreadsheets/u/0/d/1eeIOB58Dn5qRNWTySqrL35U8xY3JjZ7yhg5Dpxvbz8s/export' \
              '?format=csv&id=1eeIOB58Dn5qRNWTySqrL35U8xY3JjZ7yhg5Dpxvbz8s&gid=0')
print "Recent Earthquakes"
print data[111:-1]              
