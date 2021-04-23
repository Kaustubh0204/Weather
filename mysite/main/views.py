from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key
			place api_key in place of appid ="your_api_key_here " '''

        # source contain JSON data from API
        user_api = 'b21875bc852a45bb9ce3bd1dae98ba98'
        source = urllib.request.urlopen(
            "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+user_api).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str((list_of_data['main']['temp']) - 273.15) + '°C',
            "pressure": int(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "desc": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "city": city,
            "link":  "http://openweathermap.org/img/wn/"+list_of_data['weather'][0]['icon']+"@2x.png"
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
