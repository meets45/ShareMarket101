import pandas_datareader as pdr
import datetime as dt


class MovingAverageTracker:
    def __init__(self):
        self.start = dt.datetime(2018, 1, 1)

    def moving_average_tracker(self, short_window, long_window, share_list):
        if short_window > long_window:
            print("Short Window cannot be greater than Long Window")
            exit()
        if short_window <= 0:
            print("Short window should be greater than 0")
            exit()

        print(f"Stocks with price above {short_window} DMA and {long_window} DMA and "
              f"{short_window} DMA > {long_window} DMA")
        print("----------------------------x----------------------------")
        for i in range(len(share_list)):
            data = pdr.get_data_yahoo(share_list[i] + ".NS", self.start)
            data['MA_short'] = data['Close'].rolling(short_window).mean()
            data['MA_long'] = data['Close'].rolling(long_window).mean()
            if data['Close'].iloc[-1] > data['MA_short'].iloc[-1] > data['MA_long'].iloc[-1]:
                print(share_list[i])
                print(f"Price: {data['Close'].iloc[-1]:.2f}")
                print(f"{short_window} DMA: {data['MA_short'].iloc[-1]:.2f}")
                print(f"{long_window} DMA: {data['MA_long'].iloc[-1]:.2f}")
                print("----------------------------x----------------------------")
            else:
                print(f"{share_list[i]}'s {short_window} DMA is not above {long_window} DMA")
                print("----------------------------x----------------------------")

    def moving_average_checker(self, short_window, long_window, share_name):
        if short_window > long_window:
            print("Short Window cannot be greater than Long Window")
            exit()
        if short_window <= 0:
            print("Short window should be greater than 0")
            exit()

        share_data = pdr.get_data_yahoo(share_name + ".NS", self.start)
        share_data['MA_short'] = share_data['Close'].rolling(short_window).mean()
        share_data['MA_long'] = share_data['Close'].rolling(long_window).mean()
        if share_data['Close'].iloc[-1] > share_data['MA_short'].iloc[-1] > share_data['MA_long'].iloc[-1]:
            print(f"Stock has price above {short_window} DMA and {long_window} DMA and "
                  f"{short_window} DMA > {long_window} DMA")
            print("----------------------------x----------------------------")
            print(share_name)
            print(f"Price: {share_data['Close'].iloc[-1]:.2f}")
            print(f"{short_window} DMA: {share_data['MA_short'].iloc[-1]:.2f}")
            print(f"{long_window} DMA: {share_data['MA_long'].iloc[-1]:.2f}")
            print("----------------------------x----------------------------")

        else:
            if share_data['Close'].iloc[-1] > share_data['MA_short'].iloc[-1]:
                print(f"{share_name}'s price is not above {short_window} DMA")
                print("----------------------------x----------------------------")

            elif share_data['MA_short'].iloc[-1] > share_data['MA_long'].iloc[-1]:
                print(f"{share_name}'s {short_window} DMA is not above {long_window} DMA")
                print("----------------------------x----------------------------")
