import math
# Density of steel in g/cm3
steelDensity=7.7

pipeDiameter=float(input("Enter Diameter of Pipe (in): "))
wallThickness=float(input("Enter wall thickness (in): "))
pipeLength=float(input("Enter length of tube (cm): "))

pipeDiameter=pipeDiameter*2.54
pipeRadius=pipeDiameter/2
wallThickness=wallThickness*2.54
#pipeLength=pipeLength*2.54

print("Pipe Diameter (cm): "+str(pipeDiameter))
print("Wall Thickness (cm): "+str(wallThickness))
print("Pipe Length: "+str(pipeLength))

areaOfOutterR=(math.pow(pipeRadius,2)*math.pi)
areaOfInnerR=(math.pow(pipeRadius-2*wallThickness,2)*math.pi)
steelArea=areaOfOutterR-areaOfInnerR
steelVolume=steelArea*pipeLength
steelMass=steelVolume*steelDensity

print(str(steelMass/1000)+" Kilograms")