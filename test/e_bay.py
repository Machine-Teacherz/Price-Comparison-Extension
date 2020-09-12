import requests
from bs4 import BeautifulSoup
import json
import csv


def e_bay(product):
    """
    this function will take the name of product as argument then
    go to the E_bay online store and bring a data about title and price and link about this product 
    after that it will save the data in csv file
    """
    url = f'https://www.ebay.com/sch/i.html?_nkw={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')


    try:
        
        title = soup.find_all('h3',class_ = 's-item__title s-item__title--has-tags')
        all_title = [item.text for item in title]
    except:
        all_title = []

    try:
        price = soup.find_all('span',class_ = 's-item__price')
        all_price = [item.text.split(' ')[0] for item in price]
    except:
        all_price = []



    try:
        links = soup.find_all('a',class_ = 's-item__link')
        all_links = [item.get('href') for item in links]
    except:
        all_links = []
    
    i = 0
    all_data = []
    all_data.append(['title','price','links'])
    while i < 10:
        all_data.append([all_title[i],all_price[i],all_links[i]])
        i +=1


    
    
    with open('ebay_data.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(all_data)




if __name__ == "__main__":
    e_bay('apple watch')
    

    
    