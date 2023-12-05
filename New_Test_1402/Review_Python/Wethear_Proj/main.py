import requests

from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


# OpenWeatherMap API key (Get your API key by signing up at https://home.openweathermap.org/users/sign_up)

api_key = "YOUR_API_KEY_HERE"


@app.route("/", methods=["GET", "POST"])

def index():

    if request.method == "POST":

        city = request.form["city"]

        weather_data = get_weather_data(city)

        return render_template("index.html", weather_data=weather_data)

    return render_template("index.html")

def get_weather_data(city):

    url = f"http://api.openweathermap.org/data/2.5/forecast"

    params = {"q": city, "appid": api_key, "units": "metric"}

    response = requests.get(url, params=params)

    data = response.json()

    if data["cod"] == "200":

        weather_data = {

            "city": data["city"]["name"],

            "country": data["city"]["country"],

            "forecast": []

        }

        for forecast in data["list"]:

            weather_data["forecast"].append({

                "date": forecast["dt_txt"],

                "temperature": forecast["main"]["temp"],

                "description": forecast["weather"][0]["description"],

                "icon": forecast["weather"][0]["icon"]

            })

        return weather_data

    return None

if __name__ == "__main__":

    app.run(debug=True)