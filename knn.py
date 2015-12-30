import pandas as pd
import matplotlib.pylab as plt
import random
import math


COLS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'iris_class', 'distance']
iris_data = pd.read_csv('iris.csv', names=COLS)
del iris_data['petal_length']
del iris_data['petal_width']

# Create scatterplot of sepal_length by sepal_width colored by class
color_dict = {'Iris-setosa':'red',
              'Iris-versicolor':'blue',
              'Iris-virginica':'green'}
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Classification by Sepal')
plt.scatter(iris_data['sepal_length'], iris_data['sepal_width'], color=[ color_dict[i] for i in iris_data['iris_class']])
plt.grid()
p1 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-setosa'])
p2 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-versicolor'])
p3 = plt.Rectangle((0, 0), 0.1, 0.1, fc=color_dict['Iris-virginica'])
plt.legend((p1, p2, p3), ('Iris-setosa', 'Iris-versicolor', 'Iris-virginica'), loc='best')
#plt.show()

# Random point for plotting
random_x = random.uniform(4.0, 8.5)
random_y = random.uniform(1.5, 5.0)

# measures the distance from random point against all points in data frame
# records info in data frame column "distance"
for i in iris_data.index:
    train_x = iris_data['sepal_length'][i]
    train_y = iris_data['sepal_width'][i]
    a = (train_x - random_x) ** 2 # a squared
    b = (train_y - random_y) ** 2 # b squnared
    c = math.sqrt(a + b) # c sqrd
    iris_data.set_value(i, 'distance', c)

iris_data = iris_data.sort(['distance'], ascending=True)

def knn(k):
    subset = iris_data[0:k]
    subset = subset.iris_class.value_counts().sort_index()
    print subset
    #return subset

k = 25
knn(k)
# majority_class = knn(k)


#print "Your point with coordinates: %s, %s likely belongs to the class: %s, based on %s known neighbors." % (random_x, random_y, majority_class, k)
