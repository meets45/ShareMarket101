import pandas_datareader as pdr
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import warnings


class BollingerBandsStrategy:

    @staticmethod
    def plot_bollinger_bands(ticker_name, start=dt.datetime(2022, 1, 1), end=dt.datetime.now()):
        ticker = pdr.get_data_yahoo(ticker_name, start, end)[['Close', 'High', 'Low']]
        ticker['TP'] = (ticker['Close'] + ticker['Low'] + ticker['High']) / 3
        ticker['std'] = ticker['TP'].rolling(20).std(ddof=0)
        ticker['MA-TP'] = ticker['TP'].rolling(20).mean()
        ticker['BOLU'] = ticker['MA-TP'] + 2 * ticker['std']
        ticker['BOLD'] = ticker['MA-TP'] - 2 * ticker['std']
        ticker = ticker.dropna()
        ax = ticker[['Close', 'BOLU', 'BOLD', 'MA-TP']].plot(color=['blue', 'orange', 'orange', 'black'])
        plt.title(f"{ticker_name.replace('.NS', '')}'s Bollinger Bands")
        ax.fill_between(ticker.index, ticker['BOLD'], ticker['BOLU'], facecolor='orange', alpha=0.1)
        plt.show()

    @staticmethod
    def bollinger_bands_strategy(ticker_name, start=dt.datetime(2022, 1, 1), end=dt.datetime.now()):
        warnings.filterwarnings('ignore')

        plt.style.use('fivethirtyeight')

        df = pdr.get_data_yahoo(ticker_name, start, end)
        period = 20

        df['SMA'] = df['Close'].rolling(window=period).mean()
        df['STD'] = df['Close'].rolling(window=period).std()
        df['Upper'] = df['SMA'] + (df['STD'] * 2)
        df['Lower'] = df['SMA'] - (df['STD'] * 2)

        new_df = df[period - 1:]

        def get_signal(data):
            buy_signal = []
            sell_signal = []

            for i in range(len(data['Close'])):
                if data['Close'][i] > data['Upper'][i]:
                    buy_signal.append(np.nan)
                    sell_signal.append(data['Close'][i])
                elif data['Close'][i] < data['Lower'][i]:
                    sell_signal.append(np.nan)
                    buy_signal.append(data['Close'][i])
                else:
                    buy_signal.append(np.nan)
                    sell_signal.append(np.nan)
            return buy_signal, sell_signal

        new_df['Buy'] = get_signal(new_df)[0]
        new_df['Sell'] = get_signal(new_df)[1]
        fig = plt.figure(figsize=(14, 7))
        ax = fig.add_subplot(1, 1, 1)
        x_axis = new_df.index
        ax.fill_between(x_axis, new_df['Upper'], new_df['Lower'], color='grey')

        ax.plot(x_axis, new_df['Close'], color='gold', lw=3, label='Close Price', alpha=0.5)
        ax.plot(x_axis, new_df['SMA'], color='blue', lw=3, label='Moving Average', alpha=0.5)
        ax.scatter(x_axis, new_df['Buy'], color='green', lw=3, label='Buy', marker='^', alpha=1)
        ax.scatter(x_axis, new_df['Sell'], color='red', lw=3, label='Sell', marker='v', alpha=1)
        ax.set_title(f'Bollinger Bands for {ticker_name.replace(".NS", "")}')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (₹)')
        ax.legend()
        plt.show()
