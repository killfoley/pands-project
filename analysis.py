#This program shall perform the following actions
#Output a summary of each variable to a single text file
#Save histogram of each variable to png fils
#Outputs a scatter plot of each pair of variables

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris_data_set.csv")

df.describe(include="all").to_csv("summary.csv")