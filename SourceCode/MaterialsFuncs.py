import math

GRAVITY=9.8
WATER_DENSITY=1000

def ConvertInchToMeters(value):
    return (value * 2.54) / 100 #m

def GetMaterialVolume(pipeDiameter, wallThickness, pipeLength):
    # conversion from inches to m
    pipeDiameter = ConvertInchToMeters(pipeDiameter)
    wallThickness = ConvertInchToMeters(wallThickness)

    # find volume of just the metal part of the cylinder
    # volume of a cylinder = radius^2 * height * pi
    # volume in units of m^3
    volumeOfOutsidePipe = math.pow((pipeDiameter / 2), 2) * pipeLength * math.pi #m^3
    volumeOfInsidePipe = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * pipeLength * math.pi #m^3
    volumeOfJustPipe = volumeOfOutsidePipe - volumeOfInsidePipe #m^3

    volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi #m^3
    totalVolume = volumeOfJustPipe + volumeOfCircle #m^3

    return (totalVolume) #m^3

def GetTotalVolumeOfWaterDisplaced(pipeDiameter, wallThickness, pipeLength):
    pipeDiameter = ConvertInchToMeters(pipeDiameter)
    wallThickness = ConvertInchToMeters(wallThickness)

    # find volume of just the metal part of the cylinder
    # volume of a cylinder = radius^2 * height * pi
    # volume in units of m^3
    volumeOfOutsidePipe = math.pow((pipeDiameter / 2), 2) * pipeLength * math.pi #m^3
    volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi #m^3
    totalVolume = volumeOfOutsidePipe + volumeOfCircle #m^3

    return (totalVolume) #m^3

def GetAvailableVolume(pipeDiameter, wallThickness, pipeLength):
    # conversion from inches to m
    pipeDiameter = ConvertInchToMeters(pipeDiameter)
    wallThickness = ConvertInchToMeters(wallThickness)

    # find volume of just the metal part of the cylinder
    # volume of a cylinder = radius^2 * height * pi
    # volume in units of m^3
    volumeOfInsidePipe = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * pipeLength * math.pi #m^3
    volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi #m^3

    availableVolume = volumeOfInsidePipe - volumeOfCircle #m^3
    
    return (availableVolume) #m^3

def GetMaterialMass(pipeDiameter, wallThickness, pipeLength, density):
    materialVolume = GetMaterialVolume(pipeDiameter, wallThickness, pipeLength) #m^3

    # mass = density of pipe * volume of pipe
    # mass in units of kg
    mass = density * materialVolume #kg

    return(mass) #kg

def GetMaterialWeight(pipeDiameter, wallThickness, pipeLength, density):
    weight = GetMaterialMass(pipeDiameter, wallThickness, pipeLength, density) * GRAVITY #N

    return weight #N

def PoundsToKg(weight):
    return (weight * 0.453592)

def GetBoyantForceOfPipe(pipeDiameter, wallThickness, pipeLength):
    buoyantForce = GetTotalVolumeOfWaterDisplaced(pipeDiameter, wallThickness, pipeLength) * WATER_DENSITY * GRAVITY #N

    return(buoyantForce) #N