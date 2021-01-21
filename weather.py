import requests 
import json

# api key 
api_key = 'ec83825c2e3c97e7c5ef444333abc294'

# base_url variable
base_url = 'http://api.openweathermap.org/data/2.5/weather?'


class WeatherReport(object):

	def __init(self):
		self.base_url = base_url
		self.api_key = api_key

	# returns the current day weather
	def get_current_day_weather(self):
		# city name 
		city_name = input('Enter city name: ')

		complete_url = base_url +'&q=' + city_name + "&appid=" + api_key 

		# sending a request
		#return a response object
		response = requests.get(complete_url)

		#json method of response object
		x = response.json() 

		# check if the city is found 
		if x["cod"] != '404':
			main_tag = x["main"]
			current_temp = main_tag["temp"]

			weather_tag = x["weather"]
			weather_description = weather_tag[0]["description"]

			print(" Temperature: " + str(current_temp))
			print(" Description: " + str(weather_description))
		else:
			print("city not found")






