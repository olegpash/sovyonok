import requests, pyowm
from bs4 import BeautifulSoup


def main(city='Пенза'):
    key = 'e546183cd7ea27126bdb70949d8780ca'
    owm = pyowm.OWM(key, language='ru')
    city = (city)
    observation = owm.weather_at_place(city)
    w = observation.get_weather()
    temperature = w.get_temperature()
    answer = "В городе " + city + ' сейчас ' + str(round(int(temperature.get('temp')) - 273.15, 2)) + "°C,\n"
    answer += "На улице " + w.get_detailed_status() + '.'
    return answer
