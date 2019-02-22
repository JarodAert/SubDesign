import math
# Density of steel in g/cm3
steelDensity=7.7

pipeDiameter=float(input("Enter Diameter of Pipe (in): "))
wallThickness=float(input("Enter wall thickness (in): "))
pipeLength=float(input("Enter length of tube (m): "))

pipeDiameter=pipeDiameter*2.54*10
pipeRadius=pipeDiameter/2
wallThickness=wallThickness*2.54*10
#pipeLength=pipeLength*2.54

print("Pipe Diameter (cm): "+str(pipeDiameter))
print("Wall Thickness (cm): "+str(wallThickness))
print("Pipe Length: "+str(pipeLength))

crossSectionArea=math.pow(pipeDiameter,2) - math.pow(pipeDiameter-2*wallThickness,2)

mass=steelDensity * crossSectionArea * pipeLength * math.pi/4000

print(str(mass)+" Kilograms")