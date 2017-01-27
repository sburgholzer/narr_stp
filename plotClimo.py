import matplotlib
matplotlib.use('Agg')
from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, cm
from matplotlib import cm as cm
from matplotlib.colors import LinearSegmentedColormap

ncFile = '/home/sburgholzer/RESEARCH/narr/data/climo/greaterThan1/climo.nc'
fh = Dataset(ncFile, mode='r')
stp = fh.variables["stphours"][:]
lats = fh.variables["lats"][:]
lons = fh.variables["lons"][:]
fh.close()

#plot the map
fig = plt.figure()
fig.set_size_inches(11,7.5)
fig = fig.add_subplot(111,frameon=False)
m = Basemap  (projection='lcc',lon_0=-92.54199,lat_0=38.09401,llcrnrlat=20,
	urcrnrlat=55,llcrnrlon=-120,urcrnrlon=-60,resolution='l',area_thresh=1000)
m.drawcoastlines(color='gray')
m.drawstates(color='gray')
m.drawcountries()
x,y = m(lons,lats)
colors = [('white')] + [(cm.gist_ncar(i)) for i in range(1,256)]
new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)
cmap = plt.get_cmap(new_map)
plot = m.pcolormesh(x,y,stp/35,shading='flat',cmap=cmap)
colbar = m.colorbar(plot,"bottom",size="4%",pad="5%",extend='max')
colbar.set_label('1980-2016 Avg. STP Hours >1',fontsize='medium',weight='bold')
plt.title =('1980-2015 Ave STP Hours')
plt.savefig('/home/sburgholzer/public_html/stp/19802016STPgreaterThan1.png',bbox_inches='tight', dpi=200)
