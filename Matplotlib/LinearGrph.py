from matplotlib import pyplot as plt
from matplotlib import style

x = [1, 2, 3]
y = [2, 1, 9]

style.use('ggplot')
plt.plot(x, y, 'g', label='one', linewidth=5)
plt.title('Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.legend()
plt.grid(True, color='c')

plt.show()
