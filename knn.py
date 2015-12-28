import pandas as pd

COLS = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv('iris.csv', names=COLS)



'''
Create a scatterplot of sepal length by width in the Iris dataset. Sepals are a type of leaf around the petals of a flower.

Pick a new point, programmatically at random.

Sort each point by its distance from the new point, and subset the 10 nearest points.

Determine the majority class of the subset.

See if you can write a function called knn() that will take k as an argument and return the majority class for different values of k. (I think k is supposed to be distance)
'''
