#File:	yearlySTP.py
#Author: Scott Burgholzer
#Date: 12/3/2016
#Modified: 01/27/2016
#Purpose: To calculate the total 3 hourly intervals of STP for each year
#         and calculate how many times that occured

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap, cm
from netCDF4 import Dataset
import scipy.ndimage

data_path = '/home/sburgholzer/RESEARCH/narr/data/yearly/greaterthan1/'
years = np.arange(1980,2017,1)
count_stp =  np.zeros((277,349))
print 'Starting climo'
for yr in years:
	gr = data_path + '%s.nc' % (str(yr))
	print gr
	fh = Dataset(gr, mode='r')
	stp  = fh.variables["stphours"][:]
	lons  = fh.variables["lons"][:]
	lats  = fh.variables["lats"][:]
	count_stp = np.add(count_stp, stp)
	fh.close()
	
gr = '/home/sburgholzer/RESEARCH/narr/data/climo/greaterThan1/climo.nc'
ncfile = Dataset(gr, mode='w', format='NETCDF4')
ncfile.createDimension('latitude',277)
ncfile.createDimension('longitude',349)
latitude = ncfile.createVariable('lats','d',('latitude','longitude'))
longitude = ncfile.createVariable('lons','d',('latitude','longitude'))
nc_stpHours = ncfile.createVariable('stphours','d',('latitude','longitude'))
latitude[:] = lats
longitude[:] = lons
nc_stpHours[:] = count_stp
ncfile.close()
print 'Ending Climo'
