import math
import csv
import matplotlib.pyplot as plt

# Density of steel in kg/m^3
steelDensity = 7700
# Density of water in kg/m^3
densityOfWater = 1000

pipeDiameters = []
pipePercentages = []

with open('../DataFiles/pipes-old.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count < 2:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            pipeDiameter = float(row[0])
            wallThickness = float(row[1])
            pipeLength = float(row[2])
            line_count += 1
            # pipeDiameter = float(input("Enter Diameter of Pipe (in): "))
            # wallThickness = float(input("Enter wall thickness (in): "))
            # pipeLength = float(input("Enter length of tube (m): "))

            print(str(pipeDiameter) + " inches")
            pipeDiameters.append(pipeDiameter)

            # conversion from inches to m
            pipeDiameter = (pipeDiameter * 2.54) / 100
            wallThickness = (wallThickness * 2.54) / 100

            # find volume of just the metal part of the cylinder
            # volume of a cylinder = radius^2 * height * pi
            # volume in units of m^3
            volumeOfOutsidePipe = math.pow((pipeDiameter / 2), 2) * pipeLength * math.pi
            volumeOfInsidePipe = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * pipeLength * math.pi
            volumeOfJustPipe = volumeOfOutsidePipe - volumeOfInsidePipe
            # print(str(volumeOfOutsidePipe) + " m^3 = volume of outside pipe")
            # print(str(volumeOfInsidePipe) + " m^3 = volume of inside pipe")
            # print(str(volumeOfJustPipe) + " m^3 = volume of just pipe")

            # add volume of circle to close one end of the pipe
            # uses wallThickness as height
            volumeOfCircle = math.pow(((pipeDiameter - (wallThickness * 2)) / 2), 2) * wallThickness * math.pi
            totalVolume = volumeOfJustPipe + volumeOfCircle

            # mass = density of pipe * volume of pipe
            # mass in units of grams
            mass = steelDensity * volumeOfJustPipe
            totalMass = steelDensity * totalVolume

            # volume of water displaced is total volume enclosed by the pipe
            volumeOfWaterDisplaced = volumeOfOutsidePipe
            totalVolumeOfWaterDisplaced = volumeOfOutsidePipe + volumeOfCircle

            # print(str(mass) + " kg = mass of pipe")
            # print(str(volumeOfWaterDisplaced) + " m^3 = volume of water displaced")

            Fbuoyant = densityOfWater * 9.8 * volumeOfWaterDisplaced
            totalFbuoyant = densityOfWater * 9.8 * totalVolumeOfWaterDisplaced
            weightOfPipe = mass * 9.8
            totalWeightOfPipe = totalMass * 9.8

            # print(str(weightOfPipe) + " N = Weight of pipe")
            # print(str(Fbuoyant) + " N = Buoyant Force")

            if totalWeightOfPipe > totalFbuoyant:
                print("The pipe will sink.\n")
                pipePercentages.append(0)
                print(str(totalWeightOfPipe) + " total weight")
                print(str(totalFbuoyant) + " total Fbuoyant")
            else:
                print("The pipe will float.")
                newtonDifference = totalFbuoyant - totalWeightOfPipe
                availableVolume = volumeOfInsidePipe - volumeOfCircle
                volumeToSinkPipe = newtonDifference / (densityOfWater * 9.8)
                # print(str(availableVolume) + " M^3 = available")
                # print(str(volumeToSinkPipe) + " M^3 = to sink")

                # calculate how much volume should be filled with water to sink
                percentToFillPipe = (volumeToSinkPipe / availableVolume) * 100
                print(str(percentToFillPipe) + " % = percent of pipe to fill with water to sink\n")
                pipePercentages.append(percentToFillPipe)

plt.plot(pipeDiameters, pipePercentages)
plt.xlabel('diameter (inches)')
plt.ylabel('% of pipe to fill to sink')
plt.show()

