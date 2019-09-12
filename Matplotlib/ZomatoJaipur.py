from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x, y = np.loadtxt(
    'C:\\Users\\Home PC\\Downloads\\Compressed\\zomato-jaipur-dataset\\zomato_jaipur.csv')

plt.title('CSV')

plt.show()
