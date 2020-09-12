import requests
from bs4 import BeautifulSoup
import json
import csv


class Shops :

    def __init__ (self ) : 
        self.product = input('looking for >>>   ') 
        

    def etsy(self):
        """
        this function will take the name of product as argument then
        go to the E_bay online store and bring a data about title and price and link about this product 
        after that it will save the data in csv file
        """
        url = f'https://www.etsy.com/search?q={self.product}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_data = [[]]

        elements = soup.find_all('li' )
        for li in elements:
            try:
                one_item = []
                title = li.find('h3',class_ = 'text-gray text-truncate mb-xs-0 text-body').text
                one_item.append(title)
                price = li.find('span',class_ = 'currency-value').text
                one_item.append(f'${price}')
                link = li.find('a',class_ = 'organic-impression display-inline-block listing-link').get('href')
                one_item.append(link)
                all_data.append(one_item)
            except:
                continue
        return all_data
    def e_bay(self):
        """
        this function will take the name of product as argument then
        go to the E_bay online store and bring a data about title and price and link about this product 
        after that it will save the data in csv file
        """
        url = f'https://www.ebay.com/sch/i.html?_nkw={self.product}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_data = [['title','price','links']]

        elements = soup.find_all('li',class_ = 's-item')

        for li in elements:
            try:
                one_item = []
                title = li.find('h3').text
                one_item.append(title)
                price = li.find('span',class_ = 's-item__price').text.split(' ')[0]
                one_item.append(price)
                link = li.find('a',class_ = 's-item__link').get('href')
                one_item.append(link)
                all_data.append(one_item)

            except:
                continue
        return all_data

    ''' this function to get dataset from walart website'''

    def walmart(self):
        url = f'https://www.walmart.com/search/?query={self.product}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        resultsss = soup.find_all('div' , role="presentation")
        all_data=[[]]


        for i in resultsss:
            try:
                each_product = []

                ### to get the name of the product
                title = i.find('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title').text
                each_product.append(title)

                ### to get the price of the product
                price = i.find('span',class_ = 'price-group').text
                each_product.append(price)

                #### to  get the url link for each product
                links = i.find('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title').get('href')
                each_product.append(f"https://www.walmart.com{links}")

                all_data.append(each_product)
            
                
            except :
                continue

        return all_data
        

    def newegg(self):
        """
        this function will take the name of product as argument then
        go to the newegg online store and bring a data about title and price and link about this product 
        after that it will save the data in csv file
        """
        url = f'https://www.newegg.com/p/pl?d={self.product}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        all_data = [[]]
        

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

        return all_data

    
    def print_data(self) : 
        print('connecting to ebay ...')
        all_shops = self.e_bay() 

        print('connecting to etsy ...')

        all_shops +=  self.etsy()

        print('connecting to newegg ...')

        all_shops += self.newegg()

        print('connecting to walmart ...')

        all_shops += self.walmart()

        with open('all_data.csv', 'w', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerows(all_shops)





    
if __name__ == "__main__":
    m = Shops()
    m.print_data()

