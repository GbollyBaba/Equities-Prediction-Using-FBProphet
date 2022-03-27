import numpy
import numpy as np
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print("Relationsip with NSE  BANKING STOCKS ")
print("***********************")
print("***********************")
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20})
k = 1
dfAll=[]
dfAllTemp=[]
cols= []
data = pd.read_excel('/Users/akingboladeshada/Desktop/NSE/Daily_Equity_Data_updated_001.xlsx')
for x in data.SYMBOL.unique():
    data = pd.read_excel('/Users/akingboladeshada/Desktop/NSE/Daily_Equity_Data_updated_001.xlsx',index_col='TRADE_DATE')
    data = data[(data["SYMBOL"] == x)]

    df = pd.DataFrame(data, columns=['TRADE_DATE', 'CLOSE_PRICE'])

    df.columns = ['TRADE_DATE', x]
    print(str(k) +  ". " + x)
    k= k+1

    dfAll.append(df)
    if (x!='TRADE_DATE'):
        cols.append(x)



result = pd.concat(dfAll, axis=1, join="inner")
print(result[cols].describe())
sns.pairplot(result[cols], size=2.0)

df =result[cols]
#Calculation and visualization of the covariance matrix
from sklearn.preprocessing import StandardScaler
stdsc = StandardScaler()
X_std = stdsc.fit_transform(df[cols].iloc[:,range(0,13)].values)
cov_mat =np.cov(X_std.T)
plt.figure(figsize=(10,10))
sns.set(font_scale=1.5)
hm = sns.heatmap(cov_mat,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 12},
                 cmap='coolwarm',
                 yticklabels=cols,
                 xticklabels=cols)
plt.title('Covariance matrix showing correlation coefficients', size = 18)

plt.tight_layout()
plt.show()

result.to_csv('/Users/akingboladeshada/Desktop/AI_CLASS/NSE_Stocks.csv')

exit(-1)



