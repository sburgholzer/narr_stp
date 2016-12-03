*Purpose: Custom NARR file GrADS plotter
*Author: Gensini, Fall 2016
*Modified: Burgholzer, Fall 2016
*************************************************************************
function main(args)
 year=subwrd(args,1)
 month=subwrd(args,2)

 if month = 01 | month = 03 | month = 05 | month = 07 | month = 08 | month = 10 | month = 12
 endTime = 248
endif
if month = 04 | month = 06 | month = 09 | month = 11
 endTime = 240
endif
if month = 02
 if year = 1980 | year = 1984 | year = 1988 | year = 1992 | year = 1996 | year = 2000 | year = 2004 | year = 2008 | year = 2012 | year = 2016
  endTime = 232
 else
  endTime = 224
 endif
endif



'open /home/sburgholzer/narr/narr.ctl'


*START: PRODUCT SPECIFIC ACTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



'define ndays = sum( maskout(stpfin/stpfin, stpfin-1.), t=1,t=240)'
'define stphours = ndays/3'

'set sdfwrite 'year'_'month'.nc'
'sdfwrite stphours'
