import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


def read_csv(filename):
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by = 'Date')
    return df

def moving_avg(df, dt):
    df['MA']=df.rolling(window=dt, min_periods=0)['Open'].mean()
    print(df.iloc[0:100,7])
    return df


def main():
    df=read_csv("TSLA.csv")
    df=moving_avg(df, 100)
    df.plot(x = 'Date', y = 'MA')

    plt.show()



if __name__ == '__main__':
    main()
