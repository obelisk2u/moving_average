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

def buy_sell(df, bound):
    cash_pos=0
    profit=0
    for i in range(0,len(df)):
        if(df['Accel'][i]>bound):
            cash_pos = cash_pos + df["oc_avg"][i]
        else:
            profit+=cash_pos
            cash_pos=0
    return profit

def main():
    filename = input("CSV file name (hit Return for demonstration): ")
    if(filename==""):
        filename="TSLA.csv"
        period=75
        bound=0
    else:
        period = input("Moving average period: ")
        bound = input("Buy sell bound: ")
    
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by = 'Date')
    df = analyze_data(df, period)
    profit=buy_sell(df, bound)

    print("Summary of MA Acceleration Method for: ", filename)
    print("Profit         |", profit)
    print("MA Period      |", period)
    print("Buy/Sell Bound |", bound)




if __name__ == '__main__':
    main()
