import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    ax = plt.gca()
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.set_xlim(1850, 2075)


    # Create first line of best fit
    reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x = np.arange(1880, 2050)
    ax.plot(x, reg.intercept + reg.slope*x, 'r-')


    # Create second line of best fit
    ndf = df.loc[df['Year'] >= 2000]
    reg2 = linregress(ndf['Year'], ndf['CSIRO Adjusted Sea Level'])
    x = np.arange(2000, 2050)
    ax.plot(x, reg2.intercept + reg2.slope*x, 'y-')


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()