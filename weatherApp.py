import urllib.request, urllib.parse, urllib.error
import json
import ssl

#Service parameters
api_key = "tZjJfGYn5dsQYB9cCNDoHE4KBsyhSFYm"
locationServiceUrl = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?"
forecastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"
current24h = "http://dataservice.accuweather.com/currentconditions/v1/"

#Funtion for SSL-check, URL-open and JSON-handling
def url_service(url):
	# Ignore SSL certificate errors
	ctx = ssl.create_default_context()
	ctx.check_hostname = False
	ctx.verify_mode = ssl.CERT_NONE
	# URL handle and open
	url_handle = urllib.request.urlopen(url, context=ctx)
	data = url_handle.read().decode()
	global jdata
	jdata = json.loads(data)


#Parsing Location LIST
loc_find = input("Search Location: ")
urlloc = dict()
urlloc["apikey"] = api_key
urlloc["q"] = loc_find
urlloc["language"] = "en-en"

url_location = locationServiceUrl+urllib.parse.urlencode(urlloc)
url_service(url_location)

x = 0

location_dict = dict()
city_list = list()
for item in jdata:
	for k,v in item.items():
		if k == "Key":
			locationKey = v
		if k == "LocalizedName":
			location_city = v
		if k == "Country":
			location_country = v["LocalizedName"]
		if k == "AdministrativeArea":
			location_area = v["LocalizedName"]
	location_dict[x] = locationKey
	x = x + 1

	city_list.append((x, "City:", location_city, "Country:", location_country, "Area:", location_area, locationKey))

for i in city_list:
	print(i[0], i[2], i[4], i[6])

#Search for CURRENT Location
location = int(input("Choose your current location by number from the list: "))
l = location - 1
lkey = city_list[l]
key = lkey[7]+"?"

#Parsing Current Weather in Location
urlcw = dict()
urlcw["apikey"] = api_key
urlcw["language"] = "en-us"
urlcw["details"] = "true"

urlCurrWeather = current24h+lkey[7]+"/historical/24?"+urllib.parse.urlencode(urlcw)
url_service(urlCurrWeather)
currWeather = jdata

#Parsing 5-day Forecast
urlfc = dict()
urlfc["apikey"] = api_key
urlfc["language"] = "en-en"
urlfc["details"] = "true"
urlfc["metric"] = "true"

urlForecast = forecastUrl+key+urllib.parse.urlencode(urlfc)
url_service(urlForecast)
forecast = jdata

print()
print("Current weather in", lkey[1], lkey[2], lkey[3], lkey[4], ":")
print(currWeather[0]["WeatherText"])
print("Temperature", currWeather[0]["Temperature"]["Metric"]["Value"])
print("Feels like", currWeather[0]["RealFeelTemperature"]["Metric"]["Value"])
print("Wind direction", currWeather[0]["Wind"]["Direction"]["Localized"])
print("Wind speed", currWeather[0]["Wind"]["Speed"]["Metric"]["Value"])
print()
print("5 Day Forecast:")
print(forecast["DailyForecasts"][0]["Date"])
print(forecast["DailyForecasts"][0]["Temperature"]["Minimum"])
print(forecast["DailyForecasts"][0]["Temperature"]["Maximum"])
print(forecast["DailyForecasts"][0]["RealFeelTemperature"]["Minimum"])
print(forecast["DailyForecasts"][0]["RealFeelTemperature"]["Maximum"])
print(forecast["DailyForecasts"][0]["Day"]["IconPhrase"])



#print(json.dumps(currWeather, indent=4))
#print(json.dumps(forecast, indent=4))
