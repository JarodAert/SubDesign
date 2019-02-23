import math
# Density of steel in g/cm3
steelDensity=7.7

# Density of water in g/cm3
densityOfWater=1

pipeDiameter=float(input("Enter Diameter of Pipe (in): "))
wallThickness=float(input("Enter wall thickness (in): "))
pipeLength=float(input("Enter length of tube (m): "))

pipeDiameter=pipeDiameter*2.54*10
wallThickness=wallThickness*2.54*10


crossSectionArea=math.pow(pipeDiameter,2) - math.pow(pipeDiameter-2*wallThickness,2)
volumeOfPipe = crossSectionArea * pipeLength * math.pi/4000

mass = steelDensity * volumeOfPipe
weightOfPipe = mass * 9.8

print(str(mass) + " kg = mass of pipe")
print(str(volumeOfPipe) + " volume of pipe")
print(str(weightOfPipe) + " N = Weight of pipe")

volumeOfWaterDisplaced = math.pow(pipeDiameter,2) * pipeLength * math.pi/4000

Fbuoyant = densityOfWater * 9.8 * volumeOfWaterDisplaced

print(str(Fbuoyant)+" N = Buoyant Force")