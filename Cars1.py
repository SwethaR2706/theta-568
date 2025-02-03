import statsmodels.formula.api as smf
model = smf.ols('MPG ~ WT + VOL + SP + HP', data=df).fit()
model.params
print(model.tvalues,'\n',model.pvalues)
(model.rsquared,model.rsquared_adj)