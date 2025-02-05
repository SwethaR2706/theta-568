(np.argmax(c),np.max(c))
from statsmodels.graphics.regressionplots import influence_plot
influence_plot(model)
plt.show()
k=df.shape[1]
n=df.shape[0]
leverage_cutoff=3*((k+1)/n)
df[df.index.isin([70,76])]
df.head()