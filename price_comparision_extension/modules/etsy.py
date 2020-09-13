import requests
from bs4 import BeautifulSoup
import json
import csv
from modules.helpres import Product


def etsy(product):
    """
    this function will take the name of product as argument then
    go to the E_bay online store and bring a data about title and price and link about this product 
    after that it will save the data in csv file
    """
    url = f'https://www.etsy.com/search?q={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # all_data = [['title','price','links']]
    all_data = []

    elements = soup.find_all('li' )
    
    for li in elements:
        try:
            # one_item = []
            title = li.find('h3',class_ = 'text-gray text-truncate mb-xs-0 text-body').text.strip()
            # one_item.append(title)
            
            price = li.find('span',class_ = 'currency-value').text
            # one_item.append(f'${price}')
            
            link = li.find('a',class_ = 'organic-impression display-inline-block listing-link').get('href')
            # one_item.append(link)
            
            one_item = Product(title, price, link, 'etsy')
            all_data.append(one_item)
            
            if len(all_data) == 5:
                break

        except:
            continue

    return all_data
    
    # with open('etsy_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerows(all_data)

if __name__ == "__main__":
    print(etsy('phone'))



  
        


    

    
   

    

    
    
    






    
    