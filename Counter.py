from netCDF4 import Dataset
import numpy

# dataset declaration

ncdf = Dataset('file_path')
variables = ncdf.variables

count = 0

# global variables of import

def counter(a,b,c,d):
  for i, j, f, v in range zip(range(a), range(b)):
    # looping here
    if i > v:
      count += 1
      
counter(variables["wave_height"], variables["wave_start_time"], variables["wave_end_time"],variables["sea_state_30m_significant_wave_height_direct"])

print(count)
