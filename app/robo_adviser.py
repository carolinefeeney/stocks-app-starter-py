from dotenv import load_dotenv
import json #included in python language so don't need to install
import os
import requests
from IPython import embed

load_dotenv() # loads environment variables set in a ".env" file, including the value of the ALPHAVANTAGE_API_KEY variable

#
# INFO INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"

response = requests.get(request_url)
# print(type(response)) #> class 'requests.models.reponse'
# print(response.status_code) #> '200' --> successful
# print (response.text) #> this text is a string so we need to use JSON to process into a dictionary

parsed_response = json.loads(response.text)  #> use this to parse from a string into a dictionary

breakpoint()




quit()

#
# INFO OUTPUTS
#



# see: https://www.alphavantage.co/support/#api-key
api_key = os.environ.get("ALPHAVANTAGE_API_KEY") or "OOPS. Please set an environment variable named 'ALPHAVANTAGE_API_KEY'."

symbol = "NFLX" #TODO: capture user input

# see: https://www.alphavantage.co/documentation/#daily
# TODO: assemble the request url to get daily data for the given stock symbol

# TODO: issue a "GET" request to the specified url, and store the response in a variable

# TODO: parse the JSON response

latest_price_usd = "$100,000.00" # TODO: traverse the nested response data structure to find the latest closing price

print(f"LATEST DAILY CLOSING PRICE FOR {symbol} IS: {latest_price_usd}")
