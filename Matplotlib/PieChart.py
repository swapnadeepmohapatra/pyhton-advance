from matplotlib import pyplot as plt

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['m', 'c', 'r', 'b']

plt.pie(slices, labels=activities, colors=colors, startangle=90,
        shadow=True, explode=(0, 0.1, 0, 0), autopct='%1.1f%%')

plt.show()
