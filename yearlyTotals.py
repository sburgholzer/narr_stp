#File: yearlyTotals.py
#Author: Scott Burgholzer
#Date: 2/9/2017
#Modified: 2/9/2017
#Purpose: To calculate how many hours per year of STP there were

import matplotlib
matplotlib.use('Agg')
import numpy as np
from netCDF4 import Dataset
import matplotlib.pyplot as plt


data_path = '/home/sburgholzer/RESEARCH/narr/data/yearly/greaterthan1/clipped/'
years = np.arange(1980,2017,1)
total = 0
totals = []
for yr in years:
	gr = data_path + '%s.nc' % (str(yr))
	#print gr
	fh = Dataset(gr, mode='r')
	stp = fh.variables["stphours"][:]
	total = np.sum(stp)
	totals.append(total)
	fh.close()

maxIndex = totals.index(max(totals))
minIndex = totals.index(min(totals))

fig = plt.figure()
fig.suptitle('Total STP Hours Per Year for STP > 1', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
fig.subplots_adjust(top=0.85)
ax.set_title('Max: %i hours for year %i\n Min: %i hours for year %i' % (totals[maxIndex], years[maxIndex], totals[minIndex], years[minIndex]))
ax.set_xlabel('Years')
ax.set_ylabel('STP Hours')

#ax.text(0.1, 0.9,'Max STP Hours: %i for year: %i' % (totals[maxIndex], years[maxIndex]), ha='center', va='center', transform=ax.transAxes, fontsize = 5)


ax.plot(years, totals)
#plt.title('Max STP Hours: %i | year: %i' % (totals[maxIndex], years[maxIndex]))
plt.savefig('/home/sburgholzer/public_html/stp/testLine.png')