import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 


def read_csv(filename):
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by = 'Date')
    return df

def main():
    df=read_csv("TSLA.csv")
    


if __name__ == '__main__':
    main()
