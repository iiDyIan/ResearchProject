from netCDF4 import Dataset
import numpy

# dataset declaration

ncdf = Dataset('file_path')
variables = ncdf.variables

# global variables of import

currentSeaState = {
  significantWaveHeight = 0,
  recordedRogueWaves = 0,
  waveHistory = {},
}

# all input variables

inputVariableIndexes = {
  skewness = variables["Skewness"][:],
  kurtosis = variables["Kurtosis"][:],
  peakWavePeriod = variables["PeakWavePeriod"][:],
  peakWavelength = variables["PeakWavelength"][:],
  steepness = variables["Steepness"][:],
  bandwith = variables["Bandwith"][:],
  bejaminFeirIndex = variables["BejaminFeirIndex"][:],
  crestTroughCorrelation = variables["CrestTroughCorrelation"][:],
  energyInFrequencyInterval = variables["EnergyInFrequency"][:],
  relEnergyInFrequency = variables["RelativeEnergyInFrequency"][:],
}

for s in range(len(skewness)) and for k in range(len(kurtosis)) and for pwP in range(len(peakWavePeriod)) and for pwL in range(len(peakWaveLength)) and for st in range(len(steepness)) and for b in range(len(bandwith)) and for bfi in range(len(bejaminFeirIndex)) and for ctc in range(len(crestTroughCorrelation)) and for eiFI in range(len(energyInFrequencyInterval)) and for reFI in range(len(relEnergyInFrequency)):
  
  print("Test!")
  
  
