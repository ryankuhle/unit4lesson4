import pandas as pd
import matplotlib.pylab as plt

COLS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv('iris.csv', names=COLS)

#Create scatterplot of sepal_length by sepal_width colored by class
color_dict = {'Iris-setosa':'red',
              'Iris-versicolor':'blue',
              'Iris-virginica':'green'}
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Classification by Sepal')
plt.scatter(iris_data['sepal_length'], iris_data['sepal_width'], color=[ color_dict[i] for i in iris_data['class']])
plt.grid()
p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-setosa'])
p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-versicolor'])
p3 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-virginica'])
plt.legend((p1, p2, p3), ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'), loc='best')
plt.show()


'''
Pick a new point, programmatically at random.

Sort each point by its distance from the new point, and subset the 10 nearest points.

Determine the majority class of the subset.

See if you can write a function called knn() that will take k as an argument and return the majority class for different values of k. (I think k is supposed to be distance)
'''
