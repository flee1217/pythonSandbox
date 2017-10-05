import matplotlib.pyplot as plt
import numpy as np

np.random.seed(4)
bord = 100
botNum = 20
sampleNum = 10000
distanceOption = 4  # 1 = euclidean, 2 = taxicab, 3 = chebyshev, 4 = akritean, 5 = minkowski where p is -inf
mult = bord * .08  # length of pointing arrows
akriteanHeuristic = .5  # heurstic value between 0 and 1


fig, ax = plt.subplots()
fig.set_size_inches(6, 6)
plt.xlim(-1.1 * bord, 1.1 * bord)
plt.ylim(-1.1 * bord, 1.1 * bord)

botX, botY = 2 * bord * np.array([np.random.rand(botNum), np.random.rand(botNum)]) - np.ones(botNum) * bord

ptX, ptY = 2 * bord * np.array([np.random.rand(sampleNum), np.random.rand(sampleNum)]) - np.ones(sampleNum) * bord
plt.plot(botX, botY, 'ro')


# gets distance from i-th sample to j-th bot using num-th distance metric
def distance(i, j, k):
	if k == 1:  # euclidean
		return np.sqrt((ptX[i] - botX[j]) ** 2 + (ptY[i] - botY[j]) ** 2)
	elif k == 2:  # taxicab
		return np.abs(ptX[i] - botX[j]) + np.abs(ptY[i] - botY[j])
	elif k == 3:  # chebyshev
		return np.abs(ptX[i] - botX[j]) if np.abs(ptX[i] - botX[j]) > np.abs(ptY[i] - botY[j]) else np.abs(ptY[i] - botY[j])
	elif k == 4:  # akritean
		return distance(i, j, 1) * (1 - akriteanHeuristic) + distance(i, j, 2) * akriteanHeuristic
	elif k == 5:  # minkowski where p = negative infinity
		return np.abs(ptX[i] - botX[j]) if np.abs(ptX[i] - botX[j]) < np.abs(ptY[i] - botY[j]) else np.abs(ptY[i] - botY[j])
	else:
		return 0


# gets the closest bot coordinates for the i-th sample
def closestPoint(i, k):
	closestIndex = 0
	for j in range(1, botNum):
		if distance(i, j, k) < distance(i, closestIndex, k):
			closestIndex = j
	return closestIndex

def plotpoints():
	for i in range(0, sampleNum):
		j = closestPoint(i, distanceOption)
		endX, endY = ((botX[j] - ptX[i]) * mult / (distance(i,j,distanceOption)), (botY[j] - ptY[i]) *
									mult / (distance(i,j,distanceOption) ) )
		plt.arrow(ptX[i], ptY[i], endX, endY, length_includes_head=True, head_width=.5, alpha=.5, color='c')

plotpoints()

plt.show()
