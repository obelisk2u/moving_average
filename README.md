# Trading Algorithms

Welcome to my **Trading Algorithms** repository! This project contains a collection of algorithmic trading strategies developed in Python that are executed on daily TSLA price data from 6-29-2010 until 3-24-2022. 

## Table of Contents
- [Algorithms](#algorithms)
- [Installation](#installation-steps)

## Algorithms
- **Momentum Trading**: Buys when second derivative with respect to the day before's price is positive and sells when is negative.
Run with:
    ```bash
    python ./momentum_trading.py
    ```

## Installation Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/obelisk2u/moving_average_accel.git
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```