import requests
from bs4 import BeautifulSoup



def main():
    url = 'http://readly.ru/books/i_am_lucky/?show=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    all = soup.find_all('h3', attrs={'class': 'blvi__title'})
    name = (str(all))
    name = name[:-11]
    for i in range(len(name) - 1, -1, -1):
        if name[i] == '>':
            name = "Название: " + name[i+1::] + '\n'
            break

    all = soup.find_all('div', attrs={'class': 'book--desc'})
    desc = "Описание: " + str(all[0].text).strip()

    all = soup.find_all('span', attrs={'class': 'book-profile--rate'})
    rating = "Рейтинг: " + str(all[0].text).strip() + '\n\n'
    return name + rating + desc

