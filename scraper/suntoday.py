#!/usr/bin/env python

import urllib, calendar, os

os.chdir("/home/takuya/bbt/suntoday")


cal = calendar.Calendar()

yearstart = 2010
yearend = 2013


for i in range(yearstart,yearend):
    os.mkdir(str(i))
    for j in range(1,13):
        dirname = str(i)+"/"+str(j).zfill(2)
        os.mkdir(dirname)
        for k in cal.itermonthdays(i,j):
            if k==0: continue
            fname = str(i)+"/"+str(j).zfill(2)+"/"+str(k).zfill(2)+".json"
            fp = open(fname, "w")
            datestart = str(i)+"-"+str(j)+"-"+str(k)
            dateend = str(i)+"-"+str(j)+"-"+str(k+1)
 
            url = "https://www.lmsal.com/hek/her?cosec=2&&cmd=search&type=column&event_type=ar,ce,ch,cj,cw,fe,fa,fl,os,sg,sp&event_region=all&event_coordsys=helioprojective&x1=-5000&x2=5000&y1=-5000&y2=5000&result_limit=120&event_starttime="+datestart+"T00:00:00&event_endtime="+dateend+"T00:00:00&param0=ch.area_atdiskcenter&op0=%3E&value0=608735000"

            json = urllib.urlopen(url)
            fp.write(json.read())
            fp.close()
            print fname

