import datetime
import os
import webbrowser
import modules.get_book_now as book
import modules.get_time_now as time_now
import modules.weather_now as weather_now
import modules.get_film_now as get_film
import modules.get_coronavirus_now as get_coronavirus
import modules.get_money_now as get_money
import modules.get_citate_now as get_citate
def check_command(word):
    try:
        word = word.lower()
        if word == 'привет' or word == 'приветствую':
            return 'Доброго времени суток, Ваше высочество!'

        if word == 'музыку':#
            webbrowser.open('https://music.yandex.ru', new=2)
        elif word == 'ютуб' or word == 'youtube':#
            webbrowser.open('https://www.youtube.com')
        elif 'вк' in word or 'vk' in word:#
            webbrowser.open('https://vk.com', new=2)
        elif word == 'гугл' or word == 'браузер' or word == 'интернет' or word == 'google':#
            webbrowser.open('https://google.com', new=2)
        elif word == 'проводник':#
            os.system(r'explorer.exe')
        elif word == 'стим' or word == 'steam':#
            os.startfile('C:\\Program Files (x86)\\Steam\\steam.exe')
        elif word == 'время' or word == 'времени':
            return get_time()
        elif word == 'прочитать' or word == 'прочесть' or word == 'почитать':
            return read()
        elif word == 'погода':
            return weather()
        elif word == 'посмотреть':
            return film()
        elif word == 'коронавирус':
            return coronavirus()
        elif word == 'курс':
            return money()
        elif word == 'цитату' or word == 'цитата':
            return citate()
        else:
            return 'Слово не определено.'
        return 'Дело сделано'
    except Exception:
        return 'Непредвиденная ошибка при обработки слова ' + word



def coronavirus():
    try:
        return get_coronavirus.main()
    except Exception:
        return 'Ошибка при получении информации по коронавирусу!'
def money():
    try:
        return get_money.main()
    except Exception:
        return 'Ошибка при получении курса валют!'
def citate():
    try:
        return get_citate.main()
    except Exception:
        return 'Ошибка при получении цитаты!'

def film():
    try:
        return get_film.main()
    except Exception:
        return 'При получении фильма произошла ошибка.'
def weather():
    try:
        return weather_now.main()
    except Exception:
        return 'Не удалось получить погоду.'
def get_time():
    try:
        return time_now.main()
    except Exception:
        return 'Ошибка при получении времени.'
def read():
    try:
        return book.main()
    except Exception:
        return 'Ошибка при получении книги'


