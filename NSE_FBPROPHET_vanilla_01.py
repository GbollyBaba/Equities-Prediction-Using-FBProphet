import numpy as np




print("PREDICTING NSE  BANKING STOCKS WITH FBPROPHET VANILLA")
print("*****************************************************************")
print("*****************************************************************")
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 20})
k = 1
data = pd.read_excel('Daily_Equity_Data_updated_002.xlsx')
for x in data.SYMBOL.unique():
    data = pd.read_excel('Daily_Equity_Data_updated_002.xlsx')
    data = data[(data["SYMBOL"] == x)]
    df = pd.DataFrame(data, columns=['TRADE_DATE', 'CLOSE_PRICE'])
    df_111 = pd.DataFrame(data, columns=['TRADE_DATE', 'CLOSE_PRICE',
                                         'DIV', 'DIV_YIELD', 'EPS', 'PE_RATIO','PAYMENT_DATE'])
    # conform to fpprophet for univariate analysis
    df.columns = ['ds', 'y']
    df['ds'] = pd.to_datetime(df['ds'])
    # bring in fbprophet algorithm
    from prophet import Prophet


    model = Prophet()

    model.fit(df)

    # make future 1095 days prediction
    future_dates = model.make_future_dataframe(periods=1095)
    future_dates =future_dates.tail(1095)
    future_dates = future_dates[future_dates['ds'].dt.dayofweek < 5]
    # predict the days
    prediction = model.predict(future_dates)

    df1 = pd.DataFrame(future_dates,  columns = ['TRADE_DATE'])
    hh=[]
    tv=[]





    df_prediction = pd.DataFrame(prediction.tail(800))
    df_prediction.to_csv( x + '.csv')

    vDS =[]
    vTrainingSTOCKPRICE=[]
    vDS_Prediction =[]
    vPredictionSTOCKPRICE=[]
    vDIV =[]
    vPAYMENT_DATE= []
    vPAYMENT_DATE_withoutDuplicate=[]
    vPAYMENT_DATE_AVERAGE_PRICE = []
    vDIV_YIELD = []
    vEPS = []
    vPE_RATIO = []

    df_DIV = df_111.drop_duplicates(['PAYMENT_DATE', 'DIV'])[['PAYMENT_DATE', 'DIV' ]]
    AverageCloseprice=np.max( df_111['CLOSE_PRICE'])

    df_DIV['PAYMENT_DATE'] = pd.to_datetime(df_DIV['PAYMENT_DATE'])

    for index, row in df_111.iterrows():
        vDIV_YIELD.append(row['DIV_YIELD'])

        vPE_RATIO.append(row['PE_RATIO'])
        vEPS.append(row['EPS'])
        vPAYMENT_DATE_withoutDuplicate.append(row['PAYMENT_DATE'])
    df_DIV_removeduplicate = df_111

    for index, row in df_DIV_removeduplicate.iterrows():
        vDIV.append(row['DIV'])

    for index, row in df_DIV.iterrows():
        vPAYMENT_DATE.append(row['PAYMENT_DATE'])
        vPAYMENT_DATE_AVERAGE_PRICE.append(AverageCloseprice)

    for index, row in df_prediction.iterrows():
        # average  yhat lower and yhat upper  does the job.
        vPredictionSTOCKPRICE.append((row['yhat_upper'] + row['yhat_lower'])/2.0)
        vDS_Prediction.append(row['ds'])


    for index, row in df.iterrows():
        vTrainingSTOCKPRICE.append(row['y'])
        vDS.append(row['ds'])
    my_dpi = 100
    fig, axes = plt.subplots(nrows=5,  dpi=my_dpi)
    fig.set_size_inches(40.5, 40.5, forward=True)




    plt.suptitle(x + ' 01.JAN.2009  to  30.JUL.2022', fontsize=50)


    #axes[0].set_title(x)
    axes[0].grid()
    axes[0].set_ylabel('ClosePrice',fontsize = 30)
    sc1=axes[0].plot(vDS_Prediction, vPredictionSTOCKPRICE, color='b', label="predicted", linewidth=4.0)
    sc2=axes[0].plot(vDS, vTrainingSTOCKPRICE, color='g',label ="training", linewidth=4.0)

    sc3 = axes[0].bar(vPAYMENT_DATE, vPAYMENT_DATE_AVERAGE_PRICE, color='r',linewidth=4.0, label="Dividend Payout Date")


    axes[1].set_ylabel('Dividend',fontsize = 30)

    axes[1].grid()
    sc4=axes[1].plot(vPAYMENT_DATE_withoutDuplicate, vDIV, color='r',marker='*',linewidth=4.0)
    sc44 = axes[1].bar(vPAYMENT_DATE_withoutDuplicate, vDIV, color='g', linewidth=4.0)

    axes[2].set_ylabel('Dividend Yield',fontsize = 30)
    sc5=axes[2].plot(vDS, vDIV_YIELD, color='g', linewidth=4.0)
    axes[2].grid()

    axes[3].set_ylabel('EPS',fontsize = 30)
    sc6=axes[3].plot(vDS, vEPS, color='g', linewidth=4.0)
    axes[3].grid()


    axes[4].set_ylabel('PE_RATIO',fontsize = 30)
    sc7=axes[4].plot(vDS, vPE_RATIO, color='g', linewidth=4.0)
    axes[4].grid()

    axes[0].set_xlabel('DATE', fontsize=30)
    axes[1].set_xlabel('DATE', fontsize=30)
    axes[2].set_xlabel('DATE', fontsize=30)
    axes[3].set_xlabel('DATE', fontsize=30)
    axes[4].set_xlabel('DATE', fontsize=30)






    plt.grid()
    plt.show()
    kkk=len(vTrainingSTOCKPRICE)

    fig.savefig(x+'.png')

print("*****************************************************************")
print("*****************************************************************")

exit(0)