import matplotlib.pyplot as plt

from random_walk import randomWalk


rw = randomWalk()
rw.fill_walk()
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Reds,edgecolor='black', s=15)



plt.show()
