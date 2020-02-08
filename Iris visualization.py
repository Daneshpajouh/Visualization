%reset
import numpy as np
import matplotlib.pyplot as plt
from urllib.request import urlopen

dataset = np.loadtxt((urlopen('https://raw.githubusercontent.com/Daneshpajouh/Logistic-Regression/master/iris.data')), dtype='str', delimiter = ',')

# Defining a figure function
def figure(dataset):
    n = int(((len(dataset.transpose()) - 1)*(len(dataset.transpose()) - 2))/2)
    s = n-2
    l = 0
    y = np.array(dataset[:,-1])
    y_color = []
    for i in range(0,50):
        y_color.append("r")
    for i in range(50,100):
        y_color.append("g")
    for i in range(100,150):
        y_color.append("b")
    for i in range(n-3):
        s -= 1
        l += 1
        for j in range(s):
            x1 = np.array(dataset[:,i])
            x2 = np.array(dataset[:,l+j])
            plt.scatter(x1, x2, marker="x", c=y_color)
            plt.title(("Dataset X"+ str(i+1)+" and X"+ str(l+j+1)), fontsize=16)
            plt.xlabel(("X"+ str(i+1)), fontsize=14)
            plt.ylabel(("X"+ str(l+j+1)), fontsize=14)
            plt.axis([-2, 50, -2, 50])
            plt.show()
            
# Run the function
figure(dataset)
