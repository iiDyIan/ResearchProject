from netCDF4 import Dataset
import numpy
import statistics

# dataset declaration

ncdf = Dataset('file_path')
variables = ncdf.variables

count = 0

timeList = []

# global variables of import

def counter(a,b,c,d):
  for i, j, f, v in range zip(range(a), range(b), range(c), range(d)):
    # looping here
    if i > v:
      count += 1
      timeList.append([j,f])
      
counter(variables["wave_height"], variables["wave_start_time"], variables["wave_end_time"],variables["sea_state_30m_significant_wave_height_direct"])

runningTotal = 0
tDiffList = []

for i, in range(timeList):
  a = abs(i[1]-i[0])
  runningTotal += a
  tDiffList.append(a)

print("Average")
print(runningTotal/len(timeList))
tDiffList.sort()

print("25th Percentile")
print(tDiffList[len(tDiffList)/4])

print("75th Percentile")
print(tDiffList[3*(len(tDiffList)/4)])

print("Standard Deviation")
print(statistics.pstdev(tDiffList))
  
print(count)
