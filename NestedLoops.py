from netCDF4 import Dataset
import numpy

# dataset declaration

ncdf = Dataset('file_path')
variables = ncdf.variables

# global variables of import

currentSeaState = {
  significantWaveHeight = 0,
  recordedRogueWaves = 0,
  waveHistory = {}
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
  relEnergyInFrequency = variables["RelativeEnergyInFrequency"][:]
}
