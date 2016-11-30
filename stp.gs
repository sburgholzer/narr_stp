*Purpose: Custom NARR file GrADS plotter
*Author: Gensini, Fall 2016
*Modified: Burgholzer, Fall 2016
*************************************************************************
'reinit'
'set annot 99 1'
'set frame on'
'set display color white'
'c'
'set rgb 99 0 0 0'
'set string 99 l 1 0'
'set rgb 100 255 255 255'
'set mpt 2 99 1 2'
'set xlab off'
'set ylab off'
'set poli on'
'set rgb 101 40 40 40 0'
'set background 101'
'set clab forced'
'set clopts -1 -1 0.08'
'set clskip 1 2.5'
'set grid off'
'set map 99'
'set csmooth off'
'set parea 0 11 0 8.5'
'set mproj latlon'
'set font 4'
'set datawarn off'
'set grads off'
'set mpdraw off'
filext = '.png'
basedir = '/home/sburgholzer/narr/narr_stp/'
ctlext = '.ctl'
'open /home/sburgholzer/narr/narr_stp/narr.ctl'
'set lat 22 58'
'set lon 232 294'
*START: PRODUCT SPECIFIC ACTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*give the image a product title
'draw string 0.1 8.3 NARR | April 2012 STP Hours > 1 (all hours)'
*give the product a name between sector and fhour variables and combo into filename variables
prodname = 2012apr_stp_h
filename = basedir'/'prodname%filext
*pick a colorbar
*'set gxout shade2'
*'run /home/scripts/grads/colorbars/color.gs -levs 1 2 3 4 5 6 7 8 9 10 -kind white->(210,210,210)->(50,255,31)->(151,253,23)->(252,245,15)->(251,128,7)->(249,5,0)->(249,0,80)->(249,0,167)->(245,0,249)->(158,0,249)->(180,100,225)->cyan'
*'d max(stpfin,t=1,t=2920)'
'define ndays = sum( maskout(stpfin/stpfin, stpfin-1.), t=1,t=240)'
*'d smth9(ndays/3)'
* Define stpHours
'define stpHours = ndays/3'
'set rgb 98 0 0 0 40'
'set line 98 1 1'
'draw shp /home/scripts/grads/shapefiles/counties.shp'
'set mpdraw off'
'set line 99 1 1'
'draw shp /home/scripts/grads/shapefiles/states.shp'
*END: PRODUCT SPECIFIC ACTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*plot the colorbar on the image
'run /home/scripts/grads/functions/pltcolorbar.gs -ft 1 -fy 0.33 -line on -fskip 1 -fh .1 -fw .1 -lc 99 -edge triangle -fc 99'
*generate the image
*'run /home/scripts/grads/functions/make_image.gs 'filename
*write month's STP Hours to a new netcdf file
'set sdfwrite april2012.nc'
'sdfwrite stpHours'
