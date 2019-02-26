import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import MaterialsFuncs

DATA_FILE_PATH="../DataFiles/aluminumPipes.csv"
GRAVITY=9.8
WATER_DENSITY=1000
STEEL_DENSITY=7700
ALUMINUM_DENSITY=2700

pipesDF=pandas.read_csv(DATA_FILE_PATH)

pipeDiameters=[]
pipePercents=[]
pipeThickness=[]

for index, row in pipesDF.iterrows():
    pipeD=row['DIAMETER']
    pipeDiameters.append(pipeD)
    wallThickness=row['THICKNESS']
    pipeThickness.append(wallThickness)
    length=0.5

    print(str(pipeD) + " pipe diameter")
    print(str(wallThickness) + " pipe thickness")

    pipeWeight = MaterialsFuncs.GetMaterialWeight(pipeD, wallThickness, length, ALUMINUM_DENSITY)
    boyantForce = MaterialsFuncs.GetBoyantForceOfPipe(pipeD, wallThickness, length)

    newtonDifference = boyantForce - pipeWeight
    availableVolume = MaterialsFuncs.GetAvailableVolume(pipeD, wallThickness, length)
    volumeToSinkPipe = newtonDifference / (WATER_DENSITY * 9.8)

    percentToFillPipe = (volumeToSinkPipe / availableVolume) * 100
    print(str(percentToFillPipe) + " % to fill")

    if(percentToFillPipe<0):
        pipePercents.append(0)
    else:
        pipePercents.append(percentToFillPipe)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(pipeDiameters, pipeThickness, pipePercents)
ax.set_xlabel("Pipe Diameter")
ax.set_ylabel("Pipe Thickness")
ax.set_zlabel("Percentage to Fill")
plt.show()
