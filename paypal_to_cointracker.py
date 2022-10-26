import pandas as pd
from datetime import datetime as dt
import pytz

class Transactions_Integration:

    def __init__(self, transaction_table = None) -> None:
        self.transaction_table = transaction_table

    def transform_csv(self) -> None:
        self.format_headers()

        # shape[0] provides number of rows, and accounts for NaN values
        for row in range(self.transaction_table.shape[0]): 
            old_date = self.transaction_table.at[row, 'Date']
            self.transaction_table.at[row, 'Date'] = self.format_date(old_date)

    def format_date(self, date) -> pd.DataFrame:
        datetime_old = dt.strptime(date, '%a, %d %b %Y %H:%M:%S %Z')
        return dt.strftime(datetime_old.replace(tzinfo=pytz.utc), '%m/%d/%Y %H:%M:%S %Z')

    def format_headers(self) -> None:
        # Drop unnecessary headers
        self.transaction_table.drop({'Transaction Type', 'Market Value (USD)'}, axis=1, inplace=True)

        # Convert from PayPal to CoinTracker headers
        new_headers={'DateTime':'Date', 'Asset In (Quantity)':'Received Quantity',
                     'Asset In (Currency) ':'Received Currency',
                     'Asset Out (Quantity) ':'Sent Quantity',
                     'Asset Out (Currency) ':'Sent Currency',
                     'Transaction Fee (Quantity) ':'Fee Amount',
                     'Transaction Fee (Currency) ':'Fee Currency'}
        self.transaction_table.rename(new_headers, axis=1, inplace=True)

        # Insert 'Tag' header at the end
        self.transaction_table.insert(len(self.transaction_table.columns), 'Tag', ['']*(len(self.transaction_table)))

    def read_csv(self, file_path, header=0) -> None:
        self.transaction_table = pd.read_csv(file_path, header=header)

    #def save_csv(self) -> None: