from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# x1 = [1, 2, 3, 4, 5]
# y1 = [10, 20, 30, 11, 39, 12, 36, 43, 15, 40]
# plt.hist(y1, x1, histtype='bar', rwidth=0.8)
# # plt.hist(x2, y2, label='Two', color='k')

# plt.legend()
# plt.title('Bar Graph')
# plt.xlabel('X Axis')
# plt.ylabel('Y Axis')

# plt.show()


x = np.random.randn(10000)

# the histogram of the data
plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.grid(True)
plt.show()
