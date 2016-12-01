#!/bin/csh -f
foreach year (1980 1981 1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016)
	if $year == 2016 then
		foreach month (01 02 03 04 05 06 07 08)
			#make a narr .ctl file so that it has the right information
			rm narr.ctl
			if $month == 01 then
				set mo = jan
			else if $month == 02 then
				set mo = feb
			else if $month == 03 then
				set mo = mar
			else if $month == 04 then
				set mo = apr
			else if $month == 05 then
				set mo = may
			else if $month == 06 then
				set mo = jun
			else if $month == 07 then
				set mo = jul
			else if $month == 08 then
				set mo = aug
			else if $month == 09 then
				set mo = sep
			else if $month == 10 then
				set mo = oct
			else if $month == 11 then
				set mo = nov
			else if $month == 12 then
				set mo = dec
			endif

			echo dset /home/sburgholzer/RESEARCH/narr/narr_conv_${year}${month}%d2_%h200.nc > narr.ctl
			echo title narrstp >> narr.ctl
			echo undef 1.000E20 missing_value >> narr.ctl
			echo dtype netcdf >> narr.ctl
			echo options template >> narr.ctl
			echo PDEF 349 277 lcc 1 -145.5 1 1 50 50 -107 32463.41 32463.41 >> narr.ctl
			echo xdef 615 linear 150 .333 >> narr.ctl
			echo ydef 255 linear 2 .333 >> narr.ctl
			echo zdef 1 levels 0 >> narr.ctl
			if ($month == 01 || $month == 03 || $month == 05 || $month == 07 || $month == 08 || $month == 10 || $month == 12) then
				echo tdef 248 linear 00z01${mo}${year} 3hr >> narr.ctl
			else if ($month == 04 || $month == 06 || $month == 09 || $month == 11) then
				echo tdef 240 linear 00z01${mo}${year} 3hr >> narr.ctl
			else if ($month == 02) then
				if ($year == 1980 || $year == 1984 || $year == 1988 || $year == 1992 || $year == 1996 || $year == 2000 || $year == 2004 || $year == 2008 || $year == 2012 || $year == 2016) then
					echo tdef 232 linear 00z01${mo}${year} 3hr >> narr.ctl
				else
					echo tdef 224 linear 00z01${mo}${year} 3hr >> narr.ctl
				endif 
			endif
			echo vars 3 >> narr.ctl
			printf "stp=>stpfin 0 y,x SigTor\n" >> narr.ctl
			printf "lats=>glats 0 y,x Latitude\n" >> narr.ctl
			printf "lons=>glons 0 y,x Longitude\n" >> narr.ctl
			echo endvars >> narr.ctl

			grads -bxcl "run stp.gs ${year} ${month}" 
		end
	else
        	foreach month (01 02 03 04 05 06 07 08 09 10 11 12)
			 #make a narr .ctl file so that it has the right information
                        rm narr.ctl
                        if $month == 01 then
                                set mo = jan
                        else if $month == 02 then
                                set mo = feb
                        else if $month == 03 then
                                set mo = mar
                        else if $month == 04 then
                                set mo = apr
                        else if $month == 05 then
                                set mo = may
                        else if $month == 06 then
                                set mo = jun
                        else if $month == 07 then
                                set mo = jul
                        else if $month == 08 then
                                set mo = aug
                        else if $month == 09 then
                                set mo = sep
                        else if $month == 10 then
                                set mo = oct
                        else if $month == 11 then
                                set mo = nov
                        else if $month == 12 then
                                set mo = dec
                        endif

                        echo dset /home/sburgholzer/RESEARCH/narr/narr_conv_${year}${month}%d2_%h200.nc > narr.ctl
                        echo title narrstp >> narr.ctl
                        echo undef 1.000E20 missing_value >> narr.ctl
                        echo dtype netcdf >> narr.ctl
                        echo options template >> narr.ctl
                        echo PDEF 349 277 lcc 1 -145.5 1 1 50 50 -107 32463.41 32463.41 >> narr.ctl
                        echo xdef 615 linear 150 .333 >> narr.ctl
                        echo ydef 255 linear 2 .333 >> narr.ctl
                        echo zdef 1 levels 0 >> narr.ctl
                        if ($month == 01 || $month == 03 || $month == 05 || $month == 07 || $month == 08 || $month == 10 || $month == 12) then
                                echo tdef 248 linear 00z01${mo}${year} 3hr >> narr.ctl
                        else if ($month == 04 || $month == 06 || $month == 09 || $month == 11) then
                                echo tdef 240 linear 00z01${mo}${year} 3hr >> narr.ctl
                        else if ($month == 02) then
                                if ($year == 1980 || $year == 1984 || $year == 1988 || $year == 1992 || $year == 1996 || $year == 2000 || $year == 2004 || $year == 2008 || $year == 2012 || $year == 2016) then
                                        echo tdef 232 linear 00z01${mo}${year} 3hr >> narr.ctl
                                else
                                        echo tdef 224 linear 00z01${mo}${year} 3hr >> narr.ctl
                                endif
                        endif
                        echo vars 3 >> narr.ctl
                        printf "stp=>stpfin 0 y,x SigTor\n" >> narr.ctl
                        printf "lats=>glats 0 y,x Latitude\n" >> narr.ctl
                        printf "lons=>glons 0 y,x Longitude\n" >> narr.ctl
                        echo endvars >> narr.ctl

			grads -bxcl "run stp.gs ${year} ${month}"
		end
	endif
end
