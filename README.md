# PAYPAL COINTRACKER INTEGRATION

## Motivation
The motivation behind this program: *practice Python coding concepts*, *learn functionality of Git and Github (through VSCode)*, and more importantly, ***I needed my PayPal crypto transactions uploaded into CoinTracker!***

As of 10/13/22, a seamless wallet integration for Paypal-to-CoinTracker is not available. At best, you would need to download your transactions from PayPal, reformat the CSV file, and upload into CoinTracker.

Thankfully, CoinTracker provides the following steps to integrate your PayPal wallet
1. Download the CSV transations export from PayPal
2. Reformat the CSV file
3. Import the file into CoinTracker

This [link](https://community.cointracker.io/t/convert-any-csv-into-the-cointracker-csv-format/553) provides a video walkthrough on how to properly convert any CSV file into a CoinTracker approved format, and outlines these steps for transformation:
- Reformat Dates
- Group data by transaction type (Buy, Sell, Swap)
- Convert data by transaction type

## Notes for myself

Utilizing this exercise as practice for Data Structures and Algorithms (DSA's), coding in Python, and working a project end-to-end. I grabbed my whiteboard and came up with this algorithm:

***Overall algorithm*** <br>
```
- Ingest entire CSV
- Transform CSV
```

***transform_csv*** <br>
```
- format_headers
- for row in range(number_of_rows)
-   format_date
```

*For transform_csv: shape[0] provides number of rows for DataFrame, and accounts for NaN values; Probably unnecessary, since 'Date' is a string; maybe an edge case; let me think about that*<br>

***format_headers algorithm*** <br>
```
- Drop first row (Paypal inserts disclaimer)
- Format Time
- Drop "Transaction Type" column
- Format Headers
- Drop "Market Value" column
```

***format_date algorithm*** <br>
```
- create datetime object from string
- convert string to new datetime object
- return new datetime object
```


*PayPal CSV headers:* <br>
    
    DateTime, Transaction Type, Asset In (Quantity), Asset In (Currency), Asset Out (Quantity), Asset Out (Currency), Transaction Fee (Quantity), Transaction Fee (Currency), Market Value (USD)

*CoinTracker CSV headers:* <br>

    Date, Received Quantity, Received Currency, Sent Quantity, Sent Currency, Fee Amount, Fee Currency, Tag

