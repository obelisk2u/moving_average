import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 



def analyze_data(df, period):
    #find avg of daily high/low
    df['hc_avg']=(df['Open']+df['Close'])/2

    #take moving average 
    df['MA']=df.rolling(window=period, min_periods=0)['hc_avg'].mean()

    #take slope of moving average
    df["Slope"]= df['MA'].diff()

    return df

def plot(df, xin, yin):
    df.plot(x=xin, y=yin)
    plt.show


def main():
    df = pd.read_csv('TSLA.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by = 'Date')
    df = analyze_data(df, 75)
    plot(df,'Date', 'Slope')
    plt.show()



if __name__ == '__main__':
    main()
