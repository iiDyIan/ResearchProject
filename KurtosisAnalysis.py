from netCDF4 import Dataset
import numpy
import statistics
import matplotlib.pyplot as plt
import os

mainDirectory = 'Data'

count = 0
mainCount = 0

kurtosisDataRW = []
kurtosisDataG = []

def counter(a,b,c,d,e):
  for z,f,g,h,j in numpy.nditer([a,b,c,d,e]):
    if z >= 2*h:
      global count
      count += 1
      kurtosisDataRW.append([f,g,j])
    else:
      global mainCount
      mainCount += 1
      kurtosisDataG.append([f,g,j])

for filename in os.listdir(mainDirectory):
  f = os.path.join(mainDirectory, filename)

  if os.path.isfile(f):
    ncdf = Dataset(f)
    variables = ncdf.variables

    print("Firing up "+f+"!")

    counter(variables["wave_height"][:], variables["sea_state_10m_kurtosis"][:], variables["sea_state_30m_kurtosis"][:], variables["sea_state_30m_significant_wave_height_direct"][:], variables["wave_id_local"][:])

print("Beginning final tally.")

outputDataRW = []
outputDataG2 = []

outputDataG = []
outputDataRW2 = []

print(len(kurtosisDataRW))

for i in kurtosisDataG:
  outputDataG2.append(abs(i[0]-i[1]))
  outputDataG.append(i[2])

for i in kurtosisDataRW:
  outputDataRW.append(abs(i[0]-i[1]))
  outputDataRW2.append(i[2])

print(len(outputDataG2))

avgRW = sum(outputDataRW)/len(outputDataRW)
avgG = sum(outputDataG2)/len(outputDataG2)

print("Average RW difference between 10m and 30m Sea-State Kurtosis")
print(avgRW)

print("Average wave difference between 10m and 30m Sea-State Kurtosis")
print(avgG)

print("Percent Change")
print(str(100*(abs(avgRW-avgG)/((avgRW+avgG)/2)))+"%")

print(mainCount+count)

plt.style.use("ggplot")
plt.ylabel("Difference between 10 and 30m Sea State Kurtosis")
plt.xlabel("Wave ID (Local)")
plt.ylim(-.125,5)
plt.xlim(1,mainCount+count)
plt.scatter(outputDataG, outputDataG2, label = "Typical Waves", s=2)
plt.plot(outputDataRW2,outputDataRW, label = "Rogue Waves", color="blue")
plt.legend()
plt.show()

print("Complete.")
