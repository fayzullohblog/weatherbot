import requests
import json



def shahar(location):
    
	url = "https://yahoo-weather5.p.rapidapi.com/weather"

	querystring = {"location":location,"format":"json","u":"f"}

	headers = {
		"X-RapidAPI-Key": "fa04f8165dmshc05f6b4cdbaae3ep143269jsn30b042638c9a",
		"X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)
	data=json.loads(response.text)

	result=(
			f"Manzil: {data['location']['city']},{data['location']['country']} \n"
			f"Quyosh Chiqishi: {data['current_observation']['astronomy']['sunrise']} \n"
			f"Quyosh Botishi: {data['current_observation']['astronomy']['sunset']} \n"
			f"Time Zone: {data['location']['timezone_id']} \n"
			f"Kun: {data['forecasts'][0]['day']}"
		)
	
	return result
