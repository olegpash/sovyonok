import datetime


def main():
    hour = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    if hour == '2' or hour == '3' or hour == '4' or hour == '22' or hour == '23':
        hour_phrase = 'часа'
    elif hour == '1' or hour == '21':
        hour_phrase = 'час'
    else:
        hour_phrase = 'часов'
    if minute == '1' or minute == '21' or minute == '31' or minute == '41' or minute == '51':
        minute_phrase = 'минута'
    elif minute == '2' or minute == '3' or minute == '4' or minute == '22' or minute == '23' or minute == '24' or minute == '32' or minute == '33' or minute == '34' or minute == '42' or minute == '43' or minute == '44' or minute == '52' or minute == '53' or minute == '54':
        minute_phrase = 'минуты'
    else:
        minute_phrase = 'минут'
    return 'Сейчас ' + hour + ' ' + hour_phrase + ' ' + minute + ' ' + minute_phrase

