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
        if '$' in str(soup):
            soup = soup.text.split(' ')[1]
        
        else:
            soup = BeautifulSoup(page.content, 'html.parser').find('div',class_='notranslate u-cb convPrice vi-binConvPrc padT10').find('span').text.replace('(',' ').split(' ')[1]

        return soup
    except:
        soup = BeautifulSoup(page.content, 'html.parser').find('div',class_='notranslate u-cb convPrice').find('span').text.replace('(',' ').split(' ')[1]
        return soup


if __name__ == "__main__":
    print(e_bay_price('https://www.ebay.com/itm/Lenovo-Thinkpad-X240-Laptop-Core-i5-Turbo-2-9Ghz-8GB-Ram-1TB-Rapid-SSD-Options/353090182091?_trkparms=aid%3D111001%26algo%3DREC.SEED%26ao%3D1%26asc%3D225074%26meid%3D533b39d6d420489d80996b30e28656f2%26pid%3D100970%26rk%3D2%26rkt%3D15%26mehot%3Dpp%26sd%3D164371817149%26itm%3D353090182091%26pmt%3D1%26noa%3D1%26pg%3D2380057%26brand%3DLenovo&_trksid=p2380057.c100970.m5481&_trkparms=pageci%3A6337f8f1-f684-11ea-bd51-74dbd180b018%7Cparentrq%3A8c8d4da31740ac3ec7705b61ffffa828%7Ciid%3A1'))
