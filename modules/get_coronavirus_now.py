import requests
from bs4 import BeautifulSoup


def main():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.83 Safari/537.36'}
    full_page = requests.get('https://www.worldometers.info/coronavirus/', headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')

    all = soup.find_all('td')
    sp = []
    fl = False
    cnt = 0
    for i in all:
        i = i.text
        if fl:
            cnt += 1
            if i == '':
                i = '0'
            sp.append(i)
            if cnt == 5:
                break
        if i == 'World':
            fl = True
    for i in range(len(sp)):
        sp[i] = str(sp[i])
        sp[i] = sp[i].replace(',', '')
        sp[i] = sp[i].strip()
    answer = f'Мир:\nЗаболевших за все время: {sp[0]}, из них {sp[1]} новых случаев.\nУмерло {sp[2]}, включая {sp[3]} за последний день.\nПроцент выздоравления равен: {round(int(sp[4]) / (int(sp[4]) + int(sp[2])) * 100, 2)}%.\n\n'
    all = soup.find_all('td')
    sp = []
    fl = False
    cnt = 0
    for i in all:
        i = i.text
        if fl:
            cnt += 1
            if i == '':
                i = '0'
            sp.append(i)
            if cnt == 5:
                break
        if i == 'Russia':
            fl = True
    for i in range(len(sp)):
        sp[i] = str(sp[i])
        sp[i] = sp[i].replace(',', '')
        sp[i] = sp[i].strip()
    answer += f'Россия:\Заболевших за все время: {sp[0]}, из них {sp[1]} новых случаев.\nУмерло {sp[2]}, включая {sp[3]} за последний день.\nПроцент выздоравления равен: {round(int(sp[4]) / (int(sp[4]) + int(sp[2])) * 100, 2)}%.\n\n'
    return answer

