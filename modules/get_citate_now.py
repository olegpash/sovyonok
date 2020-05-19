import requests
from bs4 import BeautifulSoup


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
    full_page = requests.get('https://quote-citation.com/random', headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    text = soup.find_all('p')[0].text
    author = soup.find_all('p')[1].a.text
    answer = f'{text}\n\nАвтор: {author}'


    return answer


