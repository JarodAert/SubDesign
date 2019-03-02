import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import MaterialsFuncs

DATA_FILE_PATH="./DataFiles/aluminumPipes.csv"
EXPORT_FILE_PATH="./DataFiles/boyancy.csv"
GRAVITY=9.8
WATER_DENSITY=1000
STEEL_DENSITY=7700
ALUMINUM_DENSITY=2700
PVC_DENSITY=1380

# Read in data
pipesDF=pandas.read_csv(DATA_FILE_PATH)

pipeDiameters=[]
pipePercents=[]
pipeThickness=[]

for index, row in pipesDF.iterrows():
    # Get the data from the file
    pipeD=row['DIAMETER']
    pipeDiameters.append(pipeD)
    wallThickness=row['THICKNESS']
    pipeThickness.append(wallThickness)
    # Since length does not effect boyancy we keep it constant at 0.5, a length that may be good for a test sub
    length=0.5

    # Get the weight of the metal of the pipe as well as the boyant force produced by the water it displaces
    pipeWeight = MaterialsFuncs.GetMaterialWeight(pipeD, wallThickness, length, ALUMINUM_DENSITY)
    boyantForce = MaterialsFuncs.GetBoyantForceOfPipe(pipeD, wallThickness, length)

    # Calculate how much of the tube we will need to fill with water before it will sink
    newtonDifference = boyantForce - pipeWeight
    availableVolume = MaterialsFuncs.GetAvailableVolume(pipeD, wallThickness, length)
    volumeToSinkPipe = newtonDifference / (WATER_DENSITY * 9.8)
    percentToFillPipe = (volumeToSinkPipe / availableVolume) * 100

    # If the total boyant force is less than the weight of the empty pipe then there is no way we could float this pipe
    # We therefore just placehold with 0
    if(percentToFillPipe<0):
        pipePercents.append(0)
    else:
        # Otherwise add the percent to the list
        pipePercents.append(percentToFillPipe)


# Create and export a csv file with all of the data calculated here
exportDF=pandas.DataFrame({'Pipe Diameter': pipeDiameters, 'Wall Thickness': pipeThickness, 'Percent to Fill': pipePercents})
exportDF.to_csv(EXPORT_FILE_PATH, sep=",")

# Plot the data on a 3d scatterplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(pipeDiameters, pipeThickness, pipePercents)
ax.set_xlabel("Pipe Diameter")
ax.set_ylabel("Pipe Thickness")
ax.set_zlabel("Percentage to Fill")
plt.show()
