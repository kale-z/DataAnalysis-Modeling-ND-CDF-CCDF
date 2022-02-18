# Exploratory Data Analysis - Project [ 2 ]
In this project, I have used the information and data (```babyboom.dat```) provided by Prof. Allen Downey. The dataset is about the 44 babies were born on December 18, 1997, in a hospital in Brisbane, Australia[^1]. The time of birth for all 44 babies was reported in the local paper. The complete dataset can be found in [professor's repository](https://github.com/AllenDowney/ThinkStats2/blob/205bc5af51bf3c4872773bd808f58ed970b6cdd6/code/babyboom.dat), or in [this repository](/babyboom.dat). The goal of this project is to explore the given data, understand it and learn how to utilize it for data analysis by applying statistical analysis as it will be explained below.


<br>

## Getting Started
This project is consists of statistical analysis and modeling them with plots and diagrams. To do so, it's important to acquire some certain required and essential library packages to be able to run the project. These packages are:

### Dependencies
- [ThinkStats2 by Prof. Allen B. Downey](https://github.com/AllenDowney/ThinkStats2). <br>
   _Note: The link's repository is downloadable as ThinkStats2 package. You can find also his book as a guideline reference._
- [Matplotlib](https://github.com/matplotlib/matplotlib)
- [NumPy](https://github.com/numpy/numpy)
- [Pandas](https://github.com/pandas-dev/pandas/)
- [SciPy](https://github.com/scipy/scipy)


<br>

## Usage
At the bottom of the Python file, there are the calling commands sorted chronologically regarding each functon respectively, but they are commented. You may run whichever function/method you would like to witness by uncommenting them.

### Part [ 1 ]
In this part, I used the data in the file ```wine.txt``` which is monthly sales of Australian wine by category, in thousands of litres, from January 1980 until July 1995. The categories are fortified white, dry white, sweet white, red, rose, and sparkling ecnoded by ```fortw```, ```dryw```, ```sweetw```, ```red```, ```rose```, ```spark``` respectively. The overall goal is simply to examine sales of Australian wine over 15 years periof from 1980-1995 and distribution of variables in this data.

<br>

#### Methods
- **exponential( )** <br>
This method takes x and 𝛾 (lambda) and finds the CDF for exponential distribution.

- **random( )** <br>
This method randomly creates x and 𝛾 (lambda) for CDF and plot the CDFs of exponential distributions with various parameters. Then, finds the complementary CDF (CCDF) for each x and 𝛾 and plots it.

- **ExpoModelPlot( )** <br>
This method takes two parameters which are the dataset and CDF or CCDF. Then, it models the time for both CDF and CCDF using exponential distribution and plots the result.

- **NormModelPlot( )** <br>
This method models and plots the CDF of time by using normal distributions.

- **scatterplot( )** <br>
This method takes the data and makes a scatter plot of birth weights versus time.


<br>

## Screenshots
Below screeshot samples of PMF and CDF plots examples:


<br>
<p>
   <em>The Model of the CDF by using Exponential Distribution</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/modeledCDF.png" alt>
</p>



<br>

<p>
   <em>Birth Time vs Birth Weight Scatterplot</em>
   <br><br>
   <img style="max-width: 100%;height: 450px;" src="/screenshots/scatterplot.png" alt>
</p>

[^1]: This example is based on information and data from Dunn, “A Simple Dataset for Demonstrating Common Distributions,” Journal of Statistics Education v.7, n.3 (1999).
