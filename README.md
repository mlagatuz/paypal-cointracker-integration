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

## Workflow

I'm using this exercise to help me with practice Data Structures and Algorithms (DSA's), coding in Python, and working a project end-to-end. I grabbed my whiteboard and came up with this algorithm:

***Overall algorithm***
1. Ingest entire CSV
2. format_headers

***format_headers algorithm***
- Drop first row (Paypal inserts disclaimer)
- Format Time
- Drop "Transaction Type" column
- Format Headers
- Drop "Market Value" column


## Notes for myself
*PayPal CSV headers:* <br>
    
    DateTime, Transaction Type, Asset In (Quantity), Asset In (Currency), Asset Out (Quantity), Asset Out (Currency), Transaction Fee (Quantity), Transaction Fee (Currency), Market Value (USD)

*CoinTracker CSV headers:* <br>

    Date, Received Quantity, Received Currency, Sent Quantity, Sent Currency, Fee Amount, Fee Currency, Tag

