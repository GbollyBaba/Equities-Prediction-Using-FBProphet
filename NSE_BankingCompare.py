import numpy as np

print("PREDICTING NSE  BANKING STOCKS WITH FBPROPHET VANILLA")
print("*****************************************************************")
print("*****************************************************************")
import pandas as pd
import matplotlib.pyplot as plt

my_dpi = 100
fig, axes = plt.subplots(nrows=14, dpi=my_dpi)
fig.set_size_inches(80.5, 140.5, forward=True)
k = 1
data = pd.read_excel('/Users/akingboladeshada/Desktop/NSE/Daily_Equity_Data_updated_001.xlsx')

plt.suptitle( 'DIVIDEND YIELD s of BANKS  01.JAN.2009  to  12.OCT.2021', fontsize=50)

plt.grid()
colors = plt.cm.rainbow(np.linspace(0, 1, 14))
l=0
for x in data.SYMBOL.unique():
    data = pd.read_excel('/Users/akingboladeshada/Desktop/NSE/Daily_Equity_Data_updated_001.xlsx')
    data = data[(data["SYMBOL"] == x)]
    df = pd.DataFrame(data, columns=['TRADE_DATE', 'CLOSE_PRICE'])
    df_111 = pd.DataFrame(data, columns=['TRADE_DATE', 'CLOSE_PRICE',
                                         'DIV', 'DIV_YIELD', 'EPS', 'PE_RATIO','PAYMENT_DATE'])
    start_date = "2015-1-1"
    end_date = "2024-1-31"

    after_start_date = df_111["TRADE_DATE"] >= start_date
    before_end_date = df_111["TRADE_DATE"] <= end_date
    between_two_dates = after_start_date & before_end_date
    df_111 = df_111.loc[between_two_dates]
    axes[l].plot(df_111["TRADE_DATE"], df_111["DIV_YIELD"], color=colors[l], label=x, linewidth=4.0)

    axes[l].grid()
    axes[l].set_xlabel('DATE', fontsize=30)
    l=l+1






plt.show()


fig.savefig('/Users/akingboladeshada/Desktop/NSE/DIVIDENGYIELOFBANKs.png')

print("*****************************************************************")
print("*****************************************************************")

exit(-1)