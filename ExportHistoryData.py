# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:17:44 2018

@author: reby
"""

#Import the libraries

import pandas as pd
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import datetime
import configparser


##Configure API for Oanda

config = configparser.ConfigParser()
config.read(r'C:\Users\reby\Desktop\Python Projects\Oanda Project - Testing\config\config_v20.ini')
accountID = config['oanda']['account_id']
access_token = config['oanda']['api_key']
client = oandapyV20.API(access_token=access_token)

###Setup the dataframe and variables
def historydatahead():
    historicaldata = {
          "count": 5000,
          "granularity": "M"}
    r = instruments.InstrumentsCandles(instrument="EUR_USD",
                                   params=historicaldata)
    client.request(r)
    r.response['candles'][0]['mid']
    r.response['candles'][0]['time']
    r.response['candles'][0]['volume']
    dat = []
    for oo in r.response['candles']:
        dat.append([oo['time'], oo['volume'], oo['mid']['o'], oo['mid']['h'], oo['mid']['l'], oo['mid']['c']])
    global pulledhistorydata
    df = pd.DataFrame(dat)
    df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
    pulledhistorydata = df.head()
    

def historydata():
    historicaldata = {
          "count": 5000,
          "granularity": "M"}
    r = instruments.InstrumentsCandles(instrument="EUR_USD",
                                   params=historicaldata)
    client.request(r)
    r.response['candles'][0]['mid']
    r.response['candles'][0]['time']
    r.response['candles'][0]['volume']
    dat = []
    for oo in r.response['candles']:
        dat.append([oo['time'], oo['volume'], oo['mid']['o'], oo['mid']['h'], oo['mid']['l'], oo['mid']['c']])
    global pulledhistorydata
    df = pd.DataFrame(dat)
    df.columns = ['Time', 'Volume', 'Open', 'High', 'Low', 'Close']
    pulledhistorydata = df

####Create Function for dataframes to run simultainiously
def getdataframe():
    historydatahead()
    historydata()

#####Run the function
getdataframe()

######Convert to an Excel File
pulleddata = pd.DataFrame(pulledhistorydata)
pulleddata = pulleddata.to_excel(r'C:\Users\reby\Desktop\Python Projects\Historical FX Data\1_Month.xlsx', index=None, header=True)
