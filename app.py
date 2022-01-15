from flask import Flask, render_template, url_for, request
import json, requests

from instagram.client import InstagramAPI

app = Flask(__name__)


bearer_token = "AAAAAAAAAAAAAAAAAAAAANwnYAEAAAAA2oRPlKrwSLeloSMUFu7O%2BlUm6l0%3DNGLclk39Ps0QowaZ3XV1TpDfa9tMxzc0s0PKRV1ZTRUO5kb7xn"
search_url = "https://api.twitter.com/2/users/1481327998586527755/tweets"
query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}

@app.route("/")
def index():   
    city = "Lublin"
    API_key = "61c66953209ff42795cae8fb985bdcec"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}&units=metric&lang=PL"

    res = requests.get(url)
    data = res.json()
    #print(data) # MAIN DF
    #print(data['weather']) # CLOUDS / ICON: [0]{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}
    #print(data['main']) # TEMP INFO: {'temp': 1.78, 'feels_like': -4.33, 'temp_min': 0.13, 'temp_max': 1.88, 'pressure': 1018, \
                        #               'humidity': 73, 'sea_level': 1018, 'grnd_level': 989}
    #print(data['wind']) # WIND INFO: {'speed': 8.9, 'deg': 310, 'gust': 16.51}

    # current_temp = data['main']['temp']
    # feels_like = data['main']['feels_like']
    # pressure = data['main']['pressure']
    # condition = data['weather'][0]['description']

    return render_template("index.html", data=data)



@app.route('/tst')
def tst_page():

   
    return render_template("index.html") 




    


if __name__ == "__main__":
    app.run(debug=True)
    