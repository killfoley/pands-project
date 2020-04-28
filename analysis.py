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

#head() command shows first x number of lines. Specify number in bracket
print(df.head(10))

#Show number of rows and columns
print(df.shape)

#Show the unique varieties of df flower
df["variety"].unique()
print(df.groupby("variety").size())

#Summarise data set and write to .txt and .csv files
summary = df.describe(include="all")
summaryt = summary.transpose()
#summaryt["mean"] = summaryt["mean"].round(4)
#summaryt["std"] = summaryt["std"].round(4)

print(summaryt)

#df.describe(include="all").to_csv("summary.txt", sep=' ')
#df.describe(include="all").to_csv("summary.csv")

summaryt.to_csv("summary.txt", sep=',')

#plot histogram for each variable and save to .png

plt.hist(df["sepal length"], color="skyblue", ec="black")
plt.title("sepal length")
plt.xlabel("length in cm")
plt.ylabel("Frequency")
plt.savefig("sepal_length.png")
plt.clf()

plt.hist(df["sepal width"], color="green", ec="black")
plt.title("sepal width")
plt.xlabel("width in cm")
plt.ylabel("Frequency")
plt.savefig("sepal_width.png")
plt.clf()

plt.hist(df["petal length"], color="orange", ec="black")
plt.title("petal length")
plt.xlabel("length in cm")
plt.ylabel("Frequency")
plt.savefig("petal_length.png")
plt.clf()

plt.hist(df["petal width"], color="purple", ec="black")
plt.title("petal width")
plt.xlabel("width in cm")
plt.ylabel("Frequency")
plt.savefig("petal_width.png")
plt.clf()

#Scatterplot matrix of all variable pairings
g = sns.pairplot(df, hue="variety", markers=["o", "s", "D"])
plt.savefig("scatterplot_matrix.png")

#Scatterplot matrix of all variable pairings with linear regression
g = sns.pairplot(df, hue="variety", kind="reg", markers=["o", "s", "D"])
plt.savefig("scatterplot_matrix_regression.png")

#Violinplot of data
sns.set(style="whitegrid")
plt.figure(figsize=(12,10))
plt.subplot(2,2,1)
sns.violinplot(x="variety", y="sepal length", data=df)
plt.subplot(2,2,2)
sns.violinplot(x="variety", y="sepal width", data=df)
plt.subplot(2,2,3)
sns.violinplot(x="variety", y="petal length", data=df)
plt.subplot(2,2,4)
sns.violinplot(x="variety", y="sepal width", data=df)
plt.savefig("violinplot.png")

#Split the data frame into the 3 distinct varieties
#iris_setosa = df[df["variety"] == "setosa"]
#iris_virginica = df[df["variety"] == "virginica"]
#iris_versicolor = df[df["variety"] == "versicolor"]

#Plotting histogram & probability density function (PDF) using seaborn FacetGrid
sns.FacetGrid(df, hue="variety", height=5) \
   .map(sns.distplot, "sepal length") \
   .add_legend();
plt.savefig("sepal_length_PDF.png")

sns.FacetGrid(df, hue="variety", height=5) \
   .map(sns.distplot, "sepal width") \
   .add_legend();
plt.savefig("sepal_width_PDF.png")

sns.FacetGrid(df, hue="variety", height=5) \
   .map(sns.distplot, "petal length") \
   .add_legend();
plt.savefig("petal_length_PDF.png")

sns.FacetGrid(df, hue="variety", height=5) \
   .map(sns.distplot, "petal width") \
   .add_legend();
plt.savefig("petal_width_PDF.png")