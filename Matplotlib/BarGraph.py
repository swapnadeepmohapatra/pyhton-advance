from matplotlib import pyplot as plt
from matplotlib import style

x = [1, 2, 3]
y = [1, 2, 3]
x2 = [4, 5, 6]
y2 = [2, 2, 8]

plt.bar(x, y, label='One', color='c')
plt.bar(x2, y2, label='Two', color='k')

plt.legend()
plt.title('Bar Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
