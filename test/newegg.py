import requests
from bs4 import BeautifulSoup
import json
import csv

def newegg(product):
    """
    this function will take the name of product as argument then
    go to the newegg online store and bring a data about title and price and link about this product 
    after that it will save the data in csv file
    """
    url = f'https://www.newegg.com/p/pl?d={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    all_data = [['title','price','links']]
    

    elements = soup.find_all('div',class_ = 'item-cell')
    

    for div in elements:
        try:
            one_item = []
            title = div.find('a',class_='item-title').text
            one_item.append(title)
            price = div.find('li',class_ = 'price-current').find('strong').text
            if ',' in price:
                continue
            else:
                one_item.append(f'${price}')
            link = div.find('a',class_='item-title').get('href')
            one_item.append(link)
            all_data.append(one_item)

        except:
            continue

    with open('newegg.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(all_data)

if __name__ == "__main__":
    newegg('tv')
            
            
            
            




  
        


    

    
   

    

    
    
    






    
    