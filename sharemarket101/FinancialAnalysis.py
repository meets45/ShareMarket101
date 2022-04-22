import yfinance


class FinancialAnalysis:

    def __init__(self, symbol):
        self.symbol = symbol

    def get_data(self):
        try:
            data = yfinance.Ticker(self.symbol)
            print(f"Book Value: {data.info['bookValue']:.2f}")
            print(f"Current Price: {data.info['currentPrice']:.2f}")
            print(f"Debt to Equity: {(data.info['debtToEquity']) * 100:.2f}%")
            print(f"Dividend Yield: {(data.info['dividendYield']) * 100:.2f}%")
            print(f"Earnings Growth: {(data.info['earningsGrowth']) * 100:.2f}%")
            print(f"Earnings Quarterly Growth: {(data.info['earningsQuarterlyGrowth']) * 100:.2f}%")
            print(f"EBITDA: {data.info['ebitda']:.2f}")
            print(f"EBITDA Margins: {(data.info['ebitdaMargins']) * 100:.2f}%")
            print(f"52 Wk High: {data.info['fiftyTwoWeekHigh']:.2f}")
            print(f"52 Wk Low: {data.info['fiftyTwoWeekLow']:.2f}")
            print(f"Industry: {data.info['industry']}")
            print(f"Long Name: {data.info['longName']}")
            print(f"Operating Margins: {(data.info['operatingMargins']) * 100:.2f}%")
            print(f"Price to Book: {data.info['priceToBook']:.2f}x")
            print(f"Profit Margins: {(data.info['profitMargins']) * 100:.2f}%")
            print(f"Return On Equity: {(data.info['returnOnEquity']) * 100:.2f}%")
            print(f"Trailing EPS: {data.info['trailingEps']:.2f}")
            print(f"Trailing PE: {data.info['trailingPE']:.2f}x")
            print(f"PEG Ratio: {data.info['pegRatio']:.2f}x")
            print(f"Trailing PEG Ratio: {data.info['trailingPegRatio']:.2f}x")
            print(f"Earnings Per Share: {data.info['forwardEps']:.2f}")
            print(f"Price to Earning Ratio: {data.info['forwardPE']:.2f}x")
        except Exception:
            print("Unable to fetch data")
