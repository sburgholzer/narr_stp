#File#File:	monthlySTP.py
#Author: Scott Burgholzer
#Date: 12/2/2016
#Modified: 02/09/2016
#Purpose: To calculate the total 3 hourly intervals of STP for each month
#         and calculate how many times that occured

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import numpy.ma as ma
from mpl_toolkits.basemap import Basemap, cm
from netCDF4 import Dataset
import scipy.ndimage
import shapefile
from matplotlib.path import Path

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

data_path = '/home/sburgholzer/RESEARCH/narr/data/'
years = np.arange(1980,2017,1)
months = np.arange(1,13,1)
hours = ['0000','0300','0600','0900','1200','1500','1800','2100']
count_stp =  np.zeros((277,349))
for yr in years:
	for mn in months:
		if (mn == 1):
			dyvals = np.arange(1,32,1)
		elif (mn == 2):
			dyvals = np.arange(1,29,1)
		elif (mn == 3):
			dyvals = np.arange(1,32,1)
		elif (mn == 4):
			dyvals = np.arange(1,31,1)
		elif (mn == 5):
			dyvals = np.arange(1,32,1)
		elif (mn == 6):
			dyvals = np.arange(1,31,1)
		elif (mn == 7):
			dyvals = np.arange(1,32,1)
		elif (mn == 8):
			dyvals = np.arange(1,32,1)
		elif (mn == 9):
			dyvals = np.arange(1,31,1)
		elif (mn == 10):
			dyvals = np.arange(1,32,1)
		elif (mn == 11):
			dyvals = np.arange(1,31,1)
		elif (mn == 12):
			dyvals = np.arange(1,32,1)
		print 'Starting %s %s' % (str(mn), str(yr))
		for dy in dyvals:
			for hr in hours:
					gr = data_path + 'narr_conv_%s.nc' % (str(yr) + '%02d' % mn + '%02d' % dy +'_'+hr)
					fh = Dataset(gr, mode='r')
					stp  = fh.variables["stp"][:]
					cin = fh.variables["sbcin"][:]
					lons  = fh.variables["lons"][:]
					lats  = fh.variables["lats"][:]
					stp = np.array((stp >= 1) & (cin >= -5), dtype=int)
					count_stp = np.add(count_stp, stp == 1)
					count_stp = ma.masked_where(count_stp == 248, count_stp)
					count_stp = np.ma.masked_where(clip==False,count_stp)
					fh.close()
		if (mn < 10):
			mn = '0%s' % str(mn)
		gr = '/home/sburgholzer/RESEARCH/narr/data/monthly/greaterThan1/clipped/%s_%s.nc' % (str(yr), str(mn))
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
		print 'Ending %s %s' % (str(mn), str(yr))
