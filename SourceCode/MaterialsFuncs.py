import math

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

def GetTotalVolumeOfWaterDisplaced(pipeDiameter, wallThickness, pipeLength):
    pipeDiameter = ConvertInchToMeters(pipeDiameter)
    wallThickness = ConvertInchToMeters(wallThickness)
    # find volume of just the metal part of the cylinder
    # volume of a cylinder = radius^2 * height * pi
    # volume in units of m^3
    volumeOfOutsidePipe = math.pow((pipeDiameter / 2), 2) * pipeLength * math.pi
    volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi
    totalVolume = volumeOfOutsidePipe + volumeOfCircle

    return (totalVolume)

def GetAvailableVolume(pipeDiameter, wallThickness, pipeLength):
    # conversion from inches to m
    pipeDiameter = ConvertInchToMeters(pipeDiameter)
    wallThickness = ConvertInchToMeters(wallThickness)
    # find volume of just the metal part of the cylinder
    # volume of a cylinder = radius^2 * height * pi
    # volume in units of m^3
    volumeOfInsidePipe = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * pipeLength * math.pi
    volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi

    availableVolume = volumeOfInsidePipe - volumeOfCircle
    
    return (availableVolume)

def GetMaterialMass(pipeDiameter, wallThickness, pipeLength, density):
    materialVolume = GetMaterialVolume(pipeDiameter, wallThickness, pipeLength)
    # mass = density of pipe * volume of pipe
    # mass in units of grams
    mass = density * materialVolume

    return(mass)

def GetMaterialWeight(pipeDiameter, wallThickness, pipeLength, density):
    weight = GetMaterialMass(pipeDiameter, wallThickness, pipeLength, density) * GRAVITY

    return weight

def GetBoyantForceOfPipe(pipeDiameter, wallThickness, pipeLength):
    buoyantForce = GetTotalVolumeOfWaterDisplaced(pipeDiameter, wallThickness, pipeLength) * WATER_DENSITY * GRAVITY

    return(buoyantForce)