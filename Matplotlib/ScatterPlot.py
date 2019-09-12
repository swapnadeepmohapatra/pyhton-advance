from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 9, 5, 4, 6]

plt.xlabel('entry a')
plt.ylabel('entry b')

plt.scatter(x, y)
plt.show()
