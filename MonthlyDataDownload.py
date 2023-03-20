import yfinance as yf

# Download data for Apple Inc. (AAPL) for the past 10 years
df = yf.download('AAPL', period='10y', interval='1mo')

# Save the data to a CSV file
# df.to_csv('aapl.csv')

print(df.head(10))