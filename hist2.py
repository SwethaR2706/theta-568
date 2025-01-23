import matplotlib.pyplot as plt
#sample data: a small set of values
data=[5,7,7,8,9,10,10,10,11,12,11,11]
#Create histogram
plt.hist(data,bins=10,edgecolor='black')
#set title and labels for plot
plt.title('Simple Histogram Example')
plt.xlabel('Numbers')
plt.ylabel('Count')
#show the plot
plt.show()