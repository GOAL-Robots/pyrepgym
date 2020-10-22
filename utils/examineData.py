import numpy as np
import matplotlib.pyplot as plt

allData = np.loadtxt('mergedData')

filteredData = allData[(allData[:,2+7] > 0.15) & 
                       (allData[:,2+7] < 0.45) &
                       (allData[:,0+7] > -1.25) &
                       (allData[:,0+7] < -0.55) &
                       (allData[:,1+7] > -0.75) &
                       (allData[:,1+7] < 0.75), :]

filteredData = filteredData[filteredData[:,3] < 0, :]

diff1 = (np.linalg.norm(filteredData[:,-4:]-np.array([0.7,0.7,0,0]), axis=1) < 0.03)
diff2 = (np.linalg.norm(filteredData[:,-4:]+np.array([0.7,0.7,0,0]), axis=1) < 0.03)
filteredData = filteredData[diff1 | diff2, :]

print(filteredData)
plt.plot(filteredData[:, -4:], 'x')
plt.legend(['a','b','c','d'])
#plt.show()

np.savetxt('data_filtered', filteredData)
print(filteredData.shape)

