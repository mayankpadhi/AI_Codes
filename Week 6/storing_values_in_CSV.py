import numpy as np
import matplotlib.pyplot as plt
import csv
list=[]

mean =[0,0]
cov=[[1 ,0.7 ],[0.7, 1]]
x, y = np.random.multivariate_normal(mean, cov,40).T
list=[]
print(x,y)
for i in range(0,40):
    list.append([x[i],y[i]])

print(list)


mean =[4,4]
cov=[[1 ,0.25 ],[0.25, 0.5]]
x1, y1 = np.random.multivariate_normal(mean, cov,30).T
print(x1,y1)
for i in range(0,30):
    list.append([x1[i],y1[i]])

print(list)



mean =[0,3]
cov=[[0.5 ,0.1],[ 1, 0.1]]
x2, y2 = np.random.multivariate_normal(mean, cov,20).T
print(x2,y2)
for i in range(0,20):
    list.append([x2[i],y2[i]])

print(list)



mean =[4,0]
cov=[[0.25 ,0],[0, 0.35]]
x3, y3 = np.random.multivariate_normal(mean, cov,10).T
print(x1,y1)
for i in range(0,10):
    list.append([x3[i],y3[i]])

print(list)


with open('names.csv', 'w') as csvfile:
    fieldnames = ['x', 'y']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range (0,100):

        writer.writerow({'x': list[i][0] ,'y': list[i][1]})