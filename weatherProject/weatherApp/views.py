from django.shortcuts import render
import urllib.request
import json 


# Create your views here. 
def index(request):
    #post method is used to get the data from the form
    if request.method == 'POST':
        city = request.POST['city']
        #q stands for query and appid is the api key
        #Getting the data from the api
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=e6c346155a8146ac897a3ecbbd87d860').read()
        #converting json data to dictionary
        list_of_data = json.loads(source)
        #Data dictionary 
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' ' + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "main": str(list_of_data['weather'][0]['main']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": list_of_data['weather'][0]['icon'],
        } 
        print(data)
    else:
        data = {}
    #rendering the data to the index.html
    return render(request, 'index.html', data)