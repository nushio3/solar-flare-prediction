#!/usr/bin/env python

import urllib, calendar, os

os.chdir("/home/takuya/bbt/secchi/a")


cal = calendar.Calendar()

yearstart = 2010
yearend = 2013


for i in range(yearstart,yearend):
    os.mkdir(str(i))
    for j in range(1,13):
        fname = str(i)+"/"+str(j).zfill(2)+".txt"
        fp = open(fname, "w")
        date = str(i)+"/"+str(j).zfill(2)
 
        url = "http://secchi.nrl.navy.mil/cactus/SECCHI-A/"+date+"/out/cmecat.txt"

        ff = urllib.urlopen(url)
        fp.write(ff.read())
        fp.close()
        print fname

