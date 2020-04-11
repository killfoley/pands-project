#This program shall perform the following actions
#Output a summary of each variable to a single text file
#Save histogram of each variable to png files
#Outputs a scatter plot of each pair of variables

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("iris_data_set.csv")

#df.describe(include="all").to_csv("summary.txt", sep=' ')

plt.hist(df["sepal length"], color="skyblue")
plt.title("sepal length")
plt.xlabel("length in cm")
plt.ylabel("Number of flowers")
plt.savefig("sepal length.png")
plt.clf()

plt.hist(df["sepal width"], color="green")
plt.title("sepal width")
plt.xlabel("width in cm")
plt.ylabel("Number of flowers")
plt.savefig("sepal width.png")
plt.clf()

plt.hist(df["petal length"], color="orange")
plt.title("petal length")
plt.xlabel("length in cm")
plt.ylabel("Number of flowers")
plt.savefig("petal length.png")
plt.clf()

plt.hist(df["petal width"], color="purple")
plt.title("petal width")
plt.xlabel("width in cm")
plt.ylabel("Number of flowers")
plt.savefig("petal width.png")
plt.clf()


