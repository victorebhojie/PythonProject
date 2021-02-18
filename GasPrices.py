import pandas as pd
import os

url = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls'

xls = pd.read_excel(url, sheet_name = None)

metadata = xls['Contents'] 


data =  xls['Data 1'] 


data.to_csv("Prices.csv") 


New_Csv = pd.read_csv("Prices.csv", index_col=[0])


New_Csv.drop([0,0],axis=0,inplace=True)

New_Csv.replace(['Henry Hub Natural Gas Spot Price (Dollars per Million Btu)'], 'Prices', inplace=True) 

New_Csv.to_csv("Newprices.csv",header=None,index=False)
os.remove("Prices.csv")
os.rename("Newprices.csv", "Prices.csv")