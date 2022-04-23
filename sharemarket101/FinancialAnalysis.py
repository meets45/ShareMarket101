import yfinance
import tabulate


class FinancialAnalysis:

    def __init__(self, symbol):
        self.symbol = symbol

    def get_data(self):
        """This function is used to get fundamental information about stock ticker you enter such as P/E Ratio,
        P/B Ratio, OPM, Div. Yield, EPS, ROE, PEG Ratio. It also provides basic information about major shareholding
         pattern and list of institutional shareholders if available.

        symbol - (str)Name of stock ticker you want to analyze. Eg: 'RELIANCE.NS'
        """
        try:
            data = yfinance.Ticker(self.symbol)
            if data.info['bookValue'] is None:
                print(f"Book Value: {data.info['bookValue']}")
            else:
                print(f"Book Value: {data.info['bookValue']:.2f}")
            print(f"Current Price: {data.info['currentPrice']:.2f}")

            if data.info['debtToEquity'] is None:
                print(f"Debt to Equity: {(data.info['debtToEquity'])}")
            else:
                print(f"Debt to Equity: {(data.info['debtToEquity'])/100:.2f}x")

            if data.info['dividendYield'] is None:
                print(f"Dividend Yield: {(data.info['dividendYield'])}")
            else:
                print(f"Dividend Yield: {(data.info['dividendYield']) * 100:.2f}%")

            if data.info['earningsGrowth'] is None:
                print(f"Earnings Growth: {(data.info['earningsGrowth'])}")
            else:
                print(f"Earnings Growth: {(data.info['earningsGrowth']) * 100:.2f}%")

            if data.info['earningsQuarterlyGrowth'] is None:
                print(f"Earnings Quarterly Growth: {(data.info['earningsQuarterlyGrowth'])}")
            else:
                print(f"Earnings Quarterly Growth: {(data.info['earningsQuarterlyGrowth']) * 100:.2f}%")

            if data.info['forwardEps'] is None:
                print(f"Earnings Per Share: {data.info['forwardEps']}")
            else:
                print(f"Earnings Per Share: {data.info['forwardEps']:.2f}")

            if data.info['ebitdaMargins'] is None:
                print(f"EBITDA Margins: {(data.info['ebitdaMargins'])}")
            else:
                print(f"EBITDA Margins: {(data.info['ebitdaMargins']) * 100:.2f}%")

            print(f"52 Wk High: {data.info['fiftyTwoWeekHigh']:.2f}")
            print(f"52 Wk Low: {data.info['fiftyTwoWeekLow']:.2f}")
            print(f"Industry: {data.info['industry']}")
            print(f"Long Name: {data.info['longName']}")

            if data.info['operatingMargins'] is None:
                print(f"Operating Margins: {(data.info['operatingMargins'])}")
            else:
                print(f"Operating Margins: {(data.info['operatingMargins']) * 100:.2f}%")

            if data.info['pegRatio'] is None:
                print(f"PEG Ratio: {data.info['pegRatio']}")
            else:
                print(f"PEG Ratio: {data.info['pegRatio']:.2f}x")

            if data.info['priceToBook'] is None:
                print(f"Price to Book: {data.info['priceToBook']}")
            else:
                print(f"Price to Book: {data.info['priceToBook']:.2f}x")

            if data.info['forwardPE'] is None:
                print(f"Price to Earnings Ratio: {data.info['forwardPE']}")
            else:
                print(f"Price to Earnings Ratio: {data.info['forwardPE']:.2f}x")

            if data.info['profitMargins'] is None:
                print(f"Profit Margins: {(data.info['profitMargins'])}")
            else:
                print(f"Profit Margins: {(data.info['profitMargins']) * 100:.2f}%")

            if data.info['returnOnEquity'] is None:
                print(f"Return On Equity: {(data.info['returnOnEquity'])}")
            else:
                print(f"Return On Equity: {(data.info['returnOnEquity']) * 100:.2f}%")

            if data.info['trailingEps'] is None:
                print(f"Trailing EPS: {data.info['trailingEps']}")
            else:
                print(f"Trailing EPS: {data.info['trailingEps']:.2f}")

            if data.major_holders is None:
                pass
            else:
                print("\nMajor Shareholding Pattern:")
                print(tabulate.tabulate(data.major_holders, tablefmt='pretty'))

            if data.institutional_holders is None:
                pass
            else:
                print("\nMajor Institutional Shareholders:")
                print(tabulate.tabulate(data.institutional_holders, headers='keys', tablefmt='psql'))

        except Exception as e:
            print(e)
