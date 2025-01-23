import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
data=np.random.randint(20,81,1000)
plt.hist(data,bins=15,edgecolor='black',color='skyblue')
plt.title('Histogram of cancer patients age distribution')
plt.xlabel('Age')
plt.ylabel('No. of patients')
plt.show()