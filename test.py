from iexfinance.stocks import get_historical_intraday
from datetime import datetime
import pandas as pd
from pprint import pprint


date = datetime(2022, 8, 10)
df1 = get_historical_intraday("AAPL", date=date, outputformat='pandas')
date = datetime(2022, 8, 11)
df2 = get_historical_intraday("AAPL", date=date, outputformat='pandas')
# lst = [df1, df2]
# new_df = pd.concat(lst)
# print(new_df.columns)
# print(new_df[['marketOpen', 'marketClose', 'changeOverTime', 'marketChangeOverTime']])

pprint(df1[0])