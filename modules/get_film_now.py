import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://tvfeed.in/film/random/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    all = soup.find_all('h1', attrs={'class': 'f32'})
    name = str(all[0].text).strip()
    all = soup.find_all('a', attrs={'class': 'quicklink'})
    fl = False
    sp = []
    for i in all:
        i = str(i.text).strip()
        if i == 'регистрации':
            break
        if i == 'Телевидение' or fl == True:
            if fl is not True:
                fl = True
                continue
            sp.append(i)
    status = 0
    countries = 'Страны: '
    categories = 'Категории: '
    cnt = 0
    for i in sp:
        if status == 0 and i.isdigit() == False:
            cnt += 1
            if cnt == 1:
                countries += i
            else:
                countries += ', ' + i
        elif i.isdigit():
            status = 1
            cnt = 0
            year = 'Год: ' + str(i)
        else:
            cnt += 1
            if cnt == 1:
                categories += i
            else:
                categories += ', ' + i
    all = soup.find_all('div', attrs={'class': 'about'})
    about = 'Описание: ' + str(all[0].text).strip()

    return name + '\n' + categories + '\n' + year + '\n' + countries + '\n\n' + about


