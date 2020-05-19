import requests
from bs4 import BeautifulSoup


def main():
    dollar = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80&aqs=chrome.0.69i59j35i39j0l5j69i61.3599j0j7&sourceid=chrome&ie=UTF-8'
    euro = 'https://www.google.com/search?sxsrf=ALeKk012L2q0DYFJEkBAlSIfc8-21HJgtA%3A1585516200432&ei=qA6BXpX7GZuWjgbYsYbYCg&q=%D0%B5%D0%B2%D1%80%D0%BE&oq=%D0%B5%D0%B2%D1%80%D0%BE&gs_lcp=CgZwc3ktYWIQAzIJCCMQJxBGEIICMgQIABBDMgUIABCDATICCAAyBAgAEEMyAggAMgIIADIECAAQQzIECAAQQzICCAA6BAgAEEc6BwgjELACECc6BAgAEA06BAgjECc6CggAEIMBEBQQhwI6BwgjEOoCECc6BggAEAoQAToICAAQChABECpQkMAgWLvdIGDk3yBoBHABeAKAAbgBiAGGCZIBBDEzLjGYAQCgAQGqAQdnd3Mtd2l6sAEK&sclient=psy-ab&ved=0ahUKEwiV76WPzMDoAhUbi8MKHdiYAasQ4dUDCAs&uact=5'
    funt = 'https://www.google.com/search?sxsrf=ALeKk00ecHAwnkwcx9pk-AlHykX7Eqhljg%3A1585516737912&ei=wRCBXu-oN-2cmwX3l6q4AQ&q=%D1%84%D1%83%D0%BD%D1%82&oq=%D1%84%D1%83%D0%BD%D1%82&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIECCMQJzIECAAQQzIECAAQQzIECAAQQzIFCAAQgwEyBAgAEEMyAggAMgQIABBDOgQIABBHUJSMAljLlAJgppYCaABwAXgAgAFViAGoApIBATSYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwivjcuPzsDoAhVtzqYKHfeLChcQ4dUDCAs&uact=5'
    btc = 'https://www.google.com/search?q=btc+usd&oq=btc&aqs=chrome.1.69i57j0l7.2830j0j7&sourceid=chrome&ie=UTF-8'
    sp = [dollar, euro, funt, btc]
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
    count = 0
    answer = 'Курсы валют по данным Google сейчас:\n'
    for valuta in sp:
        count += 1
        full_page = requests.get(valuta, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        if count < 5:
            convert = soup.find_all('span', {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2})
        else:
            convert = soup.find_all('span', {'class': 'IsqQVc', 'class': 'NprOob'})
        try:
            if count == 1:
                answer += '1 доллар = ' + convert[0].text + ' руб.\n'
            if count == 2:
                answer += '1 евро = ' + convert[0].text + ' руб.\n'
            if count == 3:
                answer += '1 британский фунт = ' + convert[0].text + ' руб.\n'
            if count == 4:
                answer += '1 Биткоин = ' + convert[0].text + ' дол.\n\n'
        except Exception:
            pass
    return answer

