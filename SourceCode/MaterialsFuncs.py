import math
import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

GRAVITY=9.8
WATER_DENSITY=1000

def ConvertInchToMeters(value):
    return (value * 2.54) / 100

def GetMaterialVolume(pipeDiameter, wallThickness, pipeLength):
    # conversion from inches to m
    pipeDiameter = ConvertInchToMeters(pipeDiameter)
    wallThickness = ConvertInchToMeters(wallThickness)
    # find volume of just the metal part of the cylinder
    # volume of a cylinder = radius^2 * height * pi
    # volume in units of m^3
    volumeOfOutsidePipe = math.pow((pipeDiameter / 2), 2) * pipeLength * math.pi
    volumeOfInsidePipe = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * pipeLength * math.pi
    volumeOfJustPipe = volumeOfOutsidePipe - volumeOfInsidePipe

    volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi
    totalVolume = volumeOfJustPipe + volumeOfCircle

    return (totalVolume)

def GetMaterialMass(pipeDiameter, wallThickness, pipeLength, density):
    materialVolume=GetMaterialVolume(pipeDiameter, wallThickness, pipeLength)
    # mass = density of pipe * volume of pipe
    # mass in units of grams
    mass = density * materialVolume
    return(mass)

def GetMaterialWeight(pipeDiameter, wallThickness, pipeLength, density):
    return GetMaterialMass(pipeDiameter, wallThickness, pipeLength, density) * GRAVITY

def GetBoyantForceOfPipe(pipeDiameter, wallThickness, pipeLength):
    pipeDiameter=ConvertInchToMeters(pipeDiameter)
    return GetMaterialVolume(pipeDiameter, wallThickness, pipeLength) * WATER_DENSITY * GRAVITY
