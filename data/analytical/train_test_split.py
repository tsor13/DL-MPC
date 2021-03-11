import numpy as np
import matplotlib.pyplot as plt

numFiles = 6
splitLocation = 250000

for i in range(1,7):
    source = "x{}.csv".format(i)
    trainTarget = "x{}.csv".format(i)
    testTarget = "x{}.csv".format(i+numFiles)

    data = np.loadtxt(source, delimiter=',')

    trainData = data[:, :splitLocation]
    testData = data[:, splitLocation:]

    np.savetxt(trainTarget, trainData, delimiter=',')
    np.savetxt(testTarget, testData, delimiter=',')

    source = "p{}.csv".format(i)
    trainTarget = "p{}.csv".format(i)
    testTarget = "p{}.csv".format(i+numFiles)

    data = np.loadtxt(source, delimiter=',')

    trainData = data[:, :splitLocation]
    testData = data[:, splitLocation:]

    np.savetxt(trainTarget, trainData, delimiter=',')
    np.savetxt(testTarget, testData, delimiter=',')
    
