@echo off
set XSECT_GRIB_BACKEND=auto
set XSECT_CACHE_DIR=C:\Users\drew\hrrr-maps\cache\xsect
set XSECT_OUTPUTS_DIR=C:\Users\drew\hrrr-maps\outputs
set XSECT_ARCHIVE_DIR=E:\hrrr-archive,F:\hrrr-archive,H:\hrrr-archive
cd /d C:\Users\drew\hrrr-maps
C:\Users\drew\miniforge3\envs\wxsection\python.exe tools\unified_dashboard.py --port 5565 --models hrrr,gfs,rrfs
