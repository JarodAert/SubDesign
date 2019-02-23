import pandas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import MaterialsFuncs

GRAVITY=9.8
WATER_DENSITY=1000
STEEL_DENSITY=7700
ALUMINUM_DENSITY=2700

pipesDF=pandas.read_csv("./DataFiles/aluminumPipes.csv")


pipeDiameters=[]
pipePercents=[]
pipeThickness=[]

for index, row in pipesDF.iterrows():
    pipeD=row['DIAMETER']
    pipeDiameters.append(pipeD)
    wallThickness=row['THICKNESS']
    pipeThickness.append(wallThickness)
    length=0.5

    pipeWeight=MaterialsFuncs.GetMaterialWeight(pipeD, wallThickness, length, ALUMINUM_DENSITY)
    boyantForce=MaterialsFuncs.GetBoyantForceOfPipe(pipeD, length)

    newtonDifference = boyantForce - pipeWeight
    availableVolume = MaterialsFuncs.GetTotalVolumeOfPipe(MaterialsFuncs.ConvertInchToMeters(pipeD), length)
    volumeToSinkPipe = newtonDifference / (WATER_DENSITY * 9.8)

    percentToFillPipe = (volumeToSinkPipe / availableVolume) * 100

    if(percentToFillPipe<0):
        pipePercents.append(0)
    else:
        pipePercents.append(percentToFillPipe)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(pipeDiameters, pipeThickness, pipePercents)
plt.show()
