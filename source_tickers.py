#!/usr/bin/env python3

from dotenv import load_dotenv 
import os 
import pandas_datareader as web
import pandas as pd 
import datetime
import time


class Main:
    symbols = ["BAC", "C", "GS", "JPM", "MS", "WFC"] #Tickers 
    def get_historical_data(self, api_key):
        """
        Extract historical data from AlphaVantage API.
        Output to csv in local dir. 
        """
        start = datetime.datetime(2006,1,1)
        end = datetime.datetime(2016,1,1) 

        # Bank of America
        BAC = web.DataReader("BAC", 'av-daily', start, end, api_key=api_key)

        # CitiGroup
        C = web.DataReader("C", 'av-daily', start, end, api_key=api_key)

        # Goldman Sachs
        GS = web.DataReader("GS", 'av-daily', start, end, api_key=api_key)

        # JPMorgan Chase
        JPM = web.DataReader("JPM", 'av-daily', start, end, api_key=api_key)

        time.sleep(60) #Add a delay.  API limits 5 requests per minute.

        # Morgan Stanley
        MS = web.DataReader("MS", 'av-daily', start, end, api_key=api_key)

        # Wells Fargo
        WFC = web.DataReader("WFC", 'av-daily', start, end, api_key=api_key)

        #Concatenate DataFrames. Keys are not duplicates ei BAC, BAC.1, BAC.2,... represent unique values.
        #Integers trailling keys(symbols)  are intended to assist interporability of DataFrame. 
        bank_stocks = pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1, keys=self.symbols)
        bank_stocks.columns.names = ["Bank", "Date"] #Improve readability.
        print(bank_stocks.head())  
        
        #Output to csv.
        bank_stocks.to_csv('bank_stocks.csv', index=False) 
        print("Data output to bank_stocks.csv in local dir.") 
    

        
if __name__ == '__main__':         
    m = Main() 
    load_dotenv() 
    #Loaded from local env to remain confidential. Will print None without secret env loaded
    api_key = os.environ['API_KEY'] 
    if api_key:
        print("API key retrieved.  Extracting datapoints...")
        m.get_historical_data(api_key) 
    else:
        print("No api key found") 


    
