## Importing the needed libraries:

from math import *
import random
import matplotlib.pyplot as plt
import numpy as np

## =========================================================================
## Manipulating with the data:

file = open('babyboom.dat') # Import the data
Elements = [] # Create a list to simplify manipulating on the data
for p in file: # Adding the lines into the list
    Elements.append(p.rstrip("\n")) # Getting rid of the ("\n")
if "START DATA:" in Elements:
    index = Elements.index("START DATA:") # Finding the index of the statement to obtain the data
    Elements = Elements[index+1:] # Getting rid of the text lines and keep the integers
for s in range(len(Elements)): # Getting rid of the lines from the new line: ("\n") and ("\t") and keep the last column
    Elements[s] = Elements[s].rstrip("\n").split()

Data = []
for d in range(len(Elements)): # Taking the needed column from the obtained data
    Data.append(int(Elements[d][3]))
ScatterPlotData = [] # Taking the needed column for scatterplot() method
for e in range(len(Elements)):
    ScatterPlotData.append(int(Elements[e][2]))
Mean = float(sum(Data)) / len(Data) # Computing the Mean
y = 1 / Mean # Computing the lambda

## =========================================================================
## The Code Part:

class Part1():
    # The exponential() method takes the data and the lambda as inputs
    # and output the Cumulative Distribution Function (CDF)
    def exponential(self,x,y):
        CDF = []
        for o in range(len(x)): # Calculating the CDF for every element in the data
            CDF.append(1 - (exp((-y) * x[o])))
        return CDF

    # The random() method creates its own data values, finds its Cumulative Distribution Function (CDF),
    # finds its Complementary Cumulative Distribution Function (CCDF) then plot both of them
    def random(self):
        x = [] # List to contain all the data values
        for i in range(50): # Generating the random values
            x.append(random.uniform(0,50))

        Mean = float(sum(x)) / len(x)
        y = 1 / Mean # Finding the Mean and the lambda of the data

        CDF = [] # List to contain the CDF of the data
        for s in range(len(x)): # Computing the CDF of every values of the data
            CDF.append(1 - (exp((-y) * x[s])))
        # Sorting both of the data and the CDF'ed data even if they are already sorted,
        # just for making sure their arrange won't change through the loops
        CDF.sort(),x.sort()

        ComplementaryCDF = [] # List contain the CCDF of the data
        for m in range(len(CDF)): # Computing the CCDF of every values of the data
            ComplementaryCDF.append(1 - CDF[m])

        # Plotting the Cumulative Distribution Function of the data
        plt.figure(1)
        plt.plot(x,CDF)
        plt.title('Exponential Distribution CDF')
        plt.ylabel('CDF'),plt.xlabel('Time')
        plt.axis((0,50,0,1))

        # Plotting the Complementary Cumulative Distribution Function of the data
        plt.figure(2)
        plt.plot(x,ComplementaryCDF)
        plt.title('Exponential Distribution Complementary CDF')
        plt.ylabel('Complementary CDF'),plt.xlabel('Time')
        plt.axis((0,50,0,1))
        plt.show()

    # The ExpoModelPlot() takes the given data and the Cumulative Distribution Function (CDF)
    # of the data as an inputs, computes the Complementary Cumulative Distribution Function (CCDF)
    # of the data, Models both of the CDF and CCDF using Exponential Distribution
    # then finally plots both of the Models
    def ExpoModelPlot(self, Data, CDF):
        ComplementaryCDF = [] # List conatin all the CCDF of the data
        for m in range(len(CDF)): # Computing the CCDF of every values of the data
            ComplementaryCDF.append(1 - CDF[m])

        ModelCDF = [] # List contain all the modeled CDF values
        for z in range(len(CDF)): # Modeling the CDF of every value
            ModelCDF.append(log10(CDF[z]))

        ModelComplementaryCDF = [] # List contain all the modeled CCDF values
        for t in range(len(ComplementaryCDF)): # Modeling the CCDF of every value
            ModelComplementaryCDF.append(log10(ComplementaryCDF[t]))

        # Plotting the Modeled Cumulative Distribution Function of the data
        plt.figure(1)
        plt.plot(Data,ModelCDF)
        plt.title('The Model of the CDF by using Exponential Distribution')
        plt.ylabel('The Modeled CDF'),plt.xlabel('Time')

        # Plotting the Modeled Complementary Cumulative Distribution Function of the data
        plt.figure(2)
        plt.plot(Data,ModelComplementaryCDF)
        plt.title('The Model of the Comlementary CDF by using Exponential Distribution')
        plt.ylabel('The Modeled Complementary CDF'),plt.xlabel('Time')
        plt.show()

    # The NormModelPlot() method takes the given data and its Cumulative Distribution Function (CDF)
    # as inputs, models the data using Normal Distribution then plots the Model
    def NormModelPlot(self, Data, CDF):
        Mean = float(sum(Data)) / len(Data)
        y = 1 / Mean # Computing the Mean and Lambda

        Standard = [] # List to contain the data to use it to find the Standard Deviation
        for j in range(len(Data)): # Applying the Z equation from the Standard Deviation formula on each value
            Standard.append((Data[j] - Mean)**2)
        StandardDeviation = sqrt(float(sum(Standard)) / len(Data)) # Finding the Standard Deviation

        NormalDistribution = [] # List to contain the Modeled values
        for i in range(len(Data)): # Finding Normal Distribution of every element
            NormalDistribution.append((1 / (StandardDeviation * sqrt(2 * pi))) * exp(( - (Data[i] - Mean) ** 2) / (2 * ((StandardDeviation) ** 2))))

        # Plotting the Modeled Normal Distribution of the data
        plt.plot(CDF, NormalDistribution)
        plt.title('The Model of the CDF by using Normal Distribution')
        plt.ylabel('The Modeled CDF'),plt.xlabel('CDF')
        plt.show()

    # The scatterplot() method takes the data, which is Birth time of the born babies in minutes,
    # and the Weight of the born babies in Grams. Then, plots both of the taken data in Scatter Graph
    def scatterplot(self, Data1, Data2):
        # Plotting the data: Birth time of born babies VS Weight of born babies
        colors = np.random.rand(len(Data)) # Just an extra addition for Design
        plt.scatter(Data1, Data2, s=40, c=colors, alpha=0.8)
        plt.title('Birth Time Vs Birth Weight')
        plt.ylabel('Birth Weight in Grams'),plt.xlabel('Birth Time in Minutes')
        plt.show()


## =========================================================================
## The Calling or Running Code Part:
## To Call any needed methord or function just erase the hashtag from it

part = Part1()
print(part.exponential(Data,y))
part.random()
part.ExpoModelPlot(Data , part.exponential(Data,y))
part.NormModelPlot(Data, part.exponential(Data,y))
part.scatterplot(Data, ScatterPlotData)

