from dotenv import load_dotenv
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





#
# INFO OUTPUTS
#




# from https://github.com/s2t2/robo-advisor-screencast/blob/master/app/robo_advisor.py
print("-------------------------")
print("SELECTED SYMBOL: MSFT")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #TODO use date time module
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}") # string interpolation using formatting string
print(f"LATEST CLOSE: {to_usd(float(latest_close))}") # need to convert to float in order to use usd function
print(f"RECENT HIGH: ")
print(f"RECENT LOW: ")
print("-------------------------")
print("RECOMMENDATION: BUY!") 
print("BECAUSE: TODO")
print("-------------------------")
print(f"WRITING DATA TO CSV: ")
print("-------------------------")
print("HAPPY INVESTING!")

