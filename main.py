import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

def plot(df, xin, yin):
    df.plot(x=xin, y=yin)
    plt.show

def analyze_data(df, period):
    #find avg of daily high/low
    df['oc_avg']=(df['Open']+df['Close'])/2

    #take moving average 
    df['MA']=df.rolling(window=period, min_periods=0)['oc_avg'].mean()

    #take discrete derivative of moving average
    df["Slope"] = df['MA'].diff()

    #take discrete second derivative of moving average
    df['Accel'] = df['Slope'].diff()

    return df

def buy_sell(df):
    cash_pos=0
    profit=0
    for i in range(0,len(df)):
        if(df['Accel'][i]>0):
            cash_pos = cash_pos + df["oc_avg"][i]
        else:
            profit+=cash_pos
            cash_pos=0
    print(profit)

def main():
    df = pd.read_csv('TSLA.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by = 'Date')
    df = analyze_data(df, 75)
    buy_sell(df)
    #plot(df,'Date', 'Accel')
    #plt.show()



if __name__ == '__main__':
    main()
