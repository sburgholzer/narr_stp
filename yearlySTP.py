#File:	yearlySTP.py
#Author: Scott Burgholzer
#Date: 12/3/2016
#Modified: 12/3/2016
#Purpose: To calculate the total 3 hourly intervals of STP for each year
#         and calculate how many times that occured

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap, cm
from netCDF4 import Dataset
import scipy.ndimage
from matplotlib.path import Path
import shapefile

# get shapefile information for clipping
sf = shapefile.Reader('/home/sburgholzer/RESEARCH/narr/shapefiles/narr_clip')
sfrec = sf.shapeRecord()
points = sfrec.shape.points
fh = Dataset('/home/sburgholzer/RESEARCH/narr/data/narr_conv_20110101_0000.nc', mode='r')
lons = fh.variables["lons"][:]
lats = fh.variables["lats"][:]
fh.close()

lat = lats.flatten()
lon = lons.flatten()
lonlat = []
for lt,ln in zip(lat,lon):
	lonlat.append([ln,lt])
path = Path(points)
clip = path.contains_points(lonlat)
clip = clip.reshape(lats.shape)

# now with clipping done, we can get the data
data_path = '/home/sburgholzer/RESEARCH/narr/data/monthly/greaterThan1/'
years = np.arange(1980,2017,1)
months = np.arange(1,13,1)
count_stp =  np.zeros((277,349))
for yr in years:
	print 'Starting %s' % (str(yr))
	for mn in months:
		if (mn < 10):
			newMn = '0%s' % mn
		else:
			newMn = mn
		gr = data_path + '%s_%s.nc' % (str(yr), str(newMn))
		fh = Dataset(gr, mode='r')
		stp  = fh.variables["stphours"][:]
		lons  = fh.variables["lons"][:]
		lats  = fh.variables["lats"][:]
		count_stp = np.add(count_stp, stp)
		count_stp = np.ma.masked_where(clip==False,count_stp)
		fh.close()
	gr = '/home/sburgholzer/RESEARCH/narr/data/yearly/greaterthan1/clipped/%s.nc' % (str(yr))
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
	count_stp =  np.zeros((277,349))
	print 'Ending %s' % (str(yr))
