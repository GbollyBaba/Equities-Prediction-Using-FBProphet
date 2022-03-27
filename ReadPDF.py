import numpy
import pandas as pd
import tabula
import pandas as pd
import numpy as np
# readinf the PDF file that contain Table Data
# you can find find the pdf file with complete code in below
# read_pdf will save the pdf table into Pandas Dataframe
path ="/Users/akingboladeshada/Desktop/NSE/DATA/"
path_output ="/Users/akingboladeshada/Desktop/NSE/output/"

# list the files in the directory
import os
from os import listdir
from os.path import isfile, join
aaa= "3:2"
aaa.split(':')[0]

n = gas.size()
    for (int i = 0 to i < n) {
        fuel = gas[i]
        bool isAmple = true  // determine a valid starting point
        for (int j = 0 to j < n) {
            currStation = (i + j) % n
            nextStation = (currStation + 1) % n
            fuel = fuel - cost[currStation]
            // not reachable from currStation to nextStation
            if (fuel < 0) {
                isAmple = false
                break
            }
            // refuel in nextStation
            fuel = fuel + gas[nextStation]
        }
        if (isAmple) {
            return i
        }
    }
    return -1



onlyfiles = [os.path.join(path, f) for f in os.listdir(path) if
os.path.isfile(os.path.join(path, f))]
print(onlyfiles)
originalcols = ['Banking', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3',
                'Unnamed: 4', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8',
                'Unnamed: 9', 'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12',
                'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16',
                'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19']
neededcols = ['Banking', 'Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 8', 'Unnamed: 9',
              'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16',
              'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19']
remove_cols = ['c_PUBLIC_QUOTATION_PRICE', 'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']

totalpages=33
intfirst_df=1
for filename in onlyfiles:
    print(filename)
    #/Users/akingboladeshada/Desktop/NSE/DATA/Daily Official List - Equities for 15-09-2021
    ff=filename.replace('/Users/akingboladeshada/Desktop/NSE/DATA/Daily Official List - Equities for ', '')
    ff= ff.replace('.pdf','')
    strDate=ff;
    for v_pages in range(1,33):
        df_10 = tabula.read_pdf(filename, pages = v_pages, lattice = True)
        size_10 = len(df_10)- len(df_10)

        for i in (0,size_10-size_10):
            d= df_10[i]
            df_proxy=d
            c1=df_proxy.columns
            c2=d.columns
            totCols = len(c2)
            if (totCols>=21):

                df_proxy = df_proxy[df_proxy[df_proxy.columns[0]].notna()]
                df_proxy = df_proxy[df_proxy[df_proxy.columns[1]].notna()]
                df_proxy.drop(df_proxy[df_proxy[df_proxy.columns[0]] == 'Symbol'].index, inplace=True)
                df_proxy.drop(df_proxy[df_proxy[df_proxy.columns[0]] == 'Div'].index, inplace=True)

                df_proxy = df_proxy[df_proxy[df_proxy.columns[0]].notna()]
                df_proxy = df_proxy[df_proxy[df_proxy.columns[1]].notna()]
                df_proxy = pd.DataFrame(df_proxy)

                df_proxy = df_proxy.rename(columns={df_proxy.columns[0]: "C_SYMBOL"
                    , df_proxy.columns[1]: "c_EQUITY_NAME"
                    , df_proxy.columns[2]: "c_PUBLIC_QUOTATION_PRICE"
                    ,  df_proxy.columns[3]: "c_OFFICIAL_OPEN"
                    ,  df_proxy.columns[4]: "c_OFFICIAL_CLOSE"
                    ,  df_proxy.columns[5]: "c_CURRENT_MARKET_PRICE"
                    ,  df_proxy.columns[9]: "c_PRICE"
                    ,  df_proxy.columns[10]: "c_DATE"
                    , df_proxy.columns[11]: "c_QTY"
                    , df_proxy.columns[12]: "c_HIGH"
                    ,  df_proxy.columns[13]: "c_LOW"
                    ,  df_proxy.columns[14]: "c_LAST_EX_DIV_DATE"
                    ,  df_proxy.columns[15]: "c_LAST_EX_DIV_DATE"
                    ,  df_proxy.columns[16]: "c_DATE_PAID"
                    ,  df_proxy.columns[17]: "c_INTERIM"
                    ,  df_proxy.columns[18]: "c_FINALPAYMENT"
                    ,  df_proxy.columns[19]: "c_EPS"
                    ,  df_proxy.columns[20]: "c_PE"
                                           }
                                    )
                usethiscols = ["C_SYMBOL"
                ,"c_PUBLIC_QUOTATION_PRICE"
                ,"c_OFFICIAL_OPEN"
                , "c_OFFICIAL_CLOSE"
                ,"c_CURRENT_MARKET_PRICE"
                , "c_PRICE"
                , "c_DATE"
                , "c_QTY"
                ,"c_HIGH"
                ,"c_LOW"
                ,"c_LAST_EX_DIV_DATE"
                , "c_LAST_EX_DIV_DATE"
                ,"c_DATE_PAID"
                , "c_INTERIM"
                , "c_FINALPAYMENT"
                ,"c_EPS"
                , "c_PE"]

                #df_proxy =df_proxy.drop(remove_cols, axis=1)
                df_proxy_finishedProcessing = df_proxy[usethiscols]
                df_proxy_finishedProcessing.to_csv(path_output+''+str(intfirst_df)+'.csv', header=True, index=True)
                #df_proxy_finishedProcessing.to_csv('your_array.csv', header=False, index=False)
                if (intfirst_df==1):
                     df_Container =pd.DataFrame(df_proxy)
                     cols=df_Container.columns
                intfirst_df = intfirst_df + 1


