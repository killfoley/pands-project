#This program shall perform the following actions
#Output a summary of each variable to a single text file
#Save histogram of each variable to png files
#Outputs a scatter plot of each pair of variables

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#Read in file
df = pd.read_csv("iris_data_set.csv")

df.columns = ["sepal length", "sepal width", "petal length", "petal width", "variety"]

#Summarise data set and write to .txt and .csv files
summary = df.describe()
summaryt = summary.transpose()

#df.describe(include="all").to_csv("summary.txt", sep=' ')
#df.describe(include="all").to_csv("summary.csv")

summaryt.to_csv("summary.txt", sep=',')

#plot histogram for each variable and save to .png

plt.hist(df["sepal length"], color="skyblue")
plt.title("sepal length")
plt.xlabel("length in cm")
plt.ylabel("Number of flowers")
plt.savefig("sepal_length.png")
plt.clf()

plt.hist(df["sepal width"], color="green")
plt.title("sepal width")
plt.xlabel("width in cm")
plt.ylabel("Number of flowers")
plt.savefig("sepal_width.png")
plt.clf()

plt.hist(df["petal length"], color="orange")
plt.title("petal length")
plt.xlabel("length in cm")
plt.ylabel("Number of flowers")
plt.savefig("petal_length.png")
plt.clf()

plt.hist(df["petal width"], color="purple")
plt.title("petal width")
plt.xlabel("width in cm")
plt.ylabel("Number of flowers")
plt.savefig("petal_width.png")
plt.clf()

#Scatterplot matrix of all variable pairings
g = sns.pairplot(df, hue="variety", markers=["o", "s", "D"])
plt.savefig("scatterplot_matrix.png")

#Scatterplot matrix of all variable pairings with linear regression
g = sns.pairplot(df, kind="reg")
plt.savefig("scatterplot_matrix_regression.png")


