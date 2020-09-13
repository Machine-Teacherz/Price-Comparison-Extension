from bs4 import BeautifulSoup
import requests
import json
import csv
from modules.helpres import Product



def walmart(product):
    ''' 
    this function to get dataset from walart website
    '''

    url = f'https://www.walmart.com/search/?query={product}'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    resultsss = soup.find_all('div' , role="presentation")
    # all_data=[['title','price','links']]
    all_data = []

    for i in resultsss:
        

        if len(i.find_all('span',class_ = 'price-subscription-interval-unit')) > 0  :
            continue
        else:
            price = i.find('span',class_ = 'price-group').find('span', class_="price-characteristic").text



        try:
            # each_product = []

            ### to get the name of the product
            title = i.find('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title').text
            # each_product.append(title)
            
            if len(i.find_all('span',class_ = 'price-subscription-interval-unit')) > 0  :
                continue
            else:
                price = i.find('span',class_ = 'price-group').find('span', class_="price-characteristic").text

            #### to  get the url link for each product
            links = i.find('a',class_ = 'product-title-link line-clamp line-clamp-2 truncate-title').get('href')
            # each_product.append(f"https://www.walmart.com{links}")

            each_product = Product(title, price, f"https://www.walmart.com{links}", 'walmart')
            all_data.append(each_product)
           
            if len(all_data) == 5:
                break

            """ to get reviews for each product"""
            # reviews = i.find('span',class_ = 'seo-review-count visuallyhidden').text
            # each_product.append(reviews)
            
            """to get rating for each product """
            # rating = i.find('span',class_ = 'visuallyhidden seo-avg-rating').text
            # each_product.append(rating)              
        except :
            continue

    
    return all_data
       
    # ### to send the data sets into .csv file
    # with open('walmart_data.csv', 'w', newline='') as file:
    #     writer = csv.writer(file, delimiter=',')
    #     writer.writerows(all_data)  

def wal_price(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser').find('span',class_ = 'price-characteristic').get('content')
    return soup


if __name__ == "__main__":
    # print(wal_price('https://www.walmart.com/ip/onn-32-Class-720P-HD-LED-Roku-Smart-TV/314022535'))
    print(wal_price('https://www.walmart.com/ip/Straight-Talk-Apple-iPhone-11-Pro-Max-with-64GB-Silver/674137394'))
    # print(walmart('iphone11'))