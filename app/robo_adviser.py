from dotenv import load_dotenv
import csv 
import json #included in python language so don't need to install
import os
import requests
from IPython import embed

load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable
# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

# utility function to convert float or integer to usd-formatted string (for printing)
# ... adapted from: https://github.com/s2t2/shopping-cart-screencast/blob/30c2a2873a796b8766e9b9ae57a2764725ccc793/shopping_cart.py#L56-L59
def to_usd(my_price):
    return "${0:,.2f}".format(my_price) #> $12,000.71

#
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response)) #> class 'requests.models.reponse'
# print(response.status_code) #> '200' --> successful
# print (response.text) #> this text is a string so we need to use JSON to process into a dictionary

parsed_response = json.loads(response.text)  #> use this to parse from a string into a dictionary
    #> In Pdb, now that it's a dict we can access its keys by doing: parsed_response["Meta Data"]
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"] # this is a nested dictionary

#breakpoint()

tsd = parsed_response["Time Series (Daily)"] #just to be more shorthand

dates = list(tsd.keys()) #TODO assumes first day is on top but should sort to ensure latest day is first
latest_day = dates[0] #"2019-02-20"
latest_close = tsd[latest_day]["4. close"]

# need max of all of the high prices of each day
# high_prices = [10, 20, 30, 5]
#recent_high = max(high_prices) # can use the maximum function on a list

high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    high_prices.append(float(high_price))
    low_price = tsd[date]["3. low"]
    low_prices.append(float(low_price))

recent_high = max(high_prices)
recent_low = min(low_prices) 

#
# INFO OUTPUTS
#

# csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    
    # looping
    writer.writerow({
        "timestamp": "TODO",
        "open": "TODO",
        "high": "TODO",
        "low": "TODO",
        "close": "TODO",
        "volume": "TODO"
    })

# from https://github.com/s2t2/robo-advisor-screencast/blob/master/app/robo_advisor.py
print("-------------------------")
print("SELECTED SYMBOL: MSFT")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA")
print("REQUEST AT: 2018-02-20 02:00pm") #TODO use date time module
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}") # string interpolation using formatting string
print(f"LATEST CLOSE: {to_usd(float(latest_close))}") # need to convert to float in order to use usd function
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")
print("RECOMMENDATION: BUY!")  #TODO !!! use these values as part of the algorithm
print("BECAUSE: TODO")         #TODO !!!
print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
