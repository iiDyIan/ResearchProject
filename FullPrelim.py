from netCDF4 import Dataset
import numpy
import statistics
import matplotlib.pyplot as plt
import os

mainDirectory = 'Data'

# dataset declaration

mainCount = 0
count = 0

timeList = []

def counter(a,b,c,d):
  for e,f,g,h in numpy.nditer([a,b,c,d]):
    if e >= 2*h:
      global count
      count += 1
      timeList.append([f,g])
    else:
      global mainCount
      mainCount += 1

for filename in os.listdir(mainDirectory):
  f = os.path.join(mainDirectory, filename)

  if os.path.isfile(f):
    ncdf = Dataset(f)
    variables = ncdf.variables

    print("Firing up "+f+"!")

    counter(variables["wave_height"][:], variables["wave_start_time"][:], variables["wave_end_time"][:], variables["sea_state_30m_significant_wave_height_direct"][:])

print("All counting finished, moving on!!!")

runningTotal = 0
runningTotal2 = 0

timeLengthList = []
tDiffList = []

currentRWTime = 0

for i in timeList:
  a = abs(i[1]-i[0])/1000
  runningTotal += a
  timeLengthList.append(a)
  if currentRWTime != 0:
    tDiffList.append((i[0]-currentRWTime)/1000/60/60)
    currentRWTime = i[1]
  else:
   # tDiffList.append(0)
    currentRWTime = i[1]

print("Average time length")
print(runningTotal/len(timeList))

tDiffList.sort()
print(tDiffList)

count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0
count10 = 0
count11 = 0
count12 = 0
count13 = 0
count14 = 0
count15 = 0
count16 = 0
count17 = 0
count18 = 0
count19 = 0
count20 = 0
count21 = 0
count22 = 0
count23 = 0
count24 = 0
count25 = 0
count26 = 0
count27 = 0
count28 = 0
count29 = 0
count30 = 0
count31 = 0
count32 = 0
count33 = 0
count34 = 0
count35 = 0
count36 = 0
count37 = 0

count65 = 0

idList = []
v = 0

for i in tDiffList:
  count65 += 1
  idList.append(v+1)
  v += 1

  if i <= 1:
    count2 += 1
  elif i <= 2:
    count3 += 1
  elif i <= 3:
    count4 += 1
  elif i <= 4:
    count5 += 1
  elif i <= 5:
    count6 += 1
  elif i <= 6:
    count7 += 1
  elif i <= 7:
    count8 += 1
  elif i <= 8:
    count9 += 1
  elif i <= 9:
    count10 += 1
  elif i <= 10:
    count11 += 1
  elif i <= 11:
    count12 += 1
  elif i <= 12:
    count13 += 1
  elif i <= 13:
    count14 += 1
  elif i <= 14:
    count15 += 1
  elif i <= 15:
    count16 += 1
  elif i <= 16:
    count17 += 1
  elif i <= 17:
    count18 += 1
  elif i <= 18:
    count19 += 1
  elif i <= 19:
    count20 += 1
  elif i <= 20:
    count21 += 1
  elif i <= 21:
    count22 += 1
  elif i <= 22:
    count23 += 1
  elif i <= 23:
    count24 += 1
  elif i <= 24:
    count25 += 1
  elif i <= 25:
    count26 += 1
  elif i <= 26:
    count27 += 1
  elif i <= 27:
    count28 += 1
  elif i <= 28:
    count29 += 1
  elif i <= 29:
    count30 += 1
  elif i <= 30:
    count31 += 1
  elif i <= 31:
    count32 += 1
  elif i <= 32:
    count33 += 1
  elif i <= 33:
    count34 += 1
  elif i <= 34:
    count35 += 1
  elif i <= 35:
    count36 += 1

listOfFrequency = [count2, count3, count4, count5, count6, count7, count8, count9, count10, count11, count12, count13, count14, count15, count16, count17, count18, count19, count20, count21, count22, count23, count24, count25, count26, count27, count28, count29, count30, count31, count32, count33, count34, count35, count36]
frequencyListX = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
frequencyListLabels = ['0-1', "2", "3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35"]
 
plt.style.use("ggplot")

plt_1 = plt.figure(figsize=(22,10.5))
#plt.figure.set_figwidth(8.5)
#plt.figure.set_figlength(11)

plt.bar(frequencyListX, listOfFrequency, tick_label=frequencyListLabels,width=.35)
plt.ylabel("Rogues Occurrences")
plt.xlabel("Hour \"Sections\"")
#plt.xticks(frequencyListLabels)

plt.title("Rogue Wave Timing Relations")

plt.show()

print("Number of rogue waves occuring within an hour of one another:")
print(count2)
print((count2/count65)*100)

print("Number of rogue waves occuring within 1-2 hours of one another:")
print(count3)
print((count3/count65)*100)

print("Number of rogue waves occuring with 3+ hours after the last:")
print(count4)
print((count4/count65)*100)

print("Mean time between Rogue Wave events:")
print(sum(tDiffList)/len(tDiffList))

print("25th Percentile")
print(tDiffList[int(len(tDiffList)/4)])

print("75th Percentile")
print(tDiffList[int(3*(len(tDiffList)/4))])

print("Standard Deviation")
print(statistics.pstdev(tDiffList))

# average time length for all waves in set: 8.677434967607313
# average time length for rogue waves in set: 13.150999999999998, 11.05033379758588

plt.style.use("fivethirtyeight")

plt.plot(idList, tDiffList)
plt.xlabel('Internal Wave-ID')
plt.ylabel('Time Between Rogue Occurrence')
plt.xlim(1,count)
  
plt.show()

print(count)
print(mainCount)
print(100*(count/mainCount))
