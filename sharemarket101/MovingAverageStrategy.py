import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from tabulate import tabulate
import pandas_datareader.data as pdr
import warnings


class MovingAverageStrategy:

    @staticmethod
    def moving_average_crossover(stock_symbol='ITC.NS', start_date='2021-01-01',
                                 end_date=datetime.datetime.today().strftime("%Y-%m-%d"),
                                 short_window=20, long_window=50, moving_avg='EMA', display_table=True):
        """
        The function takes the stock symbol, time-duration of analysis,
        look-back periods and the moving-average type(SMA or EMA) as input
        and returns the respective MA Crossover chart along with the buy/sell signals for the given period.


        stock_symbol - (str)stock ticker as on Yahoo finance. Eg: 'ITC.NS'

        start_date - (str)start analysis from this date (format: 'YYYY-MM-DD') Eg: '2021-01-01'

        end_date - (str)end analysis on this date (format: 'YYYY-MM-DD') Eg: '2022-01-01'

        short_window - (int)look-back period for short-term moving average. Eg: 5, 10, 20

        long_window - (int)look-back period for long-term moving average. Eg: 50, 100, 200

        moving_avg - (str)the type of moving average to use ('SMA' or 'EMA')

        display_table - (bool)whether to display the date and price table at buy/sell positions(True/False)
        """
        try:
            warnings.filterwarnings('ignore')
            stock_df = pdr.get_data_yahoo(stock_symbol, start_date, end_date)['Close']
            stock_df = pd.DataFrame(stock_df)
            stock_df.columns = {'Close Price'}
            stock_df.dropna(axis=0, inplace=True)

            short_window_col = str(short_window) + '_' + moving_avg
            long_window_col = str(long_window) + '_' + moving_avg

            if moving_avg == 'SMA':
                stock_df[short_window_col] = stock_df['Close Price'].rolling(window=short_window, min_periods=1).mean()

                stock_df[long_window_col] = stock_df['Close Price'].rolling(window=long_window, min_periods=1).mean()

            elif moving_avg == 'EMA':
                stock_df[short_window_col] = stock_df['Close Price'].ewm(span=short_window, adjust=False).mean()

                stock_df[long_window_col] = stock_df['Close Price'].ewm(span=long_window, adjust=False).mean()

            stock_df['Signal'] = 0.0
            stock_df['Signal'] = np.where(stock_df[short_window_col] > stock_df[long_window_col], 1.0, 0.0)

            stock_df['Position'] = stock_df['Signal'].diff()

            if stock_df['Signal'].iloc[-1] == 1.0 and \
                    stock_df['Close Price'].iloc[-1] > stock_df[short_window_col].iloc[-1]:
                plt.figure(figsize=(14, 7))
                plt.tick_params(axis='both', labelsize=14)
                stock_df['Close Price'].plot(color='black', alpha=0.5, lw=1, label='Close Price')
                stock_df[short_window_col].plot(color='blue', lw=1, label=short_window_col)
                stock_df[long_window_col].plot(color='g', lw=1, label=long_window_col)

                plt.plot(stock_df[stock_df['Position'] == 1].index,
                         stock_df[short_window_col][stock_df['Position'] == 1],
                         '^', markersize=15, color='g', alpha=0.7, label='buy')

                plt.plot(stock_df[stock_df['Position'] == -1].index,
                         stock_df[short_window_col][stock_df['Position'] == -1],
                         'v', markersize=15, color='r', alpha=0.7, label='sell')
                plt.ylabel('Price in ₹', fontsize=16)
                plt.xlabel('Date', fontsize=16)
                plt.title(str(stock_symbol) + ' - ' + str(moving_avg) + ' Crossover', fontsize=20)
                plt.legend()
                plt.grid()
                plt.show()

                if display_table:
                    df_pos = stock_df[(stock_df['Position'] == 1) | (stock_df['Position'] == -1)]
                    df_pos['Position'] = df_pos['Position'].apply(lambda x: 'Buy' if x == 1 else 'Sell')
                    print(stock_symbol)
                    print(tabulate(df_pos, headers='keys', tablefmt='psql'))

        except Exception as e:
            print(e)
