import requests
from bs4 import BeautifulSoup
import json
import csv
from modules.helpres import Product


def newegg(product):
    """
    this function will take the name of product as argument then
    go to the newegg online store and bring a data about title and price and link about this product 
    after that it will save the data in csv file
    """
    url = f'https://www.newegg.com/p/pl?d={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # all_data = [['title','price','links']]
    
    all_data = []

    elements = soup.find_all('div',class_ = 'item-cell')
    

    for div in elements:
        try:
            one_item = []
            title = div.find('a',class_='item-title').text
            # one_item.append(title)
            
            price = div.find('li',class_ = 'price-current').find('strong').text
            new_price = price
            for i in range(len(price)):
                if price[i] == ',':
                    new_price = price[:i] + price[i+1:]

            # if ',' in price:
            #     continue
            # else:
            #     one_item.append(f'${price}')
            
            link = div.find('a',class_='item-title').get('href')
            # one_item.append(link)
            
            one_item = Product(title, new_price, link, 'newegg')
            all_data.append(one_item)

            if len(all_data) == 5:
                break
        except:
            continue

    
    return all_data

    # with open('newegg.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerows(all_data)

if __name__ == "__main__":
    print(newegg('tv'))
            
            
            
            




  
        


    

    
   

    

    
    
    






    
    