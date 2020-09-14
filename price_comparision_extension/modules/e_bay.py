import requests
from bs4 import BeautifulSoup
import json
import csv
from modules.helpres import Product


def e_bay(product):
    """
    this function will take the name of product as argument then
    go to the E_bay online store and bring a data about title and price and link about this product 
    after that it will save the data in csv file
    """
    url = f'https://www.ebay.com/sch/i.html?_nkw={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # all_data = [['title','price','links']]
    all_data = []

    elements = soup.find_all('li',class_ = 's-item')

    for li in elements:
        try:
            # one_item = []
            title = li.find('h3').text
            # one_item.append(title)
            price = li.find('span',class_ = 's-item__price').text[1:]
            # print(price)
            # one_item.append(price)
            link = li.find('a',class_ = 's-item__link').get('href')
            # one_item.append(link)
            one_item = Product(title, price, link, 'e_bay')
            all_data.append(one_item)

            if len(all_data) == 5:
                break

        except:
            continue

    return all_data

    # with open('ebay_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerows(all_data)

def e_bay_price(url):
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser').find('span',itemprop='price')
        if 'GBP' in str(soup):
            soup = BeautifulSoup(page.content, 'html.parser').find('div',class_='notranslate u-cb convPrice vi-binConvPrc padT10').find('span').text.replace('(',' ').split(' ')[1]
        
        else:
            soup = soup.text.split(' ')[1]

        return soup
    except:
        soup = BeautifulSoup(page.content, 'html.parser').find('div',class_='notranslate u-cb convPrice').find('span').text.replace('(',' ').split(' ')[1]
        return soup


if __name__ == "__main__":
    print(e_bay_price('https://www.ebay.com/itm/Apple-Watch-Series-4-40-mm-Silver-Aluminum-Case-Black-Sports-Band-GPS-Cellula/303687556482?hash=item46b5305d82:g:W0gAAOSwGUNfXOU2'))
