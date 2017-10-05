import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(0, 1))
ln, = ax.plot([], [], lw=2)

import math as m

print m.sin(m.pi / 3.0)
print np.sin(m.pi / 3.0)
print (m.sin(m.pi / 3.0) - m.sin(m.pi / 3.0)) * 100000000000
