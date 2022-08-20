# Fintech_Project_2
![](https://blockupdate.io/wp-content/uploads/2019/02/price-chart.jpg)

Introduction:

------------

## Goal

We are developing an effective learning model that can predict proper entry and exist signals for short and long term trades in the highly volatile crypto market.

## Table-of-Contents

* > [General Information](#General-Information)
* > [Customer Profile](#Customer-Profile)
* > [Technical Indicators](#Technical-Indicators)
* > [Problems with Retail](#Problems-with-Retail)
* >  [Scenario](#features)
* >  [Three things Pros have in Common](#Three-things-Pros-have-in-Common)
* >  [Scenario](#Scenario)
* >  [Solution](#Solution)
* > [Investment Plan](#Investment-Plan)
* > [Project Deliverables](#Project-Deliverables)
* > [Features](#Features)
* > [Usage](#project-status)
* >  [Contact](#contact)

## General Information

Our goal is to develop an effective learning model that can predict proper entry and exist signals for short and long term trades in the highly volatile crypto market.

## Customer Profile

Short Term Investor:
A scalper trading utilizing a minute, hour, or day chart. This person loves using technical indicators but uses too many. They leave no clear direction when to enter or exist a trade.  

Long Term Investor:
This investor may want to dollar cost into a trading range but would prefer to buy cryto at a cheaper price. Or, this investor is looking for the perfect signals for a long or short in an exisiting trade. This investor doesn't have the time to update charts everyday and trade, but this investor understands technical indicators.

## Problems with Retail

* > Time spent analzing charts
* > Panic trading
* >  False signals
* >  Fraud
* > Mulpiniulation
* > Inconsistancy
* > Confusion

## Three things Pros have in Common

* >  Patience
* > Toolbox
* > Strategy

The purpose of our project is to save the retail investor money and time.  Our Crypto Surfer Trading Strategy has all three professional trader componets making any retail trader a professional in their own right.

* > Patience:  the module waits for signals: no emotions invloved
* >  oolbox:  Our trading strategy combines technical indicators into a single strategy
* > Learning: We use machine and deep learning to predict future prices

## Technical_Indicators

### Momentum

Momentum indicators return a selling signal when prices start to move strongly higher, and a buying signal when prices start to move strongly lower. We used the Commodity Channel Index indicator to measure momentum.

CCI
CCI measures the difference between a security’s price change and its average price change. High positive readings indicate that prices are well above their average, which is a show of strength. Low negative readings indicate that prices are well below their average, which is a show of weakness.

Calculation
classta.trend.CCIIndicator(high: pandas.core.series.Series, low: pandas.core.series.Series, close: pandas.core.series.Series, window: int = 20, constant: float = 0.015, fillna: bool = False)
Commodity Channel Index (CCI)

### Trend

The Trend indicator determines whether an asset is currently overbought or oversold. Many trend following indicators, attempt to create a clear “channel". A clear channel will tell you whether prices are close to breaking out or returning to normal. We use the Moving Average Convergence Divergence indicator (MACD).

MACD
Is a trend-following momentum indicator that shows the relationship between two moving averages of prices.The MACD is calculated using two exponential moving averages (EMA) - short term and long term. An exponential moving average of MACD is used as a signal line to indicate the upward or downward momentum. An exponential moving average is nothing but simply a moving average that gives more weightage to the recent data.

Calculation
classta.trend.MACD(close: pandas.core.series.Series, window_slow: int = 26, window_fast: int = 12, window_sign: int = 9, fillna: bool = False)
Moving Average Convergence Divergence (MACD)

### Volatility

 as their name suggests, measure the volatility of the underlying instrument. We used the Average True Range (ATR) indicator to measure volatility.

ATR
The ATR indicator moves up and down as price moves in an asset become larger or smaller.

Calculation
To calculate the ATR by hand, you must first calculate a series of true ranges (TRs). The TR for a given trading period is the greatest of the following:

Current high minus the previous close
Current low minus the previous close
Current high minus the current low
Whether the number is positive or negative doesn't matter. The highest absolute value is used in the calculation.

Current ATR = ((Prior ATR x 13) + Current TR) / 141

## Scenario

Short term retail crypto trader that typically spends $5,000 a year trading on various carypto exchanges. The trader is very fimiliar with technical anaiysis but doesn't have the time to setup trades and conduct fundenmental analisis to predict future prices. This trader would rather use our stratgey than lending cytpo for APY, but wants to see a %15 return within a year.  

## Solution

A trading strategy that combines multiple technical indicators into a single strategy.  

Use indicator classifications associated with, Momentum, Trend, Volume, and Volatility

Use indicators to create a machine learning model that produces buy and sale signals

Create the algorithm based on training data

Program the model to make entry and exist trade decisions without being explicitly programmed to do so.

formulate a trading plan for short and long term traders

## Features & Screenshots

* Visualization of Data
* Aggregated Dashboard
* Machince Learning  
* Random Forest *
* Linear Regression *

## Investment Plan

| Investment     | Coin          | term |  | Expected ROI| Broker Fees   | Software Price|  
| ------------- |:-------------:| -----:|  ------------- |:-------------:| -------------:|
| $5,000         | BTC          | 365 days |%15          .075 Maker/Taker       $500

0.1000% / 0.1000%
Profit
Cumlative Returns

## Project Deliverables

* Scoping Document
* PowerPoint
* README.md
* GitHub Repository

## Usage (add link to code)

How does one go about using it?
Provide various use cases and code examples here:

`write-your-code-here`

## Project Status

Project is: _in progress_ / _complete_ / _no longer being worked on_. If you are no longer working on it, provide reasons why.

## Room for Improvement

Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:

* Improvement to be done 1
* Improvement to be done 2

To do:

* Feature to be added 1
* Feature to be added 2

## Acknowledgements

Give credit here.

## Contact
![](https://media.giphy.com/media/3oeSALRyH4rYS3Nt8Q/giphy.gif)