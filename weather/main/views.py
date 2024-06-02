from django.shortcuts import render
import json
import urllib.request
import os

weather_key = os.environ.get('WEATHER_KEY')

# Create your views here.

def index(request):
	if request.method == 'POST':
		# Extract user's input from the form/request
		city = request.POST['city']

		# Send API call to weather URL
		request = urllib.request.urlopen(
			'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + weather_key).read()

		# Convert API response to JSON
		response = json.loads(request)

		# format data from response
		data = {
			"county_code": str(response["sys"]["country"]),
			"coordinate": str(response["coord"]["lon"]) + ', ' + str(response["coord"]["lat"]),
			"temperature": str(response["main"]["temp"]) + 'K',
			"pressure": str(response["main"]["pressure"]),
			"humidity": str(response["main"]["humidity"]),
		}

		print(data)
	else:
		data = {} # return empty dictionary if API call fails

	return render(request, 'main/index.html', data)
