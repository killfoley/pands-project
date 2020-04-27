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

The **pandas** library is used to perform several useful functions in this project. It reads the .csv file, saves it as a dataframe, creates a summary of the data and writes that summary to a text file.  
`df = pd.read_csv()`  
`df.describe()`  
`df.to_csv()`  
  
**matplotlib.pyplot** is used to plot a histogram for each variable.  
  
**seaborn** is used to plot the scatterplot matrix

