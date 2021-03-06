import urllib.request, urllib.parse, urllib.error
import json
import ssl
import constants

#Service parameters
api_key = constants.key
locationServiceUrl = 'http://dataservice.accuweather.com/locations/v1/cities/autocomplete?'
forecastUrl = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'
current = 'http://dataservice.accuweather.com/currentconditions/v1/'

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

while True:


	#Parsing Location LIST
	loc_find = input('Search Location: ')
	if loc_find == 'q' or loc_find == 'Q':
		break
	urlloc = dict()
	urlloc['apikey'] = api_key
	urlloc['q'] = loc_find
	urlloc['language'] = 'en-en'

	url_location = locationServiceUrl+urllib.parse.urlencode(urlloc)
	url_service(url_location)

	x = 0

	location_dict = dict()
	city_list = list()
	for item in jdata:
		for k,v in item.items():
			if k == 'Key':
				locationKey = v
			if k == 'LocalizedName':
				location_city = v
			if k == 'Country':
				location_country = v['LocalizedName']
			if k == 'AdministrativeArea':
				location_area = v['LocalizedName']
		location_dict[x] = locationKey
		x = x + 1

		city_list.append((x, 'City:', location_city, 'Country:', location_country, 'Area:', location_area, locationKey))

	if len(city_list) < 1:
		print('No location found! Try again!')
		continue

	for i in city_list:
		print(i[0], i[2], i[4], i[6])

	#Search for CURRENT Location
	location = int(input('Choose your current location by number from the list: '))
	if loc_find == 'q' or loc_find == 'Q':
		break
	l = location - 1
	lkey = city_list[l]
	key = lkey[7]+'?'

	#Parsing Current Weather in Location
	urlcw = dict()
	urlcw['apikey'] = api_key
	urlcw['language'] = 'en-us'
	urlcw['details'] = 'true'

	urlCurrWeather = current+lkey[7]+'?'+urllib.parse.urlencode(urlcw)
	url_service(urlCurrWeather)
	currWeather = jdata

	#dictCW = dict()



	#Parsing 5-day Forecast
	urlfc = dict()
	urlfc['apikey'] = api_key
	urlfc['language'] = 'en-en'
	urlfc['details'] = 'true'
	urlfc['metric'] = 'true'

	urlForecast = forecastUrl+key+urllib.parse.urlencode(urlfc)
	url_service(urlForecast)
	forecast = jdata

	fcDict = dict()
	for i in forecast['DailyForecasts']:
		date = i['Date']
		sunrise = i['Sun']['Rise']
		sunset = i['Sun']['Set']
		moonrise = i['Moon']['Rise']
		moonset = i['Moon']['Set']
		temperatureMin = i['Temperature']['Minimum']['Value']
		temperatureMax = i['Temperature']['Maximum']['Value']
		rfTemperatureMin = i['RealFeelTemperature']['Minimum']['Value']
		rfTemperatureMax = i['RealFeelTemperature']['Maximum']['Value']
		hoursOfSun = i['HoursOfSun']
		dayWeather = i['Day']['IconPhrase']
		daySky = i['Day']['LongPhrase']
		dayPercipProb = i['Day']['PrecipitationProbability']
		dayThundProb = i['Day']['ThunderstormProbability']
		dayWindSpeed = i['Day']['Wind']['Speed']['Value']
		dayWindDirect = i['Day']['Wind']['Direction']['Localized']
		dayWindGustSpeed = i['Day']['WindGust']['Speed']['Value']
		dayWindGustDirect = i['Day']['WindGust']['Direction']['Localized']
		dayTotalqd = i['Day']['TotalLiquid']['Value']
		dayRainMM = i['Day']['Rain']['Value']
		daySnowSM = i['Day']['Snow']['Value']
		dayIceMM = i['Day']['Ice']['Value']
		dayHrsOfPrecip = i['Day']['HoursOfPrecipitation']
		nightCloudCover = i['Night']['CloudCover']
		nightWeather = i['Night']['IconPhrase']
		nightSky = i['Night']['LongPhrase']
		nightPercipProb = i['Night']['PrecipitationProbability']
		nightThundProb = i['Night']['ThunderstormProbability']
		nightWindSpeed = i['Night']['Wind']['Speed']['Value']
		nightWindDirect = i['Night']['Wind']['Direction']['Localized']
		nightWindGustSpeed = i['Night']['WindGust']['Speed']['Value']
		nightWindGustDirect = i['Night']['WindGust']['Direction']['Localized']
		nightTotalqd = i['Night']['TotalLiquid']['Value']
		nightRainMM = i['Night']['Rain']['Value']
		nightSnowSM = i['Night']['Snow']['Value']
		nightIceMM = i['Night']['Ice']['Value']
		nightHrsOfPrecip = i['Night']['HoursOfPrecipitation']
		nightCloudCover = i['Night']['CloudCover']

	#Output
	print()
	print('Current weather in', lkey[1], lkey[2], lkey[3], lkey[4], ':')
	print('Weather', currWeather[0]['WeatherText'])
	print('Temperature', currWeather[0]['Temperature']['Metric']['Value'])
	print('Feels like', currWeather[0]['RealFeelTemperature']['Metric']['Value'])
	print('Wind direction', currWeather[0]['Wind']['Direction']['Localized'])
	print('Wind speed', currWeather[0]['Wind']['Speed']['Metric']['Value'])
	print()
	print('5 Day Forecast:')
	for i in forecast['DailyForecasts']:
		print('Date', i['Date'])
		print('Temperature minimum', i['Temperature']['Minimum']['Value'])
		print('Temperature maximum', i['Temperature']['Maximum']['Value'])
		print('Feels like minimum', i['RealFeelTemperature']['Minimum']['Value'])
		print('Feels like maximum', i['RealFeelTemperature']['Maximum']['Value'])
		print('Weather', i['Day']['IconPhrase'])
		print()
input()



#print(json.dumps(currWeather, indent=4))
#print(json.dumps(forecast, indent=4))