#!/usr/bin/env ruby

require 'open-uri'

year = 2012
month = 5

(1..30).each{|day|

  ymd = sprintf("%04d-%02d-%02d", year, month, day)
  ymd1 = sprintf("%04d-%02d-%02d", year, month, day+1)
  ymdir = sprintf("%04d/%02d", year, month)
  fn =  sprintf("%04d/%02d/%02d.json", year, month, day)
  `mkdir -p #{ymdir}`
  url = "https://www.lmsal.com/hek/her?cosec=2&&cmd=search&type=column&event_type=ar,ce,ch,cj,cw,fe,fa,fl,os,sg,sp&event_region=all&event_coordsys=helioprojective&x1=-5000&x2=5000&y1=-5000&y2=5000&result_limit=120&event_starttime=#{ymd}T00:00:00&event_endtime=2012-05-#{ymd1}T00:00:00&param0=ch.area_atdiskcenter&op0=%3E&value0=608735000"

  STDERR.puts "getting #{ymd}"
  open(fn, 'w') {|fp2|
    open(url,'r'){|fp|
      fp2.write(fp.read)
    }
  }
}
