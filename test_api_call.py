#!/usr/bin/env python3

from dotenv import load_dotenv 
import os 
import pandas_datareader as web
import pandas as pd 
import datetime


class Main:
#Test api call and retrieving api key form secret .env
    def get_historical_data(self, api_key):
        start = datetime.datetime(2006,1,1)
        end = datetime.datetime(2016,1,1) 

        symbols = ["BAC", "C", "GS", "JPM", "MS", "WFC"] #Tickers
        
        for i in symbols: 
            #Call alphavantage api for a panel object of daily timeseries data
            bank_stocks = web.av.time_series.AVTimeSeriesReader(
                        f"{i}", 
                        function='TIME_SERIES_DAILY',
                        start=start, end=end,
                        pause=15,
                        api_key=api_key)
        print(bank_stocks.read())
        
if __name__ == '__main__':         
    m = Main() 
    load_dotenv() 
    api_key = os.environ['API_KEY'] 
    print(api_key) #Loaded from local env to remain confidential. Will print None without secret env loaded
    m.get_historical_data(api_key) 


    
