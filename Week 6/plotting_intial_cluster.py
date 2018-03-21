import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib.colors as colors
col = iter(colors.cnames.values())
list=[]

mean =[0,0]
cov=[[1 ,0.7 ],[0.7, 1]]
x, y = np.random.multivariate_normal(mean, cov,40).T
plt.scatter(x, y, color=next(col))

mean =[4,4]
cov=[[1 ,0.25 ],[0.25, 0.5]]
x1, y1 = np.random.multivariate_normal(mean, cov,30).T
plt.scatter(x1, y1, color=next(col))


mean =[0,3]
cov=[[0.5 ,0.1],[ 1, 0.1]]
x2, y2 = np.random.multivariate_normal(mean, cov,20).T
plt.scatter(x2, y2, color=next(col))


mean =[4,0]
cov=[[0.25 ,0],[0, 0.35]]
x3, y3 = np.random.multivariate_normal(mean, cov,10).T
plt.scatter(x3, y3, color=next(col))
plt.show()

