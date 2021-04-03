import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = "tZjJfGYn5dsQYB9cCNDoHE4KBsyhSFYm"
locationServiceUrl = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete?"
forecastUrl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

loc_find = input("Search Location: ")

urlloc = dict()
urlloc["apikey"] = api_key
urlloc["q"] = loc_find
urlloc["language"] = "en-en"

url = locationServiceUrl+urllib.parse.urlencode(urlloc)

url_handle = urllib.request.urlopen(url, context=ctx)
locdata = url_handle.read().decode()
#locdata = list()
#print(locdata)
jlocdata = json.loads(locdata)
#print(json.dumps(jlocdata, indent=4))

x = 0

location_dict = dict()
city_list = list()
for item in jlocdata:
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
#print(city_list)
for i in city_list:
	print(i[0], i[2], i[4], i[6])
#print(location_dict)



location = int(input("Choose your current location by number from the list: "))
l = location - 1
lkey = city_list[l]
key = lkey[7]+"?"

urlfc = dict()
#urlfc["key"] = key
urlfc["apikey"] = api_key
urlfc["language"] = "en-en"
urlfc["details"] = "true"
urlfc["metric"] = "true"


urlForecast = forecastUrl+key+urllib.parse.urlencode(urlfc)
url_h = urllib.request.urlopen(urlForecast, context=ctx)
forecast = url_h.read().decode()
jforecast = json.loads(forecast)
print(jforecast)
