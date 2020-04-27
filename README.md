# Programming and Scripting - Project 2020
# Iris Flower Data Set - A Summary - Author: Killian Foley

## Introduction
The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper *The use of multiple measurements in taxonomic problems*. It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”. [1](https://en.wikipedia.org/wiki/Iris_flower_data_set)

## The Data Set
The data set consists of 50 samples from each of three species of Iris Flower (Iris Setosa, Iris Virginica and Iris Versicolor). Four features were measured from each sample: sepal length, sepal width, petal length and petal width, in centimetres. The data set was downloaded from the following link [Iris dataset.csv](https://tableconvert.com/?output=csv)

## Running the Python Program
The python program is entitled *analysis.py*. To run the code one must navigate to the directory containing the program via the command line and execute the command *python analysis.py* on the command line (terminal). The output of the code is explained in detail below.

## Explaining The Code
### Python Libraries Used
`import pandas as pd`  
`import matplotlib.pyplot as plt`  
`import numpy as np`  
`import seaborn as sns`  

The **pandas** library is used to perform several useful functions in this project. It reads in the initial data from a .csv file, saves it as a *dataframe*, creates a summary of the data and writes that summary to a text file.  
  
**matplotlib.pyplot** is used to plot a histogram for each variable.  
  
**seaborn** is used to plot the scatterplot matrix x 2 and violinplots

### Data Import
The data is read in using function from pandas and first 10 lines are displayed.  

`df = pd.read_csv("iris_data_set.csv")`  
`df.columns = ["sepal length", "sepal width", "petal length", "petal width", "variety"]`

`#head() command shows first x number of lines. Specify number in bracket`  
`print(df.head(10))`  
  
|   | sepal length  | sepal width  | petal length  | petal width |variety|
|---|:-------------:|:------------:|:-------------:|:-----------:|:-----:|
| 0           | 5.1          |3.5          | 1.4          |0.2  |Setosa|  
| 1           | 4.9          |3.0          | 1.4          |0.2  |Setosa|  
| 2           | 4.7          |3.2          | 1.3         | 0.2  |Setosa|  
| 3           | 4.6          |3.1          | 1.5         | 0.2  |Setosa|  
| 4           | 5.0          |3.6          | 1.4         | 0.2  |Setosa|  
| 5           | 5.4          |3.9          | 1.7         | 0.4  |Setosa|  
| 6           | 4.6          |3.4          | 1.4         | 0.3  |Setosa|  
| 7           | 5.0          |3.4          | 1.5         | 0.2  |Setosa|  
| 8           | 4.4          |2.9          | 1.4         | 0.2  |Setosa|  
| 9           | 4.9          |3.1          | 1.5         | 0.1  |Setosa|  

### Information about the Data Set
Display the number of rows and columns.  
  
`print(df.shape)`  
  
Output: (150, 5)
  
### Display the Unique Flower Varieties
`df["variety"].unique()`  
`print(df.groupby("variety").size())`

Output:  
Setosa  50
Versicolor: 50
Virginica:  50
dtype:  int64

### Create a Summary of Each Variable and Write to a Single Text File
`summary = df.describe()`  
`summaryt = summary.transpose()`  
`summaryt["mean"] = summaryt["mean"].round(4)`  
`summaryt["std"] = summaryt["std"].round(4)`  
